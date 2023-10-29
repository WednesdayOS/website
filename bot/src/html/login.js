function checkString() {
    // Define the strings you want to check against
    const definedStrings = ["odai.exe", "aquasazure", "iadox"];

    // Get the input string from the user
    const inputString = document.getElementById("inputString").value;
    const messageElement = document.getElementById("message");

    // Check if the input string is defined
    if (definedStrings.includes(inputString)) {
        // Redirect to fol.html if the string is defined
        //window.location.href = "fol.html";
        document.getElementById("message").innerHTML = "Your account is registered but the service is not yet ready on web.";
        messageElement.style.color = "#02b4f5";
    } else {
        // Display an error message if the string is not defined
        document.getElementById("message").innerHTML = "Your account is not registered. Please contact @Wednesday.OS on Instagram";
        messageElement.style.color = "#fa1302";
    }
}