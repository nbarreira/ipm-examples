const descriptions = [
    "Lorem ipsum dolor sit amet.",
    "Ut at iaculis neque. In hac.",
    "Vestibulum elementum diam lectus, quis finibus ligula ultrices."
];

var validEmail = false;
const modal = document.querySelector("dialog#modal");
const modalInfo = document.querySelector("dialog#modal div#info");
const emailInput = document.querySelector("form input#field1");
const emailInputError = document.querySelector("form p#field1Error");
const selectInput = document.querySelector("form select#field2");
const description = document.querySelector("form p#field2Description");
const menuList = document.querySelector("nav ul");
const menuListButton = document.querySelector("header button");
const menuListButtonIcon = document.querySelector("header button i");

function setDescription() {
    let value = selectInput.value;
    description.innerText = descriptions[value]; 
}

function validateEmail() {
    let email = emailInput.value;
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function resetForm() {
    emailInput.value = "";
    emailInputError.classList.add("hidden");
    selectInput.selectedIndex = 0;
    setDescription();
}

menuListButton.addEventListener("click",  () => {
    const closed = menuList.hidden;
    menuList.hidden = !closed;
    console.log("tras cambio closed=", menuList.hidden);
    menuListButtonIcon.classList.toggle("fa-bars", !closed);
    menuListButtonIcon.classList.toggle("fa-xmark", closed);    
    menuListButton.setAttribute("aria-expanded", String(closed));
});


emailInput.addEventListener("blur", () => {
    validEmail = validateEmail();
    if (validEmail) {
        emailInputError.hidden = true;
        emailInput.setAttribute("aria-invalid", false);

    } else {
        emailInputError.hidden = false;
        emailInput.setAttribute("aria-invalid", true);
    }
    
});


selectInput.addEventListener("change", () => {
    setDescription(); 
});



document.querySelector("form").addEventListener("submit", (event) => {
    if (validEmail) {
        modalInfo.innerText = "Data sent!";
        modal.classList.remove("modal-error");
        //resetForm();
    } else {
        modalInfo.innerText = "Could not send the form due to errors: the email address is invalid";
        modal.classList.add("modal-error");
    }
    modal.showModal();
    event.preventDefault();
});

document.querySelector("dialog#modal .close").addEventListener("click", () => {
    modal.close();
    if (!modal.classList.contains("modal-error")) {
        resetForm();
    }
});

setDescription();

