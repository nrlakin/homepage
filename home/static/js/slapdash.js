var runner_image;
var finish_image;
var runners;
var finishers;
var race_length;

function updateField(result) {
  var y = 50;
  var finish = windowWidth - 80;
  var message = "";
  // field = JSON.parse(result)
  field = result;
  state = field.state;
  runners = field.runners;
  n_runners = runners.length;
  background(255);
  image(finish_image, finish-20, y);
  // image(finish, 0,0);
  if (field.state==="pre_race") message = "tap to join";
  else if (field.state === "racing") message = "go!"
  textSize(32);
  textAlign(CENTER);
  text(message, windowWidth/2, y);
  textSize(16);
  y += 20;
  for (var i=0; i<finishers.length; i++) {
    text((i+1) + ".) " + finishers[i], i*80, y, dWidth=80);
  }
  for (var i=0; i<n_runners; i++) {
    name = runners[i].name;
    position = runners[i].pos;
    image(runner_image, (finish/race_length)*position, y, dWidth=80, dHeight=80);
    y += 95;
    textSize(16);
    text(name, (finish/race_length)*position, y, dWidth=80);
    y += 20;
    if (int(position) == race_length) {
      if (finishers.indexOf(runners[i].name) == -1) {
        finishers.push(runners[i].name);
      }
    }
    // console.log(runners[i]);
  }
  httpGet('/slapdash/update', datatype="json", callback=updateField);
}

function preload() {
  runner_image = loadImage('/static/img/runner.png');
  finish_image = loadImage('/static/img/checkerboard-pattern.jpg');
}

// function onUpdate(update) {
//   var runners =
// }

function setup() {
  createCanvas(windowWidth, windowHeight);
  // image(runner, 0, 0, dWidth=80, dHeight=80);
  // image(runner, 0, 100, dWidth=80, dHeight=80);
  // image(runner, 0, 200, dWidth=80, dHeight=80);
  finishers = [];
  race_length = 60;
  httpGet('/slapdash/update', datatype="json", callback=updateField);
}

function draw() {


}

function sendInit(e) {
  e.preventDefault();
  finishers = [];
  $.post('/slapdash/init');
}

function sendStart(e) {
  e.preventDefault();
  $.post('/slapdash/start');
}
