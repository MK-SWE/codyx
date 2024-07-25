const reverseString = require('./submit').reverseString;

function main() {
  const examples = {
    test_1: { input: 'hello', expected: 'olleh' },
    test_2: { input: 'world', expected: 'dlrow' },
    test_3: { input: -1, expected: 'TypeError: Input must be a string' },
    test_4: { input: 'racecar', expected: 'racecar' },
  };
  const res = {};

  try {
    const test_1 = reverseString(examples.test_1.input);
    if (test_1 === examples.test_1.expected) {
      res.test_1 = {
        status: 'OK',
        input: examples.test_1.input,
        expected: examples.test_1.expected,
        got: test_1,
      };
    } else {
      res.test_1 = {
        status: 'Error',
        input: examples.test_1.input,
        expected: examples.test_1.expected,
        got: test_1,
      };
    }
  } catch (error) {
    res.test_1 = {
      status: 'Error',
      input: examples.test_1.input,
      expected: examples.test_1.expected,
      got: error.toString(),
    };
  }

  try {
    const test_2 = reverseString(examples.test_2.input);
    if (test_2 === examples.test_2.expected) {
      res.test_2 = {
        status: 'OK',
        input: examples.test_2.input,
        expected: examples.test_2.expected,
        got: test_2,
      };
    } else {
      res.test_2 = {
        status: 'Error',
        input: examples.test_2.input,
        expected: examples.test_2.expected,
        got: test_2,
      };
    }
  } catch (error) {
    res.test_2 = {
      status: 'Error',
      input: examples.test_2.input,
      expected: examples.test_2.expected,
      got: error.toString(),
    };
  }

  try {
    const test_3 = reverseString(examples.test_3.input);
  } catch (error) {
    switch (true) {
      case error instanceof TypeError:
        res.test_3 = {
          status: 'OK',
          input: examples.test_3.input,
          expected: examples.test_3.expected,
          got: error.toString(),
        };
        break;
      default:
        res.test_3 = {
          status: 'Error',
          input: examples.test_3.input,
          expected: examples.test_3.expected,
          got: error.toString(),
        };
    }
  }


  try {
    const test_4 = reverseString(examples.test_4.input);
    if (test_4 === examples.test_4.expected) {
      res.test_4 = {
        status: 'OK',
        input: examples.test_4.input,
        expected: examples.test_4.expected,
        got: test_4,
      };
    } else {
      res.test_4 = {
        status: 'Error',
        input: examples.test_4.input,
        expected: examples.test_4.expected,
        got: test_4,
      };
    }
  } catch (error) {
    res.test_4 = {
      status: 'Error',
      input: examples.test_4.input,
      expected: examples.test_4.expected,
      got: error.toString(),
    };
  }

  return res;
}

console.log(main());
