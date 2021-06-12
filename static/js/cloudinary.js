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
  });
  // the event listener is on the upload image button on the view case page
  // it opens a widget from Cloudinary 
  document.getElementById("upload_widget").addEventListener("click", function() {
    myWidget.open();
  }, false);