function solution(A) {
  function T(value) {
    this._value = value;
  }
  T.prototype.value = function () {
    return this._value;
  };
  const a = A.map((item) => {
    return new T(item);
  });
  return a
}