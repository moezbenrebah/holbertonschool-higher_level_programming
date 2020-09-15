#!/usr/bin/node

const size = process.argv[2];

if (isNaN(parseInt(size, 10))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
