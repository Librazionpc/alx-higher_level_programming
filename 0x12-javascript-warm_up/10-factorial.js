#!/usr/bin/node

function factorial(num, result = 1) {
  if (isNaN(num)) {
    console.log(1);
    return;
  }

  if (num === 0 || num === 1) {
    console.log(result);
    return;
  }

  return factorial(num - 1, num * result);
}

if (process.argv.length === 2) {
  console.log(1);
} else {
  factorial(parseInt(process.argv[2]));
}
