from submit import palindrome

def main():
    examples = {
        'test_1': {'input': 'hello', 'expected': False},
        'test_2': {'input': "0_0 (: /-\\ :) 0–0", 'expected': True},
        'test_3': {'input': 1, 'expected': 'Input must be a string'},
    }
    res = {}

    try:
        test_1 = palindrome(examples['test_1']['input'])
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
        test_2 = palindrome(examples['test_2']['input'])
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
      test_3 = palindrome(examples['test_3']['input'])
      res['test_3'] = {
            'status': 'Error',
            'input': examples['test_3']['input'],
            'expected': examples['test_3']['expected'],
            'got': test_3
        }
    except TypeError as error:
      res['test_3'] = {
        'status': 'OK',
        'input': examples['test_3']['input'],
        'expected': examples['test_3']['expected'],
        'got': str(error)
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
