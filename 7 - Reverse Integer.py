class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = abs(x)
            negative = True
        else:
            negative = False
        li = list(str(x))
        for i in range(round(len(str(x))/2)):
            temp = li[i]
            li[i] = li[len(li) - 1 - i]
            li[len(li) - 1 - i] = temp
        num = ''.join(li)
        if negative == True:
            new = int(num) - int(num)*2
        else:
            new = int(num)
        if new > 2**31 -1 or new < -2**31:
            return 0
        else:
            return new
