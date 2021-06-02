var myWidget = cloudinary.createUploadWidget({
    cloudName: 'dwrholwaj',
    uploadPreset: 'clt3gdsi',
    folder: 'wildlife',
    cropping: true
  }, (error, result) => {
    if (!error && result && result.event === "success") {
      console.log(result.info.url);
      document.getElementById("image").value = result.info.url;
      document.getElementById("img-thumbnail").src = result.info.url;
      console.log(document.getElementById("image").value);
    }
  })

  document.getElementById("upload_widget").addEventListener("click", function() {
    myWidget.open();
  }, false);