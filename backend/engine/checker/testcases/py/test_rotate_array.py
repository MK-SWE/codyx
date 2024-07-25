from submit import rotate_array

def main():
    examples = {
        'test_1': {'input': [[1, 2, 3, 4, 5], 2], 'expected': [4, 5, 1, 2, 3]},
        'test_2': {'input': [[1, 2, 3], 4], 'expected': [3, 1, 2]},
        'test_3': {'input': [[1, 2, 3, 4, 5, 6, 7], 3], 'expected': [5, 6, 7, 1, 2, 3, 4]},
    }
    res = {}

    try:
        test_1 = rotate_array(examples['test_1']['input'][0], examples['test_1']['input'][1])
        check = [i for i, (a, b) in enumerate(zip(examples['test_1']['expected'], test_1)) if a != b]
        if check == []:
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
        test_2 = rotate_array(examples['test_2']['input'][0], examples['test_2']['input'][1])
        check = [i for i, (a, b) in enumerate(zip(examples['test_2']['expected'], test_2)) if a != b]
        if check == []:
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
        test_3 = rotate_array(examples['test_3']['input'][0], examples['test_3']['input'][1])
        check = [i for i, (a, b) in enumerate(zip(examples['test_3']['expected'], test_3)) if a != b]
        if check == []:
            res['test_3'] = {
                'status': 'OK',
                'input': examples['test_3']['input'],
                'expected': examples['test_3']['expected'],
                'got': test_3
            }
        else:
            res['test_3'] = {
                'status': 'Error',
                'input': examples['test_3']['input'],
                'expected': examples['test_3']['expected'],
                'got': test_3
            }
    except Exception as error:
        res['test_3'] = {
            'status': 'Error',
            'input': examples['test_3']['input'],
            'expected': examples['test_3']['expected'],
            'got': str(error)
        }

    return res

print(main())
