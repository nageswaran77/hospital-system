document.addEventListener('DOMContentLoaded', function() {
    // Password toggle visibility
    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');
    
    if (togglePassword && password) {
        togglePassword.addEventListener('click', function (e) {
            const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
            password.setAttribute('type', type);
            this.classList.toggle('fa-eye-slash');
            this.classList.toggle('fa-eye');
        });
    }

    // Auto close alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Date validation for appointment
    const dateInput = document.querySelector('#appointment_date');
    if (dateInput) {
        const dtToday = new Date();
        let month = dtToday.getMonth() + 1;
        let day = dtToday.getDate();
        let year = dtToday.getFullYear();
        if(month < 10)
            month = '0' + month.toString();
        if(day < 10)
            day = '0' + day.toString();
        
        const minDate = year + '-' + month + '-' + day;
        dateInput.setAttribute('min', minDate);
    }

    // Color toggle - click to change white to blue
    const colorToggleElements = document.querySelectorAll('.color-toggle');
    colorToggleElements.forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.toggle('active');
        });
    });
});
