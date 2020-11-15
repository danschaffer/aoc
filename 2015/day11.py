#!/usr/bin/env python3
class Password:
    def __init__(self, password):
        self.password = password

    def next(self):
        self.increment()
        while not self.is_valid():
            self.increment()

    def increment(self):
        index = len(self.password) - 1
        while index >= 0:
            if self.password[index] == 'z':
                self.password = self.password[0:index] + 'a' + self.password[index+1:]
                index -= 1
            else:
                self.password = self.password[0:index] + chr(ord(self.password[index]) + 1) + self.password[index+1:]
                break

    def has_straight3(self):
        for n in range(len(self.password) - 2):
            if ord(self.password[n]) == ord(self.password[n+1]) - 1 and ord(self.password[n+1]) == ord(self.password[n+2]) - 1:
                return True
        return False

    def has_invalid(self):
        return self.password.find('i') > -1 or self.password.find('o') > -1 or self.password.find('l') > -1

    def has_twopairs(self, str = None):
        if str is None:
            str1 = self.password
        else:
            str1 = str
        for ct in range(len(str1) - 1):
            if str1[ct] == str1[ct+1]:
                if str is None:
                    test1 = self.has_twopairs(str1[0:ct] + '01' + str1[ct+2:])
                    if test1:
                        return True
                    else:
                        continue
                else:
                    return True
        return False

    def is_valid(self):
        return self.has_twopairs() and self.has_straight3() and not self.has_invalid()

    def get_password(self):
        return self.password

def test1():
    password1 = Password('aaaaaaay')
    password1.increment()
    assert password1.get_password() == 'aaaaaaaz'
    password1.increment()
    assert password1.get_password() == 'aaaaaaba'
    password2 = Password('zzzzzzzz')
    password2.increment()
    assert password2.get_password() == 'aaaaaaaa'
    password3 = Password('aaaabcaaa')
    assert password3.has_straight3() == True
    password4 = Password('aaaaiaaa')
    assert password4.has_invalid() == True
    password5 = Password('abcdeggd')
    assert password5.has_twopairs() == False
    password6 = Password('abccddef')
    assert password6.has_twopairs() == True
    password7 = Password('hijklmmn')
    assert password7.is_valid() == False
    password8 = Password('abbceffg')
    assert password8.is_valid() == False
    password9 = Password('abbcegjk')
    assert password9.is_valid() == False
    password10 = Password('abcdefgh')
    password10.next()
    assert password10.get_password() == 'abcdffaa'

    password = Password('hepxcrrq')
    password.next()
    assert password.get_password() == 'hepxxyzz'
    password.next()
    assert password.get_password() == 'heqaabcc'

if __name__ == '__main__':
    password = Password('hepxcrrq')
    password.next()
    print(f"part 1: {password.get_password()}")
    password.next()
    print(f"part 2: {password.get_password()}")
