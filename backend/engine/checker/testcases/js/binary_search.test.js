const binarySearch = require('./submit').binarySearch;

function main() {
  const examples = {
    test_1: { input: [[1, 2, 3, 4, 5], 3], expected: 2},
    test_2: { input: [[1, 2, 3, 4, 5], 6], expected: -1},
    test_3: { input: [[1, 3, 5, 7, 9], 5], expected: 2},
    test_4: { input: [[], 5], expected: -1}
  };
  const res = {};

  try {
    const [test_1_input, args] = examples.test_1.input;
    const test_1 = binarySearch(test_1_input, args);
    if (test_1 === examples.test_1.expected) {
      res.test_1 = {
        status: 'OK',
        input: test_1_input,
        expected: examples.test_1.expected,
        got: test_1
      };
    } else {
      res.test_1 = {
        status: 'Error',
        input: test_1_input,
        expected: examples.test_1.expected,
        got: test_1
      };
    }
  } catch (error) {
    res.test_1 = {
      status: 'Error',
      input: examples.test_1.input,
      expected: examples.test_1.expected,
      got: error.toString()
    };
  }

  try {
    const [test_2_input, args] = examples.test_2.input;
    const test_2 = binarySearch(test_2_input, args);
    if (test_2 === examples.test_2.expected) {
      res.test_2 = {
        status: 'OK',
        input: test_2_input,
        expected: examples.test_2.expected,
        got: test_2
      };
    } else {
      res.test_2 = {
        status: 'Error',
        input: test_2_input,
        expected: examples.test_2.expected,
        got: test_2
      };
    }
  } catch (error) {
    res.test_2 = {
      status: 'Error',
      input: examples.test_2.input,
      expected: examples.test_2.expected,
      got: error.toString()
    };
  }

  try {
    const [test_3_input, args] = examples.test_3.input;
    const test_3 = binarySearch(test_3_input, args);
    if (test_3 === examples.test_3.expected) {
      res.test_3 = {
        status: 'OK',
        input: test_3_input,
        expected: examples.test_3.expected,
        got: test_3
      };
    } else {
      res.test_3 = {
        status: 'Error',
        input: test_3_input,
        expected: examples.test_3.expected,
        got: test_3
      };
    }
  } catch (error) {
    res.test_3 = {
      status: 'Error',
      input: examples.test_3.input,
      expected: examples.test_3.expected,
      got: error.toString()
    };
  }

  try {
    const [test_4_input, args] = examples.test_4.input;
    const test_4 = binarySearch(test_4_input, args);
    if (test_4 === examples.test_4.expected) {
      res.test_4 = {
        status: 'OK',
        input: test_4_input,
        expected: examples.test_4.expected,
        got: test_4
      };
    } else {
      res.test_4 = {
        status: 'Error',
        input: test_4_input,
        expected: examples.test_4.expected,
        got: test_4
      };
    }
  } catch (error) {
    res.test_4 = {
      status: 'Error',
      input: examples.test_4.input,
      expected: examples.test_4.expected,
      got: error.toString()
    };
  }

  return res;
}

console.log(main());
