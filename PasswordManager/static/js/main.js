// Password visibility toggle

const passwordInput = document.getElementById('id_password');
const eyeToggleBtn = document.getElementById('eye');

// function to toggle input field
function togglePasswordVisible() {

    if (passwordInput.type === 'password') {
        eyeToggleBtn.classList = 'fas fa-eye-slash';
        passwordInput.type = 'text';
    } else {
        eyeToggleBtn.classList = 'fas fa-eye';
        passwordInput.type = 'password';
    };
}

// toggle fa-eye icon
eyeToggleBtn.addEventListener('click', () => {
    togglePasswordVisible();
    passwordInput.focus();
})



// Copy Credentials To Clipboard
const copyData = [...document.getElementsByClassName('to-clp')];

copyData.forEach(btn => btn.addEventListener('click', () => {
    const data = btn.getAttribute('data');
    navigator.clipboard.writeText(data);

    navigator.clipboard.readText().then(clipText => {
        console.log(clipText);
        btn.textContent = 'copied';
    })

    if (previous) {
        previous.textContent = 'click';
    }
    previous = bth;
}));


// TODO: add notification saying data was copied
// TODO: remove content form clipboard after 30 seconds
