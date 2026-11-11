const loginForm = document.querySelector('#login-form')
const logoutForm = document.querySelector('#logout-form');
const exampleGet1 = document.querySelector('#example-get-1');
const exampleGet2 = document.querySelector('#example-get-2');
const exampleGet3 = document.querySelector('#example-get-3');
const progressDog = document.querySelector('div#progress-dog');
const progressBar = document.querySelector('div#progress-ex2');

let token = null;
let currentUrl = null;


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


async function processResponse(response) {
    console.log(response);
    if (response.status == 401) {
        throw Error('Bad username or password');
    }
    const data = await response.json();
    return data;
}

async function getJSON(url, init) {
    const response = await fetch(url, init);
    if (!response.ok) {
        throw new Error(`HTTP ${response.status} ${response.statusText}`);
    }
    return response.json();
}

async function showDog() {
    try {
        progressDog.classList.remove("hide");
        const data = await getJSON('https://dog.ceo/api/breeds/image/random');
        document.querySelector('#image1').src = data.message;
    } catch (error) {
        console.error(error.message);
        M.toast({ html: error.message });
    } finally {
        progressDog.classList.add("hide");
    }
}


/* Hide elements */
do_logout();

/* Assign callbacks */


/* GET request and JSON response */
document.querySelector('#a-get-1').addEventListener('click', async event => showDog());



/* POST request with FormData */
document.querySelector('form#formpost').addEventListener('submit', async (event) => {
    event.preventDefault();

    document.querySelector('p#error-formpost').textContent = '';

    const username = document.querySelector('input#username-formpost').value;
    const password = document.querySelector('input#password-formpost').value;

    let formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            body: formData
        });
        var data = await processResponse(response);
        token = data['access_token'];
        do_login();
    } catch (error) {
        document.querySelector('p#error-formpost').textContent = error.message;
    }

});

/* POST request with JSON data */
document.querySelector('form#jsonpost').addEventListener('submit', async (event) => {
    event.preventDefault();

    document.querySelector('p#error-jsonpost').textContent = '';

    const username = document.querySelector('input#username-jsonpost').value;
    const password = document.querySelector('input#password-jsonpost').value;

    const loginData = {
        'username': username,
        'password': password
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        });
        var data = await processResponse(response);
        token = data['access_token'];
        do_login();
    } catch (error) {
        document.querySelector('p#error-jsonpost').textContent = error.message;
    }
});


document.querySelector('#btn-logout').addEventListener('click', event => {
    token = null;
    do_logout();

});




/* GET request with token authentication and JSON response */
document.querySelector('#a-get-2').addEventListener('click', async event => {
    document.querySelector('p#response-ex2').textContent = '';
    document.querySelector('div#progress-ex2').style.display = "block";

    let headers = new Headers();
    headers.append('Authorization', 'Bearer ' + token);
    try {
        const response = await fetch('http://127.0.0.1:5000/protected', {
            headers: headers
        });
        const data = await response.json();
        document.querySelector('div#progress-ex2').style.display = "none";
        document.querySelector('p#response-ex2').textContent = 'Logged in as ' + data['logged_in_as'];

    } catch (error) {
        M.toast({ html: error.message });
    } // https://materializecss.com/toasts.html

});

/* GET request and Blob response */
document.querySelector('#a-get-3').addEventListener('click', async event => {
    try {
        if (currentUrl) URL.revokeObjectURL(currentUrl);
        const response = await fetch('http://127.0.0.1:5000/image', {
            cache: "no-store",
        });
        const data = await response.blob();
        currentUrl = URL.createObjectURL(data);
        document.querySelector("#image2").src = currentUrl;
    } catch (error) {
        M.toast({ html: error.message });
    }

});
