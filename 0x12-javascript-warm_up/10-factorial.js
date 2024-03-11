#!/usr/bin/node

function factorial (num) {
  if (isNaN(num)) {
    console.log(1);
    return;
  }

  if (num === 0) {
    console.log(1);
    return;
  }

  if (num === 1) {
    console.log(1);
    return 1;
  }

  const result = num * factorial(num - 1);
  console.log(result);
  return result;
}

if (process.argv.length === 2) {
  console.log(1);
} else {
  factorial(parseInt(process.argv[2]));
}
