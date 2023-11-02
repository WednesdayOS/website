function checkString() {
    const definedStrings = ["odai.exe", "ellieshxnnon", "wakeupitsasimulation", "ineverdrinkwater"];

    const inputString = document.getElementById("inputString").value;
    const messageElement = document.getElementById("message");

    if (definedStrings.includes(inputString)) {
        messageElement.style.color = "#00ff44";
        messageElement.innerHTML = "You're registered, redirecting to dashboard...";
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


    fetch('https://bot-api.wednesdayos.com/get_2fa?user='+user)
        .then(response => response.text())
        .then(storedCode => {
            if (input2faCode === storedCode) {
                window.location.href = "about.html";
            } else {
                errorText.textContent = "Incorrect 2FA code.";
            }
        })
        .catch(error => {
            errorText.textContent = "Error reading 2FA code, please wait 1 min and try again";
        });
}