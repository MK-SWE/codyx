#!/usr/bin/env python3
""" console """

import re
import sys
import cmd
import shlex
from utils.__init__ import STORAGE


RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
CYAN = "\033[36m"  # Cyan text
RESET = "\033[0m"  # Reset to default color

ERRORS = {
    'notType': f"{RED}** ERROR: Unidentified Type {{}} **{RESET}",
    'missingType': f"{RED}** Provide Object Type **{RESET}",
    'notfound': f"{RED}** Object Not Found **{RESET}",
    'exists': f"{RED}** Object Already Exists **{RESET}",
    'empty': f"{RED}** Empty Table Or Database **{RESET}",
    'generic': f"{RED}** ERROR: {{}} **{RESET}",
    'doc': f"{CYAN}{{}}{RESET}",
    'noID': f"{RED}** Provide Object ID **{RESET}",
    'Types': f"{GREEN}Types: {{}}{RESET}"
}

class CodyX(cmd.Cmd):
    """Guidy Admin console"""
    prompt = f'{YELLOW}CodyX>{RESET} ' if sys.__stdin__.isatty() else ''

    from models.user import User
    from models.admin import Admin
    from models.challenge import Challenge
    classes = {"User": User,
               "Admin": Admin,
               "Challenge": Challenge
               }

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    types = {'rating': int, 'length': int, 'rating': int}

    def cmdloop(self, intro=None):
        while True:
            try:
                super().cmdloop(intro=intro)
                break
            except KeyboardInterrupt:
                self.do_quit('')
                return

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print(f'{YELLOW}CodyX>{RESET} ', end='')

    def precmd(self, line):
        STORAGE.reload()
        super().precmd(line)
        return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        self.preloop()
        return stop

    def _ArgParser(self, ObjD):
        """Creates a dictionary from arg list"""
        ArgDict = {}
        for arg in ObjD:
            if '=' not in arg:
                continue
            matches = re.match(r'(\w+)=(.*)', arg)
            if matches:
                k, v = matches.groups()
                if k in self.types:
                    v = self.types[k](v)
                else:
                    v = v.replace('_', ' ')
                ArgDict[k] = v
        return ArgDict

    def do_all(self, arg):
        """
        Prints string representations of instances
        [Usage]: all <Object Type> or all
        """
        Obj = shlex.split(arg)
        Type = Obj[0] if len(Obj) > 0 else ""
        ObjList = []
        ObjDict = {}

        if len(Obj) == 0:
            ObjDict = STORAGE.all()
        elif Type in self.classes:
            ObjDict = STORAGE.all(self.classes[Type])
        else:
            print(ERRORS['notType'].format(Type))
            return False

        if len(ObjDict) == 0:
            print(ERRORS['empty'])
            return False

        for key in ObjDict:
            ObjList.append(str(ObjDict[key]))

        print('\n' + CYAN + '\n\n'.join(ObjList) + RESET + '\n', end='\n')

    def do_create(self, arg):
        """
        Creates a new instance of an object
        [Usage]: create <Object Type> <Attribute1=Value1> <Attribute2=Value2>
        """
        try:
            ObjType = shlex.split(arg)
            if len(ObjType) == 0:
                print(ERRORS['missingType'])
                print(ERRORS['doc'].format(self.do_create.__doc__))
                print(ERRORS['Types'].format(list(self.classes.keys())))
                return False

            if ObjType[0] in self.classes:
                ArgDict = self._ArgParser(ObjType[1:])
                instance = self.classes[ObjType[0]](**ArgDict)
            else:
                print(f"{RED}** Unidentified Type {ObjType[0]} **{RESET}")
                return False
            instance.save()
            print(f'{CYAN}Instance Created with The id:{RESET} {GREEN}{instance.id}{RESET}')
            [print(f'{CYAN}{k}{RESET}: {GREEN}{v}{RESET}') for k, v in ArgDict.items()]

        except Exception as e:
            print(f"{RED}** {e} **{RESET}")
            return False

    def do_show(self, arg):
        """
        Prints an individual instance of an object
        [Usage]: show <Object Type> <Instance ID>
        """
        ObjD = shlex.split(arg)
        if len(ObjD) == 0:
            print(f"{RED}** Provide Object Type **{RESET}")
            return False

        if len(ObjD) < 2:
            print(f"{RED}** Provide Object ID **{RESET}")
            return False

        Type, ID = ObjD[0], ObjD[1]

        if Type not in self.classes:
            print(f"{RED}** Unidentified Type {Type}**{RESET}")
            return False
        Obj = STORAGE.get(self.classes[Type], ID)
        print(f'\n{CYAN}{Obj}{RESET}\n' if Obj else f"{RED}** NO Object Found **{RESET}")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class and id
        [Usage]: destroy <Object Type> <Instance ID>
        """
        ObjD = shlex.split(arg)

        if len(ObjD) == 0:
            print(f"{RED}** Object Type Missing **{RESET}")
            return False

        if len(ObjD) < 2:
            print(f"{RED}** Object ID Missing **{RESET}")
            return False

        Type, ID = ObjD[0], ObjD[1]

        if Type not in self.classes:
            print(f"{RED}** Unidentified Type {Type} **{RESET}")
            print(f"{RED}Types: {list(self.classes.keys())}{RESET}")
            return False

        k = f'{Type}.{ID}'
        try:
            STORAGE.delete(STORAGE.all()[k])
            STORAGE.save()
            print(f"{RED}** {Type} {ID} Deleted **{RESET}")
        except KeyError:
            print(f"{RED}** NO Object Found **{RESET}")


    def do_update(self, arg):
        """
        Update an instance based on the class Type, id, attribute & value
        [usage]: update <Object Type> <Instance ID> <Key> <Value>
        """
        ObjD = shlex.split(arg)

        if len(ObjD) == 0:
            print(f"{RED}** Object Type Missing **{RESET}")
            print(f"{GREEN}{self.do_update.__doc__}{RESET}")
            return

        if len(ObjD) < 3:
            print(f"{RED}** Provide Attribute Name**{RESET}")
            print(f"{GREEN}{self.do_update.__doc__}{RESET}")
            return

        if len(ObjD) < 4:
            print("** Provide Attribute Value **")
            print(f"{GREEN}{self.do_update.__doc__}{RESET}")
            return


        Type, ID = ObjD[0], ObjD[1]
        Key, Value = ObjD[2], ObjD[3] if len(ObjD) > 3 else ""
        Ints = ["rating", "length"]

        if Type not in self.classes:
            print(f"{RED}** Unidentified Type {Type} **{RESET}")
            return

        if len(ObjD) < 2:
            print(f"{RED}** Provide Object ID **{RESET}")
            return

        Obj = f'{Type}.{ID}'
        if Obj not in STORAGE.all():
            print(f"{RED}** NO Object Found **{RESET}")
            return

        if Key in Ints:
            try:
                Value = int(Value)
            except ValueError:
                Value = 0

        try:
            setattr(STORAGE.all()[Obj], Key, Value)
            print(f"{CYAN}** {Obj} {Key} Updated to {Value} **{RESET}")
            STORAGE.all()[Obj].save()
        except Exception as e:
            print(f"{RED}** {e.__cause__} **{RESET}")
            return False

    def do_count(self, arg):
        """
        Counts the number of instances of a class
        [Usage]: count <Object Type>
        """
        Obj = shlex.split(arg)
        if len(Obj) == 0:
            print()
            for key in self.classes:
                count = STORAGE.count(self.classes[key])
                print(f"{CYAN}{key:<10}{RESET}=> {YELLOW}{count}{RESET}")
            print()
            return

        if Obj[0] in self.classes:
            count = STORAGE.count(self.classes[Obj[0]])
            print(f'\n{CYAN}{Obj[0]:^10}{RESET}=> {YELLOW}{count}{RESET}\n')
        else:
            print(f"** Unidentified Type {Obj[0]} **")
            return False

    def do_EOF(self, arg):
        """Exits console"""
        print(f"\n{RED}Quitting...{RESET}")
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print(f"\n{RED}Quitting...{RESET}")
        return True


if __name__ == '__main__':
    CodyX().cmdloop()
