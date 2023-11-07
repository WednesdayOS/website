let params = new URLSearchParams(window.location.search);
let username = params.get('username');
document.getElementById("username").textContent = username;

function loadlist(username) {
    fetch('https://api.bot.wednesdayos.com/get_unfollowers_list?username='+username)
        .then(response => response.text())
        .then(data => {
        document.getElementById('unfollowers-list').textContent = data;
        })
        .catch(error => {
        console.error('Error fetching data:', error);
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
    } else if (destinationURL == "dashboard.html"){
        window.open(destinationURL+'?username='+encodeURIComponent(username),'_self')
        document.getElementById("username").textContent = username;
        loadlist(username);
    } else {
        window.open(destinationURL+'?username='+encodeURIComponent(username),'_self')
        document.getElementById("username").textContent = username;
    }
}