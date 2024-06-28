
global RNG_M
global RNG_A
global RNG_C
global RNG_STATE
def setSeed(seed):
  global RNG_M
  global RNG_A
  global RNG_C
  RNG_M = 0x80000000
  RNG_A = 1103515245
  RNG.C = 12345
  RNG_STATE = seed

def nextInt():
  global RNG_M
  global RNG_A
  global RNG_C
  RNG_STATE = (RNG_A * RNG_STATE + RNG_C) % RNG_M
  return RNG_STATE

"""
RNG.prototype.nextInt = function() {
  this.state = (this.a * this.state + this.c) % this.m;
  return this.state;
}
RNG.prototype.nextFloat = function() {
  // returns in range [0,1]
  return this.nextInt() / (this.m - 1);
}
RNG.prototype.nextRange = function(start, end) {
  // returns in range [start, end): including start, excluding end
  // can't modulu nextInt because of weak randomness in lower bits
  var rangeSize = end - start;
  var randomUnder1 = this.nextInt() / this.m;
  return start + Math.floor(randomUnder1 * rangeSize);
}
RNG.prototype.choice = function(array) {
  return array[this.nextRange(0, array.length)];
}
"""