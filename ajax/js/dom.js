var movies_dom = (function() {

    var api = null;

    function set_movie(data) {
      document.querySelector(".message").innerHTML = '';
      var dds = document.querySelectorAll("dd");
      var i = 0;
      dds[i++].innerHTML = data["original_title"];
      dds[i++].innerHTML = data["release_date"];
      dds[i++].innerHTML = data["vote_average"];
      dds[i++].innerHTML = data["vote_count"];
      dds[i++].innerHTML = data["overview"];
      if (data["poster_path"] != null) {
          var img = document.querySelector("figure img");
          img.src = api.image_url + api.poster_size + data["poster_path"];
      }

      document.querySelector("#movie_id").value = data["id"];
      document.querySelector("section#details").style.display = "block";
      // Reset data
      document.querySelector(".message").innerHTML = '';
      var stars = document.querySelectorAll(".star");
      for(var i = 0; i < stars.length; i++) {
          stars[i].className = "star fa fa-star-o";
          stars[i].style.color = "black";
      }


    }

    function create_row(id, title, date, img_src) {

      var td_poster = document.createElement("td");
        if (img_src != null) {
          var img = document.createElement("img");
          img.src = api.image_url + api.thumbnail_size + img_src;
          td_poster.appendChild(img);
        }

        var a = document.createElement("a");
        a.href="#";
        a.onclick = function() {
            api.find(id, set_movie, log)
        }
        a.innerHTML= title;
        var td_title = document.createElement("td");
        td_title.appendChild(a);

        var td_date = document.createElement("td");
        td_date.innerHTML = date.substring(0,4);

        var tr = document.createElement("tr");
        tr.appendChild(td_poster);
        tr.appendChild(td_title);
        tr.appendChild(td_date);

        return tr;
    }
    function create_empty_row() {
        var td = document.createElement("td");
        td.colSpan = 3;
        td.innerHTML = "No results";
        td.className = "info";
        var tr = document.createElement("tr");
        tr.appendChild(td);
        return tr;
    }


    function set_movie_list(data) {
        var old_tbody = document.querySelector("tbody");
        var new_tbody = document.createElement("tbody");
        if (data["results"].length > 0) {
            for (var i = 0; i < data["results"].length; i++) {
                new_tbody.appendChild(create_row(data["results"][i]["id"], data["results"][i]["title"], data["results"][i]["release_date"], data["results"][i]["poster_path"]));
            }
        } else {
            new_tbody.appendChild(create_empty_row());
        }
        old_tbody.parentNode.replaceChild(new_tbody, old_tbody);

    }

    function log(text) {
        console.log(text);
    }

    function show_message(data) {
        document.querySelector(".message").innerHTML = data["status_message"];
    }

    function init(movie_api) {
        api = movie_api;
        document.querySelector("#details").style.display = "none";
        document.querySelector("#query").onsearch = function(e) {
            api.search(e.target.value, set_movie_list, log);
        }
        document.querySelector("#search").onclick = function() {
            var title = document.querySelector("#query").value;
            api.search(title, set_movie_list, log);
        }
        document.querySelector("#rate").onclick = function() {
            var vote = document.querySelectorAll(".fa-star").length * 2; // Range in themoviedb is (0,10)
            var movie_id = document.querySelector("#movie_id").value;
            api.rate(movie_id, vote, show_message, log);
        }
        var stars = document.querySelectorAll(".star");
        for(var i = 0; i < stars.length; i++) {
            stars[i].onclick = function(e) {
                var j = 0;
                while (stars[j] != e.target) {
                    stars[j].className = "star fa fa-star";
                    stars[j].style.color = "gold";
                    j++;
                }
                stars[j].className = "star fa fa-star";
                stars[j].style.color = "gold";
                j++;
                while (j < stars.length) {
                    stars[j].className = "star fa fa-star-o";
                    stars[j].style.color = "black";
                    j++;
                }
            }
        }

    }

    return {
        init: init
    };

})();
