// scripts.js

$(document).ready(function() {
    // Sidebar Toggle for Mobile
    $('#sidebarToggle').on('click', function() {
        $('.sidebar').toggleClass('collapsed');
    });

    // Form Validation using Bootstrap's validation styles
    var contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(event) {
        if (!contactForm.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        contactForm.classList.add('was-validated');
    }, false);

    // Initialize Charts with Data from Flask APIs

    // Donut Chart
    fetch('/api/raw-data')
        .then(response => response.json())
        .then(data => {
            // Process data as needed
            var labels = data.map(item => item.Category); // Adjust based on your CSV structure
            var values = data.map(item => item.Value); // Adjust based on your CSV structure

            var ctxDonut = document.getElementById('donutChart').getContext('2d');
            var donutChart = new Chart(ctxDonut, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: ['#3498DB', '#2ECC71', '#E74C3C']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error('Error fetching raw data:', error));

    // Line Trend Chart
    fetch('/api/raw-data')
        .then(response => response.json())
        .then(data => {
            // Process data as needed
            var labels = data.map(item => item.Month); // Adjust based on your CSV structure
            var values = data.map(item => item.Trend); // Adjust based on your CSV structure

            var ctxLine = document.getElementById('lineTrendChart').getContext('2d');
            var lineTrendChart = new Chart(ctxLine, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Trend Over Time',
                        data: values,
                        borderColor: '#2E545D',
                        backgroundColor: 'rgba(46, 84, 93, 0.2)',
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error('Error fetching trend data:', error));

    // Bar Chart
    fetch('/api/raw-data')
        .then(response => response.json())
        .then(data => {
            // Process data as needed
            var labels = data.map(item => item.Product); // Adjust based on your CSV structure
            var values = data.map(item => item.Sales); // Adjust based on your CSV structure

            var ctxBar = document.getElementById('barChart').getContext('2d');
            var barChart = new Chart(ctxBar, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Sales',
                        data: values,
                        backgroundColor: ['#3498DB', '#2ECC71', '#E74C3C']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error('Error fetching bar data:', error));

    // Initialize Slick Carousel (if you have a testimonials section)
    /*
    $('.your-carousel').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        arrows: true,
        dots: true
    });
    */
});
