var myDropzone = new Dropzone("#kt_dropzonejs_example_1", {
    url: "/", // Set the url for your upload script location
    paramName: "file", // The name that will be used to transfer the file
    maxFiles: 1,
    maxFilesize: 3, // MB
    addRemoveLinks: true,
    acceptedFiles: 'image/*',
    accept: function(file, done) {
        if (file.name == "wow.jpg") {
            done("Naha, you don't.");
        } else {
            done();
        }
    }
});