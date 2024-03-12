#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
    console.log('Usage: ./102-concat.js <file1> <file2> <destination>');
    process.exit(1);
}

const filePath1 = process.argv[2];
const filePath2 = process.argv[3];
const destinationPath = process.argv[4];

fs.readFile(filePath1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1Path}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(filePath2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file1Path}: ${err.message}`);
      process.exit(1);
    }
    const concatenated_string = data1 + data2;

    fs.writeFile(destinationPath, concatenated_string, 'utf8', err => {
      if (err) {
        console.error(`Error writing to ${destinationPath}: ${err.message}`);
        process.exit(1);
      }
      console.log(destinationPath);
    });
  });    
});