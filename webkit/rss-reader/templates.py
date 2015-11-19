# --*-- coding: utf-8 --*--

main_template = """
<!doctype html>

<html lang="en">

<head>
<meta charset="utf-8"/>
<title>Example RSS Feed Reader</title>
<script>
function show_loading() {{
  dialog = document.getElementById('loading');
  if (dialog) {{
    dialog.classList.remove('hidden');
  }}
}}

function hide_loading() {{
  dialog = document.getElementById('loading');
  if (dialog) {{
    dialog.classList.add('hidden');
  }}
}}
</script>
<style>
section > header h1 {{
  text-align: center;
}}
article header {{
  border-bottom: 1px solid #b9b9b9;
  border-top: 1px solid #f7f7f7;
  background: #ebebeb;
  background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#ffffff) to(#ebebeb));
  background-image: -webkit-linear-gradient(top, #ffffff, #ebebeb);
  background-image:    -moz-linear-gradient(top, #ffffff, #ebebeb);
  background-image:      -o-linear-gradient(top, #ffffff, #ebebeb);
  background-image:         linear-gradient(top, #ffffff, #ebebeb); 
}}
article header h1 {{
  padding-left: 1em;
  color: #55678d;
}}
.dialog {{
  display: block;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 80%;
  height: 50%;
  min-height: 3em;
  margin: auto;
  text-align: center;
  background: rgba(128,128,128,0.9);
  -webkit-border-radius: 10px;
}}
.hidden {{
  display: none;
}}
</style>
</head>

<body>

<section id="feedView">
<header>
  <h1>{title}</h1>
</header>
{articles}
</section>
</body>

<div id="loading" class="dialog hidden">
  <h1>Loading please wait</h1>
  <progress>loading ...</progress>
</div>
</html>

</html>
"""


feed_template = """
<article>
  <header>
    <h1>{title}</h1>
  </header>
  <p>{description}</p>
</article>
"""


loading_template = """
<!doctype html>
<html lang="en">

<head>
<meta charset="utf-8"/>
<title>Example RSS Feed Reader</title>
<style>
div#loading {{
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 80%;
  height: 50%;
  min-height: 3em;
  margin: auto;
  text-align: center;
}}
</style>
</head>

<body>
<div id="loading">
<h1>Loading please wait</h1>
<progress>loading ...</progress>
</div>
</body>
</html>
"""
