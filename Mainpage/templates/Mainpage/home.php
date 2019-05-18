
	<!-- <?php
		$x = 600;
		$current_time = time();
		$file_name = 'story.txt';
		$file_creation_time = filemtime($file_name);
		$difference = $current_time - $file_creation_time;
		if ($difference >= $x) {
			file_put_contents($file_name, "");
		}
	?> -->
	{% block content %}
	{% load static from staticfiles %}
	<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<!-- <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'"> -->
	<title>Online-Story-Generator</title>
	<link href="https://fonts.googleapis.com/css?family=Euphoria+Script|Poppins|Amatic+SC|Encode+Sans+Condensed" rel="stylesheet">
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
	<style type="text/css">
		html, body {
      position: relative;
		  height: 100%;
		  width: 90%;
		  background-color: #e9ecef;
		  padding: 0vh;
		}

		.btn {
		  background-color: #000;
		}

		.main {
		  padding-top: 2%;
		  padding-left: 5%;
		}

		.row {
		  padding: 1%;
		}

		.area {
		  padding-top: 5%
		}




		/*[class*="col-sm-5"] {
		    padding: 10%;
		}*/
		.badge {
			margin-top: 5px;
		}

		textarea {
			resize: none;
		}

		[class*="col-sm-1"] {
		  margin-right: 1px;
		  margin-top: 2px;
		}
	</style>
	<link href="{% static 'upload/animate.css' %}" rel="stylesheet">
	<link href="{% static 'upload/bootstrap-social.css' %}" rel="stylesheet">

	<div class="main">
		<form class="ml-form" autocomplete="off" action="{% url 'execute' %}" method="post">
		{% csrf_token %}	
			<div class="row">
				<div class="col-sm-8">
					<input name="name" class="form-control form-control-lg" type="text" placeholder="Seed Text">
				</div>			
				<input class="col-sm-1 btn btn-primary" type="submit" value="Send">
			</div>
		</form>

		<form class="ml-form" autocomplete="off" action="{% url 'append' %}" method="post">
			{% csrf_token %}
			<div class="row">
				<div class="col-sm-2">
				<input class="form-control bg-secondary text-white form-control" type="text" name="jeffery" value="Jeffery Deaver">
				</div>
				<div class="col-sm-4">
				<textarea  class="form-control form-control-lg" type="text" placeholder="{{ jeffery }}" rows="1"></textarea>
				</div>		
				<input class="col-sm-1 btn btn-primary" type="submit" value="Append">
			</div>
		</form>
		
		<form class="ml-form" autocomplete="off" action="{% url 'append' %}" method="post">
			{% csrf_token %}
			<div class="row">
				<div class="col-sm-2">
				<input class="form-control bg-secondary text-white form-control" type="text" name="narayan" value="R. K. Narayan">
				</div>
				<div class="col-sm-4">
				<textarea  class="form-control form-control-lg" type="text" placeholder="{{ narayan }}" rows="1"></textarea>
				</div>			
				<input class="col-sm-1 btn btn-primary" type="submit" value="Append">
			</div>
		</form>

		<form class="ml-form" autocomplete="off" action="{% url 'append' %}" method="post">
			{% csrf_token %}
			<div class="row">
				<div class="col-sm-2">
				<input class="form-control bg-secondary text-white form-control" type="text" name="rowlings" value="J. K. Rowlings">
				</div>
				<div class="col-sm-4">
				<textarea class="form-control form-control-lg" type="text" placeholder="{{ rowlings }}" rows="1"></textarea>
				</div>			
				<input class="col-sm-1 btn btn-primary" type="submit" value="Append">
			</div>
		</form>

		<div class=" col-sm-9 area">
			<textarea name="story" id="story" class="form-control form-control-lg" type="text" placeholder="Story" rows="5">{{ data }}</textarea>
		</div>
		

		<form class="ml-form" autocomplete="off" action="{% url 'generate' %}" method="post">
			{% csrf_token %}
			<div class="row">
				<div class="col-sm-4">
					<input class="btn btn-primary" type="submit" value="Generate">
				</div>
				<div class="col-sm-4">
					<div class="container">
						<h4><span class="badge badge-secondary">Next number of word predictions</span></h4>
					</div>
				</div>
				<div class="col-sm-1">
					<input id="predictions" name="predictions" class="form-control" type="text" value="3">
				</div>
			</div>
		</form>
	</div>


	{% endblock %}
</body>

