const loginForm = document.querySelector('#login-form')
const logoutForm = document.querySelector('#logout-form');
const exampleGet1 = document.querySelector('#example-get-1');
const exampleGet2 = document.querySelector('#example-get-2');
const exampleGet3 = document.querySelector('#example-get-3');
const progressBar = document.querySelector('div#progress-ex2');

var token = null;


function do_login() {
    logoutForm.style.display = 'block'; 
    exampleGet1.style.display = 'none';
    exampleGet2.style.display = 'block';
    exampleGet3.style.display = 'block';

    loginForm.style.display = 'none';
    progressBar.style.display = "none";
}

function do_logout() {
    logoutForm.style.display = 'none'; 
    exampleGet1.style.display = 'block';
    exampleGet2.style.display = 'none';
    exampleGet3.style.display = 'none';

    loginForm.style.display = 'block'; 
}


function handleErrors(response) {
    console.log(response);
    if (response.status == 401) {
        throw Error('Bad username or password');
    }
    return response.json();
}





/* Hide elements */
do_logout();

/* Assign callbacks */

/* GET request and JSON response */
document.querySelector('#a-get-1').addEventListener('click',event  => {
        fetch("https://dog.ceo/api/breeds/image/random")
        .then(response => response.json())
        .then(data => document.querySelector("#image1").src = data['message'])
        .catch(error => M.toast({html: error.message})); // https://materializecss.com/toasts.html
});



/* POST request with FormData */
document.querySelector('form#formpost').addEventListener('submit', event => {
        document.querySelector('p#error-formpost').textContent = '';

        const username = document.querySelector('input#username-formpost').value;
        const password = document.querySelector('input#password-formpost').value;

        let formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        fetch('http://localhost:5050/login',{
            method: 'POST',
            body: formData
        })
        .then(handleErrors)
        .then(data => {
            token = data['access_token'];
            do_login();
        })
        .catch(error => document.querySelector('p#error-formpost').textContent = error.message); 

        event.preventDefault();
});

/* POST request with JSON data */
document.querySelector('form#jsonpost').addEventListener('submit', (event) => {
        document.querySelector('p#error-jsonpost').textContent = '';

        const username = document.querySelector('input#username-jsonpost').value;
        const password = document.querySelector('input#password-jsonpost').value;

        const data = {
            'username': username,
            'password': password
        };
        
        fetch('http://localhost:5050/login',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(handleErrors)
        .then(data => {
            token = data['access_token'];
            do_login();
        })
        .catch(error => document.querySelector('p#error-jsonpost').textContent = error.message);
        
        event.preventDefault();
});


document.querySelector('#btn-logout').addEventListener('click', event => {
        token = null;
        do_logout();

});


    

    /* GET request with token authentication and JSON response */
document.querySelector('#a-get-2').addEventListener('click', event => {
        document.querySelector('p#response-ex2').textContent = '';
        document.querySelector('div#progress-ex2').style.display = "block";

        let headers = new Headers();
        headers.append('Authorization', 'Bearer ' + token);
        fetch('http://localhost:5050/protected',{
            headers: headers
        })
        .then(response => response.json())
        .then(data => {
            document.querySelector('div#progress-ex2').style.display = "none";
            document.querySelector('p#response-ex2').textContent = 'Logged in as ' + data['logged_in_as'];
        })
        .catch(error => M.toast({html: error.message})); // https://materializecss.com/toasts.html

}); 
    
    /* GET request and Blob response */
document.querySelector('#a-get-3').addEventListener('click',event => {
        console.log("fetching");
        document.querySelector("#image2").src = '';
        let headers = new Headers();
        headers.append('pragma', 'no-cache');
        headers.append('cache-control', 'no-cache');

        fetch('http://localhost:5050/image',{
            headers: headers,
        })
        .then(response => response.blob())
        .then(data => {
            const url = URL.createObjectURL(data);
            document.querySelector("#image2").src = url;  
         })
        .catch(error => M.toast({html: error.message})); // https://materializecss.com/toasts.html

});
