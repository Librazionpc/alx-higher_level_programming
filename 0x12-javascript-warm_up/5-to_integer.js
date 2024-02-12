#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Not a number');
} else {
  const number = parseInt(process.argv[2]);
  if (number) {
    console.log('My number :', number);
  } else {
    console.log('Not a number');
  }
}
