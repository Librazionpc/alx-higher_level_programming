#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  const num = number + 1;
  theFunction(num);
};

module.exports.addMeMaybe = addMeMaybe;
