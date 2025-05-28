// Function to animate progress bars
function setProgress(elementId, percentage) {
    const progressElement = document.getElementById(elementId);
    progressElement.style.setProperty("--progress", percentage);
}

// values for progress
setProgress("patientsTreated", 80); // 75% patients treated
setProgress("emergencyResponses", 90); // 50% emergency responses
setProgress("doctorRating", 90); // 90% doctor rating
