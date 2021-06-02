function ready() {

    function formEnable() {
        document.getElementById("fieldset1").removeAttribute("disabled");
        document.getElementById("fieldset2").removeAttribute("disabled");
        document.getElementById("editCaseBtn").classList.add("visually-hidden");
        document.getElementById("saveCaseBtn").classList.remove("visually-hidden");
        document.getElementById("deleteCaseBtn").classList.remove("visually-hidden");
        document.getElementById("upload_widget").classList.remove("visually-hidden");
      }
    
    document.getElementById("editCaseBtn").addEventListener("click", formEnable);

}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", ready());
} else {
    ready();
}