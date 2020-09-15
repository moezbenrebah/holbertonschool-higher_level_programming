#!/usr/bin/node

const language = 'C is fun';

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(language);
}
