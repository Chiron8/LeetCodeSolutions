class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        solved = False
        while solved == False:
            string = str(num)
            li = list(string)
            product = 1
            for i in range(len(li)):
                product *= int(li[i])
            if product % t == 0:
                solved = True
                return num

            num += 1
