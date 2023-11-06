function checkString() {
    let username = document.getElementById("username").value.toLowerCase();
    let email = document.getElementById("email").value.toLowerCase();
    const messageElement = document.getElementById("message");

    if (username.startsWith("@")) {
        console.log("username starts with @")
        username = username.slice(1);
        console.log(username);
    } else {
        console.log("String does not start with '@'.");
    }
    console.log(username)
    if (username == "") {
        document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
        messageElement.style.color = "#fa1302"; 
    }else if (email == ""){
        document.getElementById("message").innerHTML = "Please Enter a valid email."
        messageElement.style.color = "#fa1302"; 
    } else {
        fetch('https://api.bot.wednesdayos.com/register_user?username='+username+'&email='+email, {
        method: 'GET'
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (response.status === 200) {
                messageElement.style.color = "#00ff44";
                messageElement.innerHTML = "User registered successfully!";
            } else if (response.status === 403) {
                document.getElementById("message").innerHTML = "An error occured, likely user or email already exists";
                messageElement.style.color = "#fa1302";
            } else {
                document.getElementById("message").innerHTML = "Error ("+response.status+"): exit code was not defined by the backend API";
                messageElement.style.color = "#fa1302";
            }
        })
        .catch(error => {
            errorText.textContent = "Some error occurred, please try again.";
        });
    }
}