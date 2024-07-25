from submit import merge_intervals

def compare_nested_lists(list1, list2):
    # Return indices of sublists that are not equal
    return [i for i, (sublist1, sublist2) in enumerate(zip(list1, list2)) if sublist1 != sublist2]

def main():
    examples = {
        'test_1': {'input': [[1,3],[2,6],[8,10],[15,18]], 'expected': [[1,6],[8,10],[15,18]]},
        'test_2': {'input': [[1,4],[4,5]], 'expected': [[1,5]]},
        'test_3': {'input': [[1,2],[3,5],[6,7],[8,10],[12,16]], 'expected': [[1,5],[6,7],[8,10],[12,16]]},
    }
    res = {}

    try:
        test_1 = merge_intervals(examples['test_1']['input'])
        compare = compare_nested_lists(test_1, examples['test_1']['expected'])
        if compare == []:
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
        test_2 = merge_intervals(examples['test_2']['input'])
        compare = compare_nested_lists(test_2, examples['test_2']['expected'])
        if compare == []:
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
        test_3 = merge_intervals(examples['test_3']['input'])
        compare = compare_nested_lists(test_3, examples['test_3']['expected'])
        if compare == []:
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
