#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const secarr = arr.sort(function (a, b) { return b - a; })[1];
  console.log(secarr);
}
