class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        ans = ""
        list1 = []
        for num in nums:
            if num.isnumeric():
                list1.append(num)
        while list1:
            last = list1.pop()
            if last != 0:
                ans += last
            elif ans and last == 0:
                ans += last
        rev = int(ans)
        if x < 0:
            rev = -1 * rev
        if rev < pow(-2, 31) or rev > (pow(2, 31) - 1):
            return 0 
        return rev
