from execEngine import DOCKER

res = DOCKER.run_tests(clientID='12345', challenge_name='fibonacci', code='def fibonacci(n):\n\t\t\t\ta, b = 0, 1\n\t\t\t\tfor _ in range(n):\n\t\t\t\t\t\ta, b = b, a + b\n\t\t\t\treturn a', submit_lang='py')

print(res)