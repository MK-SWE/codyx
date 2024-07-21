import json
from submit import fibonacci

def main():
    res = {}

    try:
        test_1 = fibonacci(1)
        assert test_1 == 1
        res[1] = {
            "status": 'OK',
            'expected': 1,
            'got': test_1
        }
    except AssertionError:
        res[1] = {
            "status": 'Error',
            'expected': 1,
            'got': test_1
        }

    try:
        test_2 = fibonacci(2)
        assert test_2 == 1
        res[2] = {
            "status": 'OK',
            'expected': 1,
            'got': test_2
        }
    except AssertionError:
        res[2] = {
            "status": 'Error',
            'expected': 1,
            'got': test_2
        }

    try:
        test_3 = fibonacci(6)
        assert test_3 == 8
        res[3] = {
            "status": 'OK',
            'expected': 8,
            'got': test_3
        }
    except AssertionError:
        res[3] = {
            "status": 'Error',
            'expected': 8,
            'got': test_3
        }

    try:
        test_4 = fibonacci(10)
        assert test_4 == 55
        res[4] = {
            "status": 'OK',
            'expected': 55,
            'got': test_4
        }
    except AssertionError:
        res[4] = {
            "status": 'Error',
            'expected': 55,
            'got': test_4
        }

    return json.dumps(res)

if __name__ == '__main__':
    print(main())
