#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    if (!c) {
        this.print()
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
module.exports = { Rectangle, Square };