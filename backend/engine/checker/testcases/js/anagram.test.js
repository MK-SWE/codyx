const anagram = require('./submit').anagram;

function main() {
  const examples = {
    test_1: { input: ["hello", "world"], expected: false },
    test_2: { input: ["listen", "silent"], expected: true },
    test_3: { input: ["racecar", "carrace"], expected: true }
  };
  const res = {};

  try {
    const test_1 = anagram(examples.test_1.input[0], examples.test_1.input[1]);
    if (test_1 === examples.test_1.expected) {
      res.test_1 = {
        status: 'OK',
        input: examples.test_1.input,
        expected: examples.test_1.expected,
        got: test_1
      };
    } else {
      res.test_1 = {
        status: 'Error',
        input: examples.test_1.input,
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
    const test_2 = anagram(examples.test_2.input[0], examples.test_2.input[1]);
    if (test_2 === examples.test_2.expected) {
      res.test_2 = {
        status: 'OK',
        input: examples.test_2.input,
        expected: examples.test_2.expected,
        got: test_2
      };
    } else {
      res.test_2 = {
        status: 'Error',
        input: examples.test_2.input,
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
    const test_3 = anagram(examples.test_3.input[0], examples.test_3.input[1]);
    if (test_3 === examples.test_3.expected) {
      res.test_3 = {
        status: 'OK',
        input: examples.test_3.input,
        expected: examples.test_3.expected,
        got: test_3
      };
    } else {
      res.test_3 = {
        status: 'Error',
        input: examples.test_3.input,
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

  return res;
}

console.log(main());
