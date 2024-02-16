#!/usr/bin/node
exports.esrever = function (list) {
  let reversed = [];

  for (i = list.lenght - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;x
};