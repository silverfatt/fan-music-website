var audioPlayers = [...document.getElementsByClassName("audio-player")]
var players = [...document.getElementsByClassName("player")]
let progress = [...document.getElementsByClassName("progress")]
let playbtns = [...document.getElementsByClassName("playbtn")]

const onPauseHandler = (player) => {
    const playButton = player.querySelector('.fas')
    playButton.classList.add("fa-play");
    playButton.classList.remove("fa-pause");
}

const onPlayHandler = (player) => {
    const playButton = player.querySelector('.fas')
    playButton.classList.remove("fa-play");
    playButton.classList.add("fa-pause");
}

const onTimeUpdate = (player) => {
    const audioPlayer = player.querySelector('.audio-player')
    const current = player.querySelector('.current')
    const progress = player.querySelector('.progress')

    let ct = audioPlayer.currentTime;

    const duration = audioPlayer.duration;
    const prog = Math.floor((ct * 100) / duration);

    current.innerHTML = timeFormat(ct);
    progress.style.setProperty("--progress", prog + "%");
}


audioPlayers.forEach((audioPlayer) => {
    audioPlayer.onpause = () => onPauseHandler(audioPlayer.parentElement)
    audioPlayer.onplay = () => onPlayHandler(audioPlayer.parentElement)
    audioPlayer.ontimeupdate = () => onTimeUpdate(audioPlayer.parentElement)
})

const playButtonClickHandler = function (player) {
    if (player.paused) {
        audioPlayers.forEach((playerElement) => {
            playerElement.pause()
            playerElement.currentTime = 0
        })
        player.play()
        return
    }
    player.pause()
}

players.forEach((player) => {
    const playButton = player.querySelector('i.fas')
    const audioPlayer = playButton.parentElement.parentElement.querySelector('audio')
    playButton.addEventListener('click', () => {
        playButtonClickHandler(audioPlayer)
    })
})

function timeFormat(ct) {
    minutes = Math.floor(ct / 60);
    seconds = Math.floor(ct % 60);

    if (seconds < 10) {
        seconds = "0" + seconds;
    }

    return minutes + ":" + seconds;
}
