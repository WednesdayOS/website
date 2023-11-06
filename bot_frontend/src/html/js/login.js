function checkString() {
    const definedStrings = ["odai.exe", "wednesday.os", "ellieshxnnon", "wakeupitsasimulation", "ineverdrinkwater"];

    const inputString = document.getElementById("inputString").value;
    const messageElement = document.getElementById("message");

    if (definedStrings.includes(inputString)) {
        messageElement.style.color = "#00ff44";
        messageElement.innerHTML = "You're registered, redirecting to dashboard...";
        fetch('https://api.bot.wednesdayos.com/gen_co?username='+inputString);
        showPopup()
    } else if (inputString == "") {
        document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
        messageElement.style.color = "#fa1302";
    } else {
        document.getElementById("message").innerHTML = "Your account is not registered. Please contact @Wednesday.OS on Instagram";
        messageElement.style.color = "#fa1302";
    }
}

const overlay = document.getElementById("overlay");
const errorText = document.getElementById("errorText");

function handleKeydown(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent the form from being submitted (if it's inside a form)
      showPopup();
    }
}

function showPopup() {
    overlay.style.display = "block";
}

function submit2faCode() {
    const input2faCode = document.getElementById("2faCode").value;
    const inputElement = document.getElementById("inputString");
    const user = inputElement.value;

    fetch('https://api.bot.wednesdayos.com/auth?username='+user+'&etoken='+input2faCode)
        .then(response => {
            if (response.status === 200) {
                window.location.href = "about.html";
            } else if (response.status === 403) {
                window.location.href = "error.html";
            } else {
                errorText.textContent = "Unknown error occurred.";
            }
        })
        .catch(error => {
            errorText.textContent = "Error occurred, please try again.";
        });
}