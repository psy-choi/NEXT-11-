const play = (e) => {
  console.log(e);
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);

  if (audio) {
    audio.play();
    key.classList.add("play");
  }
};

const pause = (e) => {
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);

  if (audio) {
    audio.currentTime = 0;
    audio.pause();
    key.classList.remove("play");
  }
};

window.addEventListener("keydown", play);
window.addEventListener("keyup", pause);
