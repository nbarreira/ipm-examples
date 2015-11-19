
page = dict()
item = dict()
page["book"] = """
<html>
	<head>

        <link href='https://fonts.googleapis.com/css?family=Slabo+27px' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
		<script type="text/javascript" src="js/funcs.js"></script>

	</head>
	
	<body>
	
	    <div class="books">
            <div class="cover">
                <img src="{image}" alt="{title}" />
                <br />
                <button>
                    Open
                </button>
                <button>
                    Send
                </button>
            </div>
            <div class="data">
            	<dl>
            	    <dt>Title</dt>
            	    <dd>{title}</dd>
            	    <dt>Author</dt>
            	    <dd>{author}</dd>
            	    <dt>Publication year</dt>
            	    <dd>{year}</dd>
            	    <dt>Editorial</dt>
            	    <dd>{editorial}</dd>
            	    <dt>Synopsis</dt>
            	    <dd>{synopsis}</dd>
            	</dl>
               	<a href="#">Back</a>
	      	</div>
   	</div>
		
	</body>
</html>
"""


page["table"] = """
<html>
	<head>
        <link href='https://fonts.googleapis.com/css?family=Slabo+27px' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
		
		<script type="text/javascript" src="js/funcs.js"></script>
		
	</head>
		
	
	<body>
	
	
		<table>
			<tr>
				<th>Cover</th>
				<th>Title</th>
				<th>Author</th>
				<th>Editorial</th>
				<th>Year</th>
			</tr>
			{library}
		</table>
	</body>
</html>
"""


item["table"] = """
<tr>
	<td><img src="{image}" alt="cover" /></td>
	<td><a href="#{bookId}">{title}</a></td>
	<td>{author}</td>
	<td>{editorial}</td>
	<td>{year}</td>
</tr>
"""
