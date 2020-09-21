#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let i = 0, j = list.length; i < j; i++) {
    if (list[i] === searchElement) counter++;
  } return counter;
};
