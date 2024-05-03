document.addEventListener('DOMContentLoaded', function() {
    const confirmationMessage = document.getElementById('confirmation-message');
    if (confirmationMessage) {
        confirmationMessage.style.display = 'block';
        setTimeout(function() {
            document.getElementById("confirmation-message").style.display = "none";
          }, 5000);
    }
});

