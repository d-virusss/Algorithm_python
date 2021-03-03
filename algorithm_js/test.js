class Person{
  constructor(name){
    this._name = name;
  }
}

{
  class Person{
    constructor(name){
      console.log('qwer');
      this._name = name;
    }
  }
  const a = new Person('hah');
  console.log(a._name)
}