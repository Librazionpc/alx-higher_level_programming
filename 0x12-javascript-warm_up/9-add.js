#!/usr/bin/node
const add = (num1, num2) => {
  if (num1 && num2) {
    console.log(num1 + num2);
  } else {
    console.log('NaN');
  }
};

if (process.argv.length === 2) {
  console.log('NaN');
} else if (process.argv.length === 3) {
  console.log('NaN');
} else {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
