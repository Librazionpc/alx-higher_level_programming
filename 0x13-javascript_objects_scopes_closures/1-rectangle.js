#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && parseInt(h)) {
      this.width = w;
      this.height = h;
    }
  }
};
