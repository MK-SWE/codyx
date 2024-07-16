import subprocess
import shutil
import os

def test_checker():
    # Test case 1: Test with Python code
    clientid = "test_client"
    challenge_name = "fibonacci"
    code = "from submit import fibonacci\nprint(fibonacci(5))"
    lang = "py"

    # Create test case file
    os.makedirs(clientid, exist_ok=True)
    with open(f'{clientid}/test_{challenge_name}.{lang}', 'w') as f:
        f.write(code)

    # Run the checker
    res = subprocess.run(['python', f'{clientid}/test_{challenge_name}.{lang}'], stdout=subprocess.PIPE).stdout.decode().strip()

    # Clean up
    shutil.rmtree(clientid)

    # Assert the result
    assert res == "5"

    # Test case 2: Test with JavaScript code
    clientid = "test_client"
    challenge_name = "sum"
    code = "console.log(2 + 3);"
    lang = "js"

    # Create test case file
    os.makedirs(clientid, exist_ok=True)
    with open(f'{clientid}/{challenge_name}.test.{lang}', 'w') as f:
        f.write(code)

    # Run the checker
    res = subprocess.run(['node', f'{clientid}/{challenge_name}.test.{lang}'], stdout=subprocess.PIPE).stdout.decode().strip()

    # Clean up
    shutil.rmtree(clientid)

    # Assert the result
    assert res == "5"

if __name__ == '__main__':
    test_checker()