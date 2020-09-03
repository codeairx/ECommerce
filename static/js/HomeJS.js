function changeImage(_src) {
    var imgDiv = document.getElementById('main-img');
    var imageElement = imgDiv.getElementsByTagName('img')[0];
    imageElement.src = _src;
}
