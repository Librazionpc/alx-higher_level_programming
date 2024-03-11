#!/usr/bin/node
function factorial (num) {
  let answer = 1;
  if (num) {
    for (let i = num; i > 0; i--) {
      answer *= i;
    }
  } else {
    console.log('NaN');
  }
  console.log(answer);
}

if (process.argv.length === 2) {
  console.log(1);
} else {
  factorial(parseInt(process.argv[2]));
}
