#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      let A = '';
      for (let i = 0; i < this.width; i++) {
        A += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(A);
      }
    }
  }
};

module.exports = Square;
