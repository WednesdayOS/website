let params = new URLSearchParams(window.location.search);
let username = params.get('username');
document.getElementById("username").textContent = username;

function addNamesFromTextFile() {
    const nameList = document.getElementById('name-list');

    fetch('./followers.txt')
        .then(response => response.text())
        .then(data => {
            const names = data.split('\n');
            const ul = document.createElement('ul');

            names.forEach(function (name) {
                const li = document.createElement('li');
                li.textContent = name;
                ul.appendChild(li);
            });

            nameList.innerHTML = '';
            nameList.appendChild(ul);
        })
        .catch(error => {
            console.error('Error fetching names.txt:', error);
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

function LogOut() {
    window.location.href = "index.html";
}

function redirectToPage(destinationURL) {
    const params = new URLSearchParams(window.location.search);
    const username = params.get('username');
    //window.location.href = destinationURL+'?username='+encodeURIComponent(username);
    window.open(destinationURL+'?username='+encodeURIComponent(username),'_self')
    document.getElementById("username").textContent = username;
}