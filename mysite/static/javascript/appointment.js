window.onload = function() {
    // Holiday Modal elements
    const holidayModal = document.getElementById('holidayModal');
    const closeModalButton = document.getElementById('closeModal');
    
    // Set holidays (add more if needed)
    const holidays = ["2024-12-28"]; // Example: Christmas day

    // Get today's date in the format YYYY-MM-DD
    const today = new Date().toISOString().split('T')[0]; // "2024-12-25"

    // Check if today is a holiday
    if (holidays.includes(today)) {
        holidayModal.classList.add('is-active'); // Show the holiday modal
    }

    // Close modal event
    closeModalButton.addEventListener('click', function() {
        holidayModal.classList.remove('is-active'); // Hide the modal
    });

    let dateInput = document.getElementById('appointment_date');
    let timeInput = document.getElementById('appointment_time');
    let form = document.querySelector('form');
    let nameInput = document.querySelector('[name="patient_name"]');
    let phoneInput = document.querySelector('[name="contact_number"]');

    // Event listener to restrict weekends for the date picker
    dateInput.addEventListener('input', function(event) {
        let selectedDate = new Date(event.target.value);
        let day = selectedDate.getDay();

        // Check if the selected day is Saturday (6) or Sunday (0)
        if (day === 6 || day === 0) {
            alert("Please select a weekday (Monday to Friday). Saturdays and Sundays are not available.");
            event.target.value = ''; // Clear the date input
        }
    });

    // Event listener to restrict time between 10:00 AM and 5:00 PM
    timeInput.addEventListener('input', function(event) {
        let selectedTime = event.target.value;
        let [hour, minute] = selectedTime.split(':').map(Number);

        // Ensure time is between 10:00 AM (10:00) and 5:00 PM (17:00)
        if (hour < 10 || hour >= 17) {
            alert("Please select a time between 10:00 AM and 5:00 PM.");
            event.target.value = ''; // Clear the time input
        }
    });

    // Form validation
    form.addEventListener('submit', function(event) {
        // Validate Name (can't be empty)
        if (nameInput.value.trim() === "") {
            alert("Please enter your full name.");
            event.preventDefault();  // Prevent form submission
            return;
        }

        // Validate Phone Number (must be 10 digits)
        let phoneNumber = phoneInput.value.trim();
        let phonePattern = /^[0-9]{10}$/;  // RegEx for 10 digits
        if (!phonePattern.test(phoneNumber)) {
            alert("Please enter a valid 10-digit phone number.");
            event.preventDefault();  // Prevent form submission
            return;
        }
    });
};
