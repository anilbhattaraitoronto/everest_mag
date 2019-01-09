var slideIndex = 1;
var videoIndex = 1;
showVideos(videoIndex);
showSlides(slideIndex);



// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}
function plusVideos(n) {
    showVideos(videoIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}
function currentVideo(n) {
    showVideos(videoIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("gallery-image");
    var dots = document.getElementsByClassName("slide-indicator");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

function showVideos(n) {
    var i;
    var videos = document.getElementsByClassName('video-items');
    var videoDots = document.getElementsByClassName('video-indicator');
    if (n > videos.length) {
        videoIndex = 1;
    }
    if (n < 1) {
        videoIndex = videos.length;
    }
    for (i = 0; i < videos.length; i++) {
        videos[i].style.display = 'none';
    }
    for (i = 0; i < videoDots.length; i++) {
        videoDots[i].className = videoDots[i].className.replace(" active-video", "");
    }
    videos[videoIndex - 1].style.display = 'block';
    videoDots[videoIndex - 1].className += " active-video";
}
