const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(function(dropdown) {
    const button = dropdown.querySelector('.dropbtn');
    const content = dropdown.querySelector('.dropdown-content');

    button.addEventListener('click', function() {
                content.classList.toggle('show');
            });
        });
        window.onclick = function(event) {
            if (!event.target.matches('.dropbtn')) {
                dropdowns.forEach(function(dropdown) {
                    const content = dropdown.querySelector('.dropdown-content');
                    if (content.classList.contains('show')) {
                        content.classList.remove('show');
                    }
                });
            }
        }