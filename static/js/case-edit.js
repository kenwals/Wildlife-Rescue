function ready() {
    /**
    * this enables the form for updating, 
    * Edit button is hidden
    * Edit case, Delete case and upload image buttons are made visible,
    * the heading is changed to reflect the view is an edit case view
    */
    function formEnable() {
        document.getElementById("fieldset1").removeAttribute("disabled");
        document.getElementById("fieldset2").removeAttribute("disabled");
        document.getElementById("editCaseBtn").classList.add("visually-hidden");
        document.getElementById("saveCaseBtn").classList.remove("visually-hidden");
        document.getElementById("deleteCaseBtn").classList.remove("visually-hidden");
        document.getElementById("upload_widget").classList.remove("visually-hidden");
        document.getElementById("heading-case-view-page").innerText = "Edit Case";
      }
    
    // the event listener is on the Edit case button on the view case page
    document.getElementById("editCaseBtn").addEventListener("click", formEnable);

}

/**
 * This waits for document to be fully loaded
 * then runs the ready() function when loading is completed
 */
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", ready());
} else {
    ready();
}