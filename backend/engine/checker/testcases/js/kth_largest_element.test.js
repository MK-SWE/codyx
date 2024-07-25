const kthLargestElement = require('./submit').kthLargestElement;

function main() {
  const examples = {
    test_1: { input: [[3, 2, 1, 5, 6, 4], 2], expected: 5 },
    test_2: { input: [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], expected: 4 },
    test_3: { input: [[-1, 2, 0], 1], expected: 2 },
    test_4: { input: [[], 5], expected: 0 }
  };
  const res = {};
  Object.keys(examples).forEach(test => {
    try {
      const result = kthLargestElement(...examples[test].input);
      if (result === examples[test].expected) {
        res[test] = {
          status: 'OK',
          input: examples[test].input[0],
          expected: examples[test].expected,
          got: result,
        };
      } else {
        res[test] = {
          status: 'Error',
          input: examples[test].input[0],
          expected: examples[test].expected,
          got: result,
        };
      }
    } catch (error) {
      res[test] = {
        status: 'Error',
        input: examples[test].input[0],
        expected: examples[test].expected,
        got: error.toString(),
      };
    }
  });
  return res;
}
console.log(main());
