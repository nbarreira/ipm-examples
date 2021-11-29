const descriptions = [
    "Lorem ipsum dolor sit amet.",
    "Ut at iaculis neque. In hac.",
    "Vestibulum elementum diam lectus, quis finibus ligula ultrices."
];

var validEmail = false;


function setDescription() {
    let value = document.querySelector("form select#field2").value;
    document.querySelector("form p#field2Description").innerText = descriptions[value]; 
}

function validateEmail() {
    let email = document.querySelector("form input#field1").value;
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function resetForm() {
    document.querySelector("form input#field1").value = "";
    document.querySelector("form select#field2").selectedIndex = 0;
    setDescription();
}

document.querySelector("nav button").addEventListener("click", function (event) {
    document.querySelector("nav ul").classList.toggle("open");
    document.querySelector("nav button i").classList.toggle("fa-close");
});


document.querySelector("form input#field1").addEventListener("change", function (event) {
    validEmail = validateEmail();
     if (validEmail) {
        document.querySelector("form p#field1Error").classList.add("hidden");
    } else {
        document.querySelector("form p#field1Error").classList.remove("hidden");
    }
    
});


document.querySelector("form select#field2").addEventListener("change", function(event) {
    setDescription(); 
});



document.querySelector("form").addEventListener("submit", function(event) {
    let modal = document.querySelector("div#modal");
    let modalInfo = document.querySelector("div#modal div#info");
    if (validEmail) {
        modalInfo.innerText = "Data sent!";
        modal.classList.remove("modal-error");
        resetForm();
    } else {
        modalInfo.innerText = "Could not send the form due to errors: the email address is invalid";
        modal.classList.add("modal-error");
    }
    modal.classList.remove("hidden");


    event.preventDefault();
});

document.querySelector(".close").addEventListener("click", function(event) {
    document.querySelector("div#modal").classList.toggle("hidden");
});

setDescription();

