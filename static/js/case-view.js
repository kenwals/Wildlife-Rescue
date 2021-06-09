function ready() {
    function formatDate(date) {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) month = '0' + month;
        if (day.length < 2) day = '0' + day;

        return [year, month, day].join('-');
    }

    let today = new Date();

    document.getElementById("date").max = formatDate(today);


    let autocomplete;

    function initAutocomplete() {
        autocomplete = new google.maps.places.Autocomplete(
            document.getElementById("location"), {
                componentRestrictions: {
                    "country": ["IE"]
                },
                fields: ["place_id", "geometry", "name"]
            });
        autocomplete.addListener("place_changed", onPlaceChanged);
    }

    function onPlaceChanged() {
        var place = autocomplete.getPlace();

        if (!place.geometry) {
            // User did not select a prediction; reset the input field
            document.getElementById("location").placeholder = "Enter a Place";
        }
    }


    var myWidget = cloudinary.createUploadWidget({
        cloudName: 'dwrholwaj',
        uploadPreset: 'clt3gdsi',
        folder: 'wildlife',
        cropping: true
    }, (error, result) => {
        if (!error && result && result.event === "success") {
            document.getElementById("image").value = result.info.url;
            document.getElementById("img-thumbnail").src = result.info.url;
        }
    })
    // the event listener is on the upload image button on the view case page
    // it opens a widget from Cloudinary 
    document.getElementById("upload_widget").addEventListener("click", function () {
        myWidget.open();
    }, false);


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