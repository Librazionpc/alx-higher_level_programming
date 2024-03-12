#!/usr/bin/node

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) {
        let square = '';
        for (let i = 0; i < this.width; i++) {
          square += c;
        }
        console.log(square);
      }
    }
  }
}
module.exports = { Square };
