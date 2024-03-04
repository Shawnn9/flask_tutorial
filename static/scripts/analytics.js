        var dropdowns = document.querySelectorAll('.dropdown');

        dropdowns.forEach(function(dropdown) {
            var button = dropdown.querySelector('.dropbtn');
            var content = dropdown.querySelector('.dropdown-content');

            button.addEventListener('click', function() {
                content.classList.toggle('show');
            });
        });
        window.onclick = function(event) {
            if (!event.target.matches('.dropbtn')) {
                dropdowns.forEach(function(dropdown) {
                    var content = dropdown.querySelector('.dropdown-content');
                    if (content.classList.contains('show')) {
                        content.classList.remove('show');
                    }
                });
            }
        }