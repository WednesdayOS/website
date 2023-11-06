function checkString() {
    let inputString = document.getElementById("inputString").value.toLowerCase();
    const messageElement = document.getElementById("message");

    if (inputString.startsWith("@")) {
        console.log("username starts with @")
        inputString = inputString.slice(1);
        console.log(inputString);
    } else {
        console.log("String does not start with '@'.");
    }
    fetch('https://api.bot.wednesdayos/is_registered?username='+user, {
        method: 'GET'
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (inputString == "") {
                document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
                messageElement.style.color = "#fa1302"; 
            } else if (response.status === 200) {
                messageElement.style.color = "#00ff44";
                messageElement.innerHTML = "You're registered, redirecting to dashboard...";
                fetch('https://api.bot.wednesdayos/gen_co?username='+inputString, {
                    method: 'GET',
                    mode: 'no-cors'
                    }); 
                showPopup()

            } else if (response.status === 403) {
                document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
                messageElement.style.color = "#fa1302";
            } else {
                document.getElementById("message").innerHTML = "Your account is not registered. Please contact @Wednesday.OS on Instagram";
                messageElement.style.color = "#fa1302";
            }
        })
        .catch(error => {
            errorText.textContent = "Error occurred, please try again.";
        });
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
    fetch('https://api.bot.wednesdayos/auth?username='+user+'&etoken='+input2faCode, {
        method: 'GET'
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (response.status === 200) {
                window.location.href = "about.html";
                window.location.href = 'about.html?username=@'+encodeURIComponent(user);

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