from submit import binary_search

def main():
    examples = {
        'test_1': {'input': [[1, 2, 3, 4, 5], 3], 'expected': 2},
        'test_2': {'input': [[1, 2, 3, 4, 5], 6], 'expected': -1},
        'test_3': {'input': [[1, 3, 5, 7, 9], 5], 'expected': 2},
        'test_4': {'input': [[], 5], 'expected': -1}
    }
    res = {}

    try:
        test_1 = binary_search(examples['test_1']['input'][0], examples['test_1']['input'][1])
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
        test_2 = binary_search(examples['test_2']['input'][0], examples['test_2']['input'][1])
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
        test_4 = binary_search(examples['test_4']['input'][0], examples['test_4']['input'][1])
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
