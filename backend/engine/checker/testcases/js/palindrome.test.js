const palindrome = require('./submit').palindrome;

function main() {
  const examples = {
    test_1: { input: "hello", expected: false },
    test_2: { input: "racecar", expected: true },
    test_3: { input: "0_0 (: /-\\ :) 0–0", expected: true },
    test_4: { input: 1, expected: 'TypeError: Input must be a string' }
  };
  const res = {};

  try {
    const test_1 = palindrome(examples.test_1.input);
    if (test_1 === examples.test_1.expected) {
      res["test_1"] = {
        status: 'OK',
        input: examples.test_1.input,
        expected: examples.test_1.expected,
        got: test_1
      };
    } else {
      res["test_1"] = {
        status: 'Error',
        input: examples.test_1.input,
        expected: examples.test_1.expected,
        got: test_1
      };
    }
  } catch (error) {
    res["test_1"] = {
      status: 'Error',
      input: examples.test_1.input,
      expected: examples.test_1.expected,
      got: error.message
    };
  }

  try {
    const test_2 = palindrome(examples.test_2.input);
    if (test_2 === examples.test_2.expected) {
      res["test_2"] = {
        status: 'OK',
        input: examples.test_2.input,
        expected: examples.test_2.expected,
        got: test_2
      };
    } else {
      res["test_2"] = {
        status: 'Error',
        input: examples.test_2.input,
        expected: examples.test_2.expected,
        got: test_2
      };
    }
  } catch (error) {
    res["test_2"] = {
      status: 'Error',
      input: examples.test_2.input,
      expected: examples.test_2.expected,
      got: error.message
    };
  }

  try {
    const test_3 = palindrome(examples.test_3.input);
    if (test_3 === examples.test_3.expected) {
      res["test_3"] = {
        status: 'OK',
        input: examples.test_3.input,
        expected: examples.test_3.expected,
        got: test_3
      };
    } else {
      res["test_3"] = {
        status: 'Error',
        input: examples.test_3.input,
        expected: examples.test_3.expected,
        got: test_3
      };
    }
  } catch (error) {
    res["test_3"] = {
      status: 'Error',
      input: examples.test_3.input,
      expected: examples.test_3.expected,
      got: error.message
    };
  }

  try {
    const test_4 = palindrome(examples.test_4.input);
  } catch (error) {
    switch (true) {
      case error instanceof TypeError:
        res.test_4 = {
          status: 'OK',
          input: examples.test_4.input,
          expected: examples.test_4.expected,
          got: error.toString(),
        };
        break;
      default:
        res.test_4 = {
          status: 'Error',
          input: examples.test_4.input,
          expected: examples.test_4.expected,
          got: error.toString(),
        };
    }
  }

  return res;
}

console.log(main());
