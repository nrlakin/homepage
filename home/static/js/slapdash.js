var runner;

function preload() {
  runner = loadImage('/static/img/runner.png');
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  image(runner, 0, 0, dWidth=80, dHeight=80);
  image(runner, 0, 100, dWidth=80, dHeight=80);
  image(runner, 0, 200, dWidth=80, dHeight=80);
}

function draw() {
  
}
