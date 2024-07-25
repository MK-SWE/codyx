from submit import kth_largest_element

def main():
    examples = {
        'test_1': {'input': [[3, 2, 1, 5, 6, 4], 2], 'expected': 5},
        'test_2': {'input': [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], 'expected': 4},
        'test_3': {'input': [[-1, 2, 0], 1], 'expected': 2},
        'test_4': {'input': [[], 5], 'expected': 0}
    }
    res = {}

    try:
        test_1 = kth_largest_element(examples['test_1']['input'][0], examples['test_1']['input'][1])
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
        test_2 = kth_largest_element(examples['test_2']['input'][0], examples['test_2']['input'][1])
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
        test_4 = kth_largest_element(examples['test_4']['input'][0], examples['test_4']['input'][1])
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
