
var allMethods = document.getElementsByClassName("methods");

var commands = {};

for (var i = 0; i < allMethods.length; i++){
  commands[ allMethods[i].id ] = allMethods[i].innerHTML;
}

function makeGetInput(id){
  return function(){
    return document.getElementById(id);
  };
}

function createContent(output){
  var div_out = document.createElement("div")
  for (var i=0; i < output.length; i++){
    var p = document.createElement("p")
    var text = document.createTextNode(output[i]);
    p.appendChild(text);
    div_out.appendChild(p);
  }
  return div_out;
}

function createError(out){
  var d = document.createElement("div")
  var p1 = document.createElement("p")
  var line1 = document.createTextNode("Traceback (most recent call last):");
  p1.appendChild(line1);
  var p2 = document.createElement("p")
  var line2 = document.createTextNode("File \"<stdin>\", line 1, in <module>");
  p2.appendChild(line2);
  var p3 = document.createElement("p")
  var line3 = document.createTextNode("AttributeError: \'MySelf\' object has no attribute '" + out.method +"'");
  p3.appendChild(line3);
  d.appendChild(p1);
  d.appendChild(p2);
  d.appendChild(p3);
  return d;
}

function makeAddOutput(id, f){
  return function(output){
    var out = document.getElementById(id);
    var content = f(output);
    out.appendChild(content);
  };
}

function analyze(input){
  var output = {};
  output.result = commands[input];
  output.method = input;
  return output;
}

var writeInput = makeAddOutput("out", function(a){
                   var div_out = document.createElement("div");
                   div_out.innerHTML = a;
                   return div_out;});

var addOutput = makeAddOutput("out", function(a){
                  var div_out = document.createElement("div");
                  div_out.innerHTML = a;
                  return div_out;});

var commandError = makeAddOutput("out", createError)

var getInput = makeGetInput("in")

function resetInput(){
  var inputBox = getInput();
  inputBox.value = '';
}

function onInput(e) {
  if (e.keyCode == 13){
    var inputBox = getInput();
    var output = analyze(inputBox.value);
    writeInput(">>> siscia." + inputBox.value);
    if (output.result != undefined){
      addOutput(output.result);
    }
    else if (analyze(inputBox.value + "()").result != undefined){
      output = analyze(inputBox.value + "()");
      addOutput(output.result);
    }
    else {
      commandError(output);
    }
    resetInput();
    inputBox.focus();
    inputBox.scrollIntoView();
  }
}

(function(){

  var allMethods = document.getElementsByClassName("methods");

  var commands = {};
  var dir_output = "["

  for (var i = 0; i < allMethods.length; i++){
    commands[ allMethods[i].id ] = allMethods[i].innerHTML;
    dir_output += "'" + allMethods[i].id.slice(0, -2) + "', "
  }

  dir_output = dir_output.slice(0, -2) + "]";

  document.getElementById("methods-list").innerHTML = dir_output;


  document.getElementById("in").focus();

})();