from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, CuDNNLSTM, Dense, Dropout, Bidirectional
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping
from keras.models import Sequential, model_from_json
import keras.utils as ku
import numpy as np
import codecs
import os



tokenizer = Tokenizer()
def dataset_preparation(data):
    corpus = data.lower().split("\n")   
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1
    
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
            
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences,   
                          maxlen=max_sequence_len, padding='pre'))
    
    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    label = ku.to_categorical(label, num_classes=total_words)
    return predictors, label, max_sequence_len, total_words
    
    
def create_model(predictors, label, max_sequence_len, total_words, mod_n):
#     input_len = max_sequence_len - 1
#     model = Sequential()
#     model.add(Embedding(total_words, 10, input_length=input_len))
#     model.add((CuDNNLSTM(150), input_shape=(total_words, 10, 1)))
#     model.add(Dropout(0.2))
#     model.add(Dense(total_words, activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam')
#     m = model.fit(predictors, label, epochs=1000, verbose=1)
    
#     model_json = model.to_json()
#     with open("model.json","w") as json_file:
#     	json_file.write(model_json)

#     model.save_weights("model.h5")
#     print("Saved model to disc...")
    loaded_model = None

    if mod_n == 0:
        json_file = open("Mainpage/assets/jeffery.json")
        loaded_model_json = json_file.read()
        json_file.close()

        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("Mainpage/assets/jeffery.h5")
        print("Loaded model from file..")

    if mod_n == 1:
        json_file = open("Mainpage/assets/modelnarayan.json")
        loaded_model_json = json_file.read()
        json_file.close()

        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("Mainpage/assets/modelnarayan.h5")
        print("Loaded model from file..")

    if mod_n == 2:
        json_file = open("Mainpage/assets/rowlings.json")
        loaded_model_json = json_file.read()
        json_file.close()

        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("Mainpage/assets/rowlings.h5")
        print("Loaded model from file..")

    return loaded_model



def generate_text(seed_text, next_words, max_sequence_len, model):
    for j in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen= 
                             max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
  
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

for ind in range(3):
    data = ""
    data_count = 0

    data_files = ["jeffery.txt","narayan.txt","rowlings.txt"]

    f = codecs.open((str(os.path.dirname(os.path.realpath(__file__))) + "/" + (data_files[ind])),"r",encoding="utf8",errors="ignore")
    lines = f.readlines()
    for i in lines:
        thisline = i.split(" ")
        for j in thisline:
            data_count += 1
            data += " "
            data += j

    f.close()

    X, Y, max_len, total_words = dataset_preparation(data)
    model = create_model(X, Y, max_len, total_words, ind)

    file = open(str(os.path.dirname(os.path.realpath(__file__))) + "/predictions.txt","r")
    text = file.read()
    no_of_predictions = int(text)

    file = open(str(os.path.dirname(os.path.realpath(__file__))) + "/story.txt","r")
    text = temp_data = file.read()
    story_data_length = len(temp_data.split(" "))
    for i in range(no_of_predictions):
        sentence = text
        text = generate_text(sentence, 1, max_len, model)
    file.close()
    temp_data = text
    output_data = temp_data.split(" ")
    generated_data = ""
    for appended_data in output_data[story_data_length:]:
        generated_data += appended_data + " "

    with open(str(os.path.dirname(os.path.realpath(__file__))+"/../static/upload/"+data_files[ind]), "w") as file:
        file.write(generated_data)

    with open(str(os.path.dirname(os.path.realpath(__file__))) + "/output.txt","w") as file:
        file.write(text)

