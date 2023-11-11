let gip, gctry, gct;
async function fetchIPInfo() {
    try {
      const response = await fetch('https://api.bot.wednesdayos.com/get_ip');
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data = await response.json();
  
      console.log('Raw data from API:', data);
  
      const ip = data.ip_address;
      const country = data.country;
      const city = data.city;

      return { ip, country, city };
    } catch (error) {
      console.error('Error fetching IP info:', error.message);
      throw error;
    }
}

fetchIPInfo()
    .then(ipInfo => {
      gip = ipInfo.ip;
      gctry = ipInfo.country;
      gct = ipInfo.city;
      console.log(`IP: ${gip}, Country: ${gctry}, City: ${gct}`);
    })
    .catch(error => {
      console.error('Error in exampleUsage:', error.message);
    });  

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
    console.log(inputString)
    if (inputString == "") {
        document.getElementById("message").innerHTML = "Please Enter a valid instagram username.";
        messageElement.style.color = "#fa1302"; 
    } else {
        fetch('https://api.bot.wednesdayos.com/is_registered?username='+inputString, {
        method: 'GET'
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (response.status === 200) {
                messageElement.style.color = "#00ff44";
                messageElement.innerHTML = "You're registered, requesting 2FA Token...";
                fetch('https://api.bot.wednesdayos.com/gen_co?username='+inputString+'&ip='+gip+'&ctry='+gctry+'&ct='+gct, {
                    method: 'GET',
                    mode: 'cors'
                }); 
                showPopup()
            } else if (response.status === 403) {
                document.getElementById("message").innerHTML = "Your account is not registered. Please contact @odai.exe on Instagram";
                messageElement.style.color = "#fa1302";
            } else {
                document.getElementById("message").innerHTML = "????🙂";
                messageElement.style.color = "#fa1302";
            }
        })
        .catch(error => {
            errorText.textContent = "Some error occurred, please try again.";
        });
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
    const user = inputElement.value.toLowerCase();
    fetch('https://api.bot.wednesdayos.com/auth?username='+user+'&etoken='+input2faCode, {
        method: 'GET'
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (response.status === 200) {
                window.open('about.html?username=@'+encodeURIComponent(user), '_self')
            } else if (response.status === 403) {
                window.location.href = "error.html";
            } else {
                errorText.textContent = "Unknown error occurred.";
            }
        })
        .catch(error => {
            errorText.textContent = "Some error occurred, please try again.";
        });
}