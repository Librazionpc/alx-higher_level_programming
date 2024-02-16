#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && parseInt(h)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;