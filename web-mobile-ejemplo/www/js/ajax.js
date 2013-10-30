function init() {
    var more = document.querySelector("#more");
    more.onclick = get_data;
}


function get_data(e) {
   var xmlhttp = new XMLHttpRequest();
   var num = 5;
   var offset = document.querySelectorAll("article").length;
   
   xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4) {
      
        switch (xmlhttp.status) {
            case 200: // OK!
                eventList = JSON.parse(xmlhttp.responseText);
                if (eventList.count < num) {
                    document.querySelector("#more").style.display = "none";
                } else {
                    for(var i = 0; i < eventList.count; i++) {
                        create_article(eventList.data[i]);
                    }
                }
            break;
            case 404: // Error: 404 - Resource not found!
                alert("Resource not found!");
            break;
            default:  // Error: Unknown!
        }
       }
   }

   xmlhttp.open("GET","http://localhost:8080/cgi-bin/events.py?n=" + num + "&offset=" + offset, false);
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
