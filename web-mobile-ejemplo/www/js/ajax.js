function init() {
    var more = document.querySelector("#more");
    more.onclick = get_data;
}


function get_data(e) {
   e.preventDefault();
   var xmlhttp = new XMLHttpRequest();
   var num = 5;
   var offset = document.querySelectorAll("article").length;
   
   xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4) {
      
        switch (xmlhttp.status) {
            case 200: // OK!
                response = JSON.parse(xmlhttp.responseText);
                rows = response.rows;
                if (rows.length < num) {
                    document.querySelector("#more").style.display = "none";
                } 
                for(var i = 0; i < rows.length; i++) {
                    create_article(rows[i].value);
                }                
            break;
            case 404: // Error: 404 - Resource not found!
                alert("Resource not found!");
            break;
            default:  // Error: Unknown!
        }
       }
   }

  // cgi request
  // xmlhttp.open("GET","http://localhost:8080/cgi-bin/events.py?n=" + num + "&offset=" + offset, true);
  
  // couchdb request: 
  //  1. Habilitar CORS 
  //     http://docs.couchdb.org/en/1.4.x/configuring.html#cross-origin-resource-sharing
  //  2. Necesario crear documento de diseño Event/by_date
  //     function (doc) { if (doc.type == 'Event') { emit (doc.date, doc); } }
   xmlhttp.open("GET", "http://localhost:5984/calendar/_design/Event/_view/by_date?limit="+ num + "&skip=" + offset, true);
   xmlhttp.send();
}


function create_element(parent, type, className, data) {
    var element = document.createElement(type);
    element.className = className;
    element.innerHTML = data;
    parent.appendChild(element);
}

function create_article(event) {
    var article = document.createElement("article");
    create_element(article, "time", "", event.date);
    create_element(article, "h1", "", event.description);
    create_element(article, "p", "tags", event.tags);
    create_element(article, "p", "creator", event.creator);
    
    var section = document.querySelector("section");
    section.appendChild(article);
    
    
}
