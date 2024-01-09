#!/usr/bin/node
exports.esrever = function (list) {
  let rev = list.length - 1;
  let m = 0;
  while ((rev - m) > 0) {
    const tmp = list[rev];
    list[rev] = list[m];
    list[m] = tmp;
    m++;
    rev--;
  }
  return (list);
};
