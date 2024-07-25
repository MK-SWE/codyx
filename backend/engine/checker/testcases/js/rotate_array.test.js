const rotateArray = require('./submit').rotateArray;

function main() {
  const examples = {
    test_1: { input: [[1, 2, 3, 4, 5], 2], expected: [4, 5, 1, 2, 3] },
    test_2: { input: [[1, 2, 3], 4], expected: [3, 1, 2] },
    test_3: { input: [[1, 2, 3, 4, 5, 6, 7], 3], expected: [5, 6, 7, 1, 2, 3, 4] },
  };
  const res = {};

  try {
    const test_1 = rotateArray(examples.test_1.input[0], examples.test_1.input[1]);
    const check = examples.test_1.expected.filter((el, i) => el !== test_1[i]);
    if (check.length === 0) {
      res.test_1 = {
        status: 'OK',
        input: examples.test_1.input[0],
        expected: examples.test_1.expected,
        got: test_1,
      };
    } else {
      res.test_1 = {
        status: 'Error',
        input: examples.test_1.input[0],
        expected: examples.test_1.expected,
        got: test_1,
      };
    }
  } catch (error) {
    res.test_1 = {
      status: 'Error',
      input: examples.test_1.input[0],
      expected: examples.test_1.expected,
      got: error.toString(),
    };
  }

  try {
    const test_2 = rotateArray(examples.test_2.input[0], examples.test_2.input[1]);
    const check = examples.test_2.expected.filter((el, i) => el !== test_2[i]);
    if (check.length === 0) {
      res.test_2 = {
        status: 'OK',
        input: examples.test_2.input[0],
        expected: examples.test_2.expected,
        got: test_2,
      };
    } else {
      res.test_2 = {
        status: 'Error',
        input: examples.test_2.input[0],
        expected: examples.test_2.expected,
        got: test_2,
      };
    }
  } catch (error) {
    res.test_2 = {
      status: 'Error',
      input: examples.test_2.input[0],
      expected: examples.test_2.expected,
      got: error.toString(),
    };
  }

  try {
    const test_3 = rotateArray(examples.test_3.input[0], examples.test_3.input[1]);
    const check = examples.test_3.expected.filter((el, i) => el !== test_3[i]);
    if (check.length === 0) {
      res.test_3 = {
        status: 'OK',
        input: examples.test_3.input[0],
        expected: examples.test_3.expected,
        got: test_3,
      };
    } else {
      res.test_3 = {
        status: 'Error',
        input: examples.test_3.input[0],
        expected: examples.test_3.expected,
        got: test_3,
      };
    }
  } catch (error) {
    res.test_3 = {
      status: 'Error',
      input: examples.test_3.input[0],
      expected: examples.test_3.expected,
      got: error.toString(),
    };
  }

  return res;
}

console.log(main());
