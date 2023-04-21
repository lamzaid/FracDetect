const img = document.querySelector('#img')

function loadImage(e) {
    const file = e.target.files[0]
 
    if (!isFileImage(file)) {
        console.log('Please select an image')
        return;
    }
    console.log("done")
    const reader = new FileReader();
    reader.onload = function() {
        const dataURL = reader.result;
        const imgElement = document.getElementById("preview-img");
        imgElement.src = dataURL;
        imgElement.style.display = "block";
    };
    reader.readAsDataURL(file);
}


function isFileImage(file) {
    const acceptedImageTypes = ['image/gif', 'image/png', 'image/jpeg']
    return file && acceptedImageTypes.includes(file['type'])

}

img.addEventListener('change', loadImage)