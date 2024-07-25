import os
import subprocess
import sys
import json

def checker():
    """
    This function executes a code submission for a given challenge and language.
    It performs the following steps:
    1. Retrieves the client ID, challenge name, code, and language from command-line arguments.
    2. Copies the corresponding test cases file to a directory named after the client ID.
    3. Decodes the escape sequences in the code.
    4. Writes the decoded code to a file named 'submit.{lang}' in the client ID directory.
    5. Executes the checker for the submitted code using the appropriate interpreter.
    6. Prints the result of the checker.
    7. Removes the client ID directory.

    Args:
        None

    Returns:
        None
    """

    clientid = sys.argv[1]
    challenge_name = sys.argv[2]
    code = sys.argv[3]
    lang = sys.argv[4]

    checkers = {
        'py': 'python',
        'js': 'node'
    }
    test_cases = {
        'py': f'checker/testcases/{lang}/test_{challenge_name}.py',
        'js': f'checker/testcases/{lang}/{challenge_name}.test.js'
    }
    
    subprocess.run(['mkdir', '-p', clientid])
    subprocess.run(['cp', test_cases[lang], f'{clientid}'])
    subprocess.run(['touch', f'{clientid}/__init__.py'])
    
    code_decoded = bytes(code, "utf-8").decode("unicode_escape")
    with open(f'{clientid}/submit.{lang}', 'w') as f:
        f.write(code_decoded)

    os.environ['PYTHONPATH'] = f"$PYTHONPATH:/usr/src/app/{clientid}"
    res = subprocess.run([checkers[lang], f'{clientid}/test_{challenge_name}.{lang}'], stdout=subprocess.PIPE).stdout.decode().strip()

    print(res)
    subprocess.run(['rm', '-rf', clientid])

if __name__ == '__main__':
    checker()
