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
    window.location.href = destinationURL;
}