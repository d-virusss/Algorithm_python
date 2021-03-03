var Foo = (function(){
  function a(name){
    this._name = name;
  }

  a.prototype.say = function(){
    console.log('hi ' + this._name);
    return this._name;
  }

  return a;
}());

class Qoo{
  constructor(name){
    this._name = name;
  }
  say(){
    console.log('hi '+ this._name)
  }
}

var ins = new Foo('qwer');
console.log(ins);

