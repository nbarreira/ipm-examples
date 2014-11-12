page_template="""
<!doctype html>

<html lang="en">

<head>
	<meta charset="utf-8"/>
	<title>IPM-MovieDB-WEBKIT</title>
	<link rel="stylesheet" type="text/css" media="all" href="lib/jquery.bxslider.css" />
	
</head>

<body>
<div id="wrapper">	
	<div class="slider">
		<ul class="bxslider">
			{movies}
		</ul>
		
	</div>
</div>	

<script type="text/javascript" src="lib/jquery.min.js"></script>
<script src="lib/jquery.bxslider.min.js"></script>
<script>
  $(document).ready(function() {{
	$('.bxslider').bxSlider({{
	  mode: 'horizontal',
	  captions: true,
	  controls: true,
	  auto: true
	}});
  }}); 
  function test() {{
  	console.log("[JAVASCRIPT] on test");
  	var body = document.querySelector("body");
  	body.style.backgroundColor = "#000";
  }}   
</script>
</body>

</html>
"""

movie_template="""
	<li> 
		<a href="#"><img src="{url_image}"  alt="Image" title="{title}" /></a>
	</li>
"""
