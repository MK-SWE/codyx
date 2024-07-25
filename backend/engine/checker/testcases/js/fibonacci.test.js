const fibonacci = require('./submit').fibonacci;

function main() {
    const examples = {
        test_1: { input: 0, expected: 0 },
        test_2: { input: 1, expected: 1 },
        test_3: { input: -1, expected: 1 },
        test_4: { input: 6, expected: 8 },
        test_5: { input: 10, expected: 55 }
    };
    const res = {};

    try {
        const test_1 = fibonacci(examples.test_1.input);
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
        const test_2 = fibonacci(examples.test_2.input);
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
        const test_3 = fibonacci(examples.test_3.input);
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
        const test_4 = fibonacci(examples.test_4.input);
        if (test_4 === examples.test_4.expected) {
            res["test_4"] = {
                status: 'OK',
                input: examples.test_4.input,
                expected: examples.test_4.expected,
                got: test_4
            };
        } else {
            res["test_4"] = {
                status: 'Error',
                input: examples.test_4.input,
                expected: examples.test_4.expected,
                got: test_4
            };
        }
    } catch (error) {
        res["test_4"] = {
            status: 'Error',
            input: examples.test_4.input,
            expected: examples.test_4.expected,
            got: error.message
        };
    }

    try {
        const test_5 = fibonacci(examples.test_5.input);
        if (test_5 === examples.test_5.expected) {
            res["test_5"] = {
                status: 'OK',
                input: examples.test_5.input,
                expected: examples.test_5.expected,
                got: test_5
            };
        } else {
            res["test_5"] = {
                status: 'Error',
                input: examples.test_5.input,
                expected: examples.test_5.expected,
                got: test_5
            };
        }
    } catch (error) {
        res["test_5"] = {
            status: 'Error',
            input: examples.test_5.input,
            expected: examples.test_5.expected,
            got: error.message
        };
    }


    return res;
}

console.log(main());
