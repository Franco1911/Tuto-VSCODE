class Video{
    constructor(selector){
        this.selector = selector;
        this.playerElement = document.querySelector(selector);
        this.videoElement = document.querySelector(selector+"video");

        this.bindEvents();
    }

    bindEvents(){
        this.playPauseBTN = document.querySelector(this.selector +" .play.pause");
        this.playPauseBTN.addEventListener('click', ()=>this.playPause())
    }

    playPause(){
        if(this.videoElement.paused){
            this.videoElement.play();
            this.playPauseBTN.innerHTML = "pause";
        }else{
            this.videoElement.pause();
            this.playPauseBTN.innerHTML = "play_arrow";
        }
    }
}