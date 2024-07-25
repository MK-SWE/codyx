from submit import subarray_sum_equals_k

def main():
    examples = {
        'test_1': {'input': [[1, 1, 1], 2], 'expected': 2},
        'test_2': {'input': [[1, 2, 3], 3], 'expected': 2},
        'test_3': {'input': [[1, -1, 0], 0], 'expected': 3},
        'test_4': {'input': [[], 5], 'expected': 0}
    }
    res = {}

    try:
        test_1 = subarray_sum_equals_k(examples['test_1']['input'][0], examples['test_1']['input'][1])
        if test_1 == examples['test_1']['expected']:
            res['test_1'] = {
                'status': 'OK',
                'input': examples['test_1']['input'],
                'expected': examples['test_1']['expected'],
                'got': test_1
            }
        else:
            res['test_1'] = {
                'status': 'Error',
                'input': examples['test_1']['input'],
                'expected': examples['test_1']['expected'],
                'got': test_1
            }
    except Exception as error:
        res['test_1'] = {
            'status': 'Error',
            'input': examples['test_1']['input'],
            'expected': examples['test_1']['expected'],
            'got': str(error)
        }

    try:
        test_2 = subarray_sum_equals_k(examples['test_2']['input'][0], examples['test_2']['input'][1])
        if test_2 == examples['test_2']['expected']:
            res['test_2'] = {
                'status': 'OK',
                'input': examples['test_2']['input'],
                'expected': examples['test_2']['expected'],
                'got': test_2
            }
        else:
            res['test_2'] = {
                'status': 'Error',
                'input': examples['test_2']['input'],
                'expected': examples['test_2']['expected'],
                'got': test_2
            }
    except Exception as error:
        res['test_2'] = {
            'status': 'Error',
            'input': examples['test_2']['input'],
            'expected': examples['test_2']['expected'],
            'got': str(error)
        }

    try:
        test_4 = subarray_sum_equals_k(examples['test_4']['input'][0], examples['test_4']['input'][1])
        if test_4 == examples['test_4']['expected']:
            res['test_4'] = {
                'status': 'OK',
                'input': examples['test_4']['input'],
                'expected': examples['test_4']['expected'],
                'got': test_4
            }
        else:
            res['test_4'] = {
                'status': 'Error',
                'input': examples['test_4']['input'],
                'expected': examples['test_4']['expected'],
                'got': test_4
            }
    except Exception as error:
        res['test_4'] = {
            'status': 'Error',
            'input': examples['test_4']['input'],
            'expected': examples['test_4']['expected'],
            'got': str(error)
        }

    return res

print(main())
