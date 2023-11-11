let params = new URLSearchParams(window.location.search);
let username = params.get('username');
document.getElementById("username").textContent = username;

function loadlist() {
    var element = document.getElementById("username");
    var user = element.innerHTML;
    if (user.startsWith("@")) {
        console.log("username starts with @")
        user = user.slice(1);
        console.log(user);
    } else {
        console.log("String does not start with '@'.");
    }
    console.log(user)
    fetch('https://api.bot.wednesdayos.com/get_unfollowers_list?username='+user)
        .then(response => response.text())
        .then(data => {
        document.getElementById('unfollowers-list').innerHTML = data;
        })
        .catch(error => {
        console.error('Error fetching data:', error);
        document.getElementById('unfollowers-list').innerHTML = '<h6 class="inbox-message-error">Unable to Fetch List</h6>';
        });
}

function toggleSidebar() {
    var sidebar = document.querySelector(".sidebar");
    if (sidebar.classList.contains("sidebar-hidden")) {
        sidebar.classList.remove("sidebar-hidden");
    } else {
        sidebar.classList.add("sidebar-hidden");
    }
}

function redirectToPage(destinationURL) {
    const params = new URLSearchParams(window.location.search);
    const username = params.get('username');
    if (destinationURL == "index.html"){
        window.location.href = destinationURL;
    } else {
        window.open(destinationURL+'?username='+encodeURIComponent(username),'_self')
        document.getElementById("username").textContent = username;
    }
}