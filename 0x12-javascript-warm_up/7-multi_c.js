#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  if (x) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
