var themoviedb = (function() {

    var url = "https://api.themoviedb.org/3";
    var api_key = "COPY_YOUR_API_KEY_HERE";
    var image_url = "http://image.tmdb.org/t/p/";
    var thumbnail_size = "w92/";
    var poster_size = "w185/";
    var guest_session_id = null;


    function async_request(method, path, params, callback, on_error, isAsync) {
        var xhttp = new XMLHttpRequest();
        var location = url + path + "?api_key=" + api_key;
        var post_params = '';

        if (params != null) {
            if (params["GET"] != null) {
                for(var key in params["GET"]) {
                    location += '&' + key + "=" + params["GET"][key];
                }
            }
        }

        console.log(location);

        xhttp.open(method, location, isAsync);

        if (params != null) {
            if (params["HEADERS"] != null) {
                for (var key in params["HEADERS"]) {
                    xhttp.setRequestHeader(key, params["HEADERS"][key]);
                }
            }
        }

        xhttp.onreadystatechange = function () {
            if (this.readyState == 4) {
                if ((this.status == 200) || (this.status == 201)){
                    callback(JSON.parse(this.responseText));
                } else {
                    on_error(this.status);
                }
            }
        }
        if (params != null && params["POST"] != null) {
            xhttp.send(params["POST"]);
        } else {
            xhttp.send();
        }
    }

    function search(query, callback, on_error) {
        var params = {
            "GET": {"query": query}
        };
        async_request("GET", "/search/movie", params, callback, on_error, true);
    }

    function find(id, callback, on_error) {
      async_request("GET", "/movie/" + id, null, callback, on_error, true);
    }

    function log(text) {
        console.log(text);
    }

    function set_guess_session(data) {
        if (data["success"]) {
            guest_session_id = data["guest_session_id"];
        } else {
            log(data);
        }
    }

    function create_guest_session() {
        async_request("GET", "/authentication/guest_session/new", null, set_guess_session, log, false);
    }


    function rate(id, vote, callback, on_error) {
        if (guest_session_id == null) {
            create_guest_session();
        }
        if (guest_session_id != null) {
            var params = {
                "GET": {"guest_session_id": guest_session_id},
                "POST": JSON.stringify({'value':  vote }),
                "HEADERS": {"Content-Type": "application/json;charset=utf-8"}
            };
            async_request("POST", "/movie/" + id + "/rating", params, callback, on_error, true);
        }
    }

    return {
        image_url: image_url,
        thumbnail_size: thumbnail_size,
        poster_size: poster_size,
        search: search,
        find: find,
        rate: rate
    }
}
)();
