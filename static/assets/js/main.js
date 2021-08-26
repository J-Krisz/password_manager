//display modals on clicking

const modalWrapper = document.querySelector(".modals_wrapper");
if (modalWrapper) {
    function displayModal(id) {
        const modal = document.getElementById(id);
        modalWrapper.style.display = "flex";
        modal.style.display = "flex";
        
        //close modal 
        const close = document.getElementById("close_modal");
        close.addEventListener("click", () => {
            modalWrapper.style.display = "none";
            modal.style.display = "none";
        })
    }
}

//copy to clipboard

const copies = document.querySelectorAll(".copy");
copies.forEach(copy => {
    copy.onclick = () => {
        let elementToCopy = copy.previousElementSibling;
        elementToCopy.select();
        document.execCommand("copy");
    }
})


//display actions on mobile devices

const actions = document.querySelectorAll(".actions");
if (actions) {
    actions.forEach(action => {
        action.onclick = () => {
            const links = action.querySelectorAll("a");
            links.forEach(link = () => {
                link.style.display = "none";
            })
            setTimeout(function() {
                links.forEach(link => {
                    link.style.display = "none";
                })
            }, 6000)
        }
    })
}