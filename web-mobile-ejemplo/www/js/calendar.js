function calendar_init() {
  var items = document.querySelectorAll("nav ul li");
  for (var i = 0; i < items.length; i++) {
    var a = items[i].querySelector("a");
    var currentSubject = a.innerHTML.trim();
    a.href = "#";
    a.onclick = function(e) { 
        var selectedSubject = document.querySelector("li.selected");
        selectedSubject.className = "";        
        var a = e.currentTarget;
        var currentSubject = a.innerHTML.trim();
        a.parentElement.className = "selected";
        change_subjects(currentSubject); 
        return false; 
        
    }    
  }
}


function change_subjects(currentSubject) {

    var articles = document.querySelectorAll("article");
    var selectedSubject = document.querySelector("li.selected a").innerHTML.trim();
    var sectionTitle = document.querySelector("section  h1");
    sectionTitle.innerHTML = "Lista de eventos de " + selectedSubject;
  
    for (var i = 0; i < articles.length; i++) {
        if (selectedSubject == "Todas") {
            articles[i].style.display = "block";
        } else { 
            var tags = articles[i].querySelector(".tags").innerHTML.trim();
            if (tags.indexOf(currentSubject) != -1) {
                articles[i].style.display = "block";   
            } else {
                articles[i].style.display = "none";                    
            }
        }
    } 
}
