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


// TODO: add tootltip for copyin when howered and clicked
// TODO: remove content form clipboard after 30 seconds
