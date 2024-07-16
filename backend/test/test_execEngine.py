from engine.execEngine import DOCKER

def test_run_tests():
    # Test case 1: Empty code
    clientID = "123"
    challenge_name = "Fibonacci"
    code = ""
    submit_lang = "python"
    expected_result = "0%, []"
    assert DOCKER.run_tests(clientID, challenge_name, code, submit_lang) == expected_result

    # Test case 2: Invalid code
    clientID = "456"
    challenge_name = "Factorial"
    code = "print('Hello, World!')"
    submit_lang = "python"
    expected_result = "0%, ['1', '2', '3', '4']"
    assert DOCKER.run_tests(clientID, challenge_name, code, submit_lang) == expected_result

    # Test case 3: Correct code
    clientID = "789"
    challenge_name = "Palindrome"
    code = "def is_palindrome(s):\n    return s == s[::-1]"
    submit_lang = "python"
    expected_result = "100%, []"
    assert DOCKER.run_tests(clientID, challenge_name, code, submit_lang) == expected_result

    # Test case 4: Multiple failed tests
    clientID = "101112"
    challenge_name = "Prime Numbers"
    code = "def is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, n):\n        if n % i == 0:\n            return False\n    return True"
    submit_lang = "python"
    expected_result = "50%, ['1', '2', '3', '4']"
    assert DOCKER.run_tests(clientID, challenge_name, code, submit_lang) == expected_result

    print("All test cases passed!")

if __name__ == '__main__':
    test_run_tests()