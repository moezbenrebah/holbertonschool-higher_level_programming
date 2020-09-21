#!/usr/bin/node

exports.converter = function (base) {
  function nConverter (n) {
    return n.toString(base);
  }
  return nConverter;
};
