class Solution:
    def possibleStringCount(self, word: str) -> int:
        letters = []
        repeat = 0
        old = ''
        current = ''
        for i in range(len(word)):
            if word[i] not in letters:
                letters.append(word[i])
        for x in range(len(word)):
            current = word[x]
            if current == old:
                repeat += 1
            old = current
        return repeat + 1
