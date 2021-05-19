function ready() {

    function formEnable() {
        document.getElementById("fieldsetProfile").removeAttribute("disabled");
        document.getElementById("editProfileBtn").classList.add("visually-hidden");
        document.getElementById("updateProfileBtn").classList.remove("visually-hidden");
    }
    
    document.getElementById("editProfileBtn").addEventListener("click", formEnable);

}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", ready());
} else {
    ready();
}