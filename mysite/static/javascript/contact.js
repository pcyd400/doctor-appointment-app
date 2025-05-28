// Initialize EmailJS
(function () {
    emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your EmailJS public key
})();

document.getElementById("contact-form").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission

    // Collect form data
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    // Validate inputs
    if (!name || !email || !message) {
        alert("Please fill in all fields.");
        return;
    }

    // Send email using EmailJS
    emailjs
        .send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {
            from_name: name,
            from_email: email,
            message: message,
        })
        .then(
            () => {
                // Show success modal
                const modal = document.getElementById("success-modal");
                modal.classList.add("is-active");

                // Clear form
                document.getElementById("contact-form").reset();
            },
            (error) => {
                alert("Failed to send the message. Please try again later.");
                console.error("EmailJS Error:", error);
            }
        );
});

// Close modal
document.getElementById("close-modal").addEventListener("click", function () {
    const modal = document.getElementById("success-modal");
    modal.classList.remove("is-active");
});
