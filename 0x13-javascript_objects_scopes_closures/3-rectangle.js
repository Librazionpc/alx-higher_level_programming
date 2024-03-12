#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && parseInt(h)) {
      if (!(w <= 0 || h <= 0)) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let square = '';
      for (let i = 0; i < this.width; i++) {
        square += 'X';
      }
      console.log(square);
    }
  }
}

module.exports = Rectangle;
