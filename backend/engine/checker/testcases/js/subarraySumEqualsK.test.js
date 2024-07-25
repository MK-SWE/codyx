const subarraySumEqualsK = require('./submit').subarraySumEqualsK;

function main() {
  const examples = {
    test_1: { input: [[1, 1, 1], 2], expected: 2 },
    test_2: { input: [[1, 2, 3], 3], expected: 2 },
    test_3: { input: [[1, -1, 0], 0], expected: 3 },
    test_4: { input: [[], 5], expected: 0 },
  };
  const res = {};

  try {
    const test_1 = subarraySumEqualsK(examples.test_1.input[0], examples.test_1.input[1]);
    if (test_1 === examples.test_1.expected) {
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
    const test_2 = subarraySumEqualsK(examples.test_2.input[0], examples.test_2.input[1]);
    if (test_2 === examples.test_2.expected) {
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
    const test_3 = subarraySumEqualsK(examples.test_3.input[0], examples.test_3.input[1]);
    if (test_3 === examples.test_3.expected) {
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

  try {
    const test_4 = subarraySumEqualsK(examples.test_4.input[0], examples.test_4.input[1]);
    if (test_4 === examples.test_4.expected) {
      res.test_4 = {
        status: 'OK',
        input: examples.test_4.input[0],
        expected: examples.test_4.expected,
        got: test_4,
      };
    } else {
      res.test_4 = {
        status: 'Error',
        input: examples.test_4.input[0],
        expected: examples.test_4.expected,
        got: test_4,
      };
    }
  } catch (error) {
    res.test_4 = {
      status: 'Error',
      input: examples.test_4.input[0],
      expected: examples.test_4.expected,
      got: error.toString(),
    };
  }

  return res;
}

console.log(main());