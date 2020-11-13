#!/usr/bin/env python3

class NiceString:
    def __init__(self, word):
        self.word = word

    def countVowels(self):
        count = 0
        for ch in list(self.word):
            if ch in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        return count

    def containsAtLeast3Vowels(self):
        return self.countVowels() >= 3

    def containsAtLeastOneLetterTwiceInARow(self):
        for ct in range(1, len(self.word)):
            if self.word[ct] == self.word[ct-1]:
                return True
        return False

    def containsAtLeastOneLetterTwiceInARowPair(self):
        for ct in range(len(self.word) - 3):
            pair = self.word[ct:ct+2]
            if self.word[ct+2:].find(pair) > -1:
                return True
        return False

    def containsAtLeastOneLetterinBetween(self):
        for ct in range(2, len(self.word)):
            if self.word[ct] == self.word[ct-2]:
                return True
        return False

    def containsPair(self):
        for ct in range(2, len(self.word)):
            if self.word[ct] == self.word[ct-2]:
                return True
        return False

    def doesNotContainString(self):
        if self.word.find('ab') > -1 or self.word.find('cd') > -1 or self.word.find('pq') > -1 or self.word.find('xy') > -1:
            return False
        return True

    def isNice1(self):
        return self.containsAtLeast3Vowels() and self.containsAtLeastOneLetterTwiceInARow() and self.doesNotContainString()

    def isNice2(self):
        return self.containsAtLeastOneLetterinBetween() and self.containsAtLeastOneLetterTwiceInARowPair()

    def __repr__(self):
        return self.word

def countNice1(words):
    count = 0
    for word in words:
        if NiceString(word).isNice1():
            count += 1
    return count

def countNice2(words):
    count = 0
    for word in words:
        if NiceString(word).isNice2():
            count += 1
    return count

def test1():
    assert NiceString('ugknbfddgicrmopn').containsAtLeast3Vowels()
    assert NiceString('aei').containsAtLeast3Vowels()
    assert NiceString('ugknbfddgirmpn').containsAtLeast3Vowels() is False
    assert NiceString('xx').containsAtLeastOneLetterTwiceInARow()
    assert NiceString('abcdde').containsAtLeastOneLetterTwiceInARow()
    assert NiceString('abcde').containsAtLeastOneLetterTwiceInARow() is False
    assert NiceString('ugknbfddgicrmopn').doesNotContainString()
    assert NiceString('ugkxynbfddgicrmopn').doesNotContainString() is False

def test2():
    assert NiceString('abcdefeghi').containsAtLeastOneLetterinBetween()
    assert NiceString('xyxy').containsAtLeastOneLetterTwiceInARowPair()
    assert NiceString('zaabcdefgaa').containsAtLeastOneLetterTwiceInARowPair()
    assert NiceString('aaa').containsAtLeastOneLetterTwiceInARowPair() is False
    assert NiceString('qjhvhtzxzqqjkmpb').isNice2()
    assert NiceString('xxyxx').isNice2()
    assert NiceString('uurcxstgmygtbstg').isNice2() is False
    assert NiceString('ieodomkazucvgmuy').isNice2() is False

if __name__ == '__main__':
    words = open('day5.input').read().strip().split()
    print(f"part 1 = {countNice1(words)}")
    print(f"part 2 = {countNice2(words)}")
