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
