function checkString() {
    const definedStrings = ["odai.exe", "Test", "test"];

    const inputString = document.getElementById("inputString").value;
    const messageElement = document.getElementById("message");

    if (definedStrings.includes(inputString)) {
        messageElement.style.color = "#00ff44";
        messageElement.innerHTML = "You're registered, redirecting to dashboard...";
        window.location.href = "about.html";
    } else if (inputString == "") {
        document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
        messageElement.style.color = "#fa1302";
    } else {
        document.getElementById("message").innerHTML = "Your account is not registered. Please contact @Wednesday.OS on Instagram";
        messageElement.style.color = "#fa1302";
        window.location.href = "about.html";
    }
}