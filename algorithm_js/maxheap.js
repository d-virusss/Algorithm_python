class Queue {
  data = [];

  enQueue = (data) => {
    this.data.push(data);
  };

  deQueue = () => {
    return this.data.shift();
  };
}

class PriorityQueue extends Queue {
  swap = (a, b) => {
    const temp = this.data[a];
    this.data[a] = this.data[b];
    this.data[b] = temp;
  };

  compareBottomUp = (data, index) => {
    const parentIndex = Math.floor((index - 1) / 2);
    if (this.data[parentIndex] < data) {
      this.swap(index, parentIndex);
      this.compareBottomUp(data, parentIndex);
    }
  };

  enQueue = (data) => {
    this.data.push(data);
    this.compareBottomUp(data, this.data.length - 1);
  };

  compareTopDown = (data, index) => {
    const childIndexBase = index * 2;
    let target = childIndexBase + 1;
    if (this.data[childIndexBase + 1] < this.data[childIndexBase + 2]) {
      target += 1;
    }
    if (this.data[target] > data) {
      this.swap(target, index);
      this.compareTopDown(data, target);
    }
  };

  deQueue = () => {
    const result = this.data[0] || false;
    const data = this.data.pop();
    if(this.data.length !== 0) this.data[0] = data;
    this.compareTopDown(data, 0);
    return result;
  };
}