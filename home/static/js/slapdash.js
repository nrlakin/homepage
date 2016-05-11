var runner;
var runners;

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
  if (field.state==="pre_race") message = "tap to join";
  else if (field.state === "racing") message = "go!"
  textSize(32);
  textAlign(CENTER);
  text(message, windowWidth/2, y);
  y += 20;
  for (var i=0; i<n_runners; i++) {
    name = runners[i].name;
    position = runners[i].pos;
    image(runner, (finish/100)*position, y, dWidth=80, dHeight=80);
    y += 100;
    // console.log(runners[i]);
  }
  httpGet('/slapdash/update', datatype="json", callback=updateField);
}

function preload() {
  runner = loadImage('/static/img/runner.png');
}

// function onUpdate(update) {
//   var runners =
// }

function setup() {
  createCanvas(windowWidth, windowHeight);
  // image(runner, 0, 0, dWidth=80, dHeight=80);
  // image(runner, 0, 100, dWidth=80, dHeight=80);
  // image(runner, 0, 200, dWidth=80, dHeight=80);
  httpGet('/slapdash/update', datatype="json", callback=updateField);
}

function draw() {


}

function sendInit(e) {
  e.preventDefault();
  $.post('/slapdash/init');
}

function sendStart(e) {
  e.preventDefault();
  $.post('/slapdash/start');
}
