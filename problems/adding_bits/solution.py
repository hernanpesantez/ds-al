

"""
zip function is used to combine two lists into a list of tuples.
zip takes two lists and returns a list of tuples.
"""


class Solution(object):
    def add_binary(self, x, y) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)

        # initialize the result
        result = ''

        # initialize the carry
        carry = 0

        # Traverse the string
        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1     # Compute the carry.

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)

res = Solution().add_binary('11', '1')
print(res)



def add_binary(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b= b.zfill(max_len)
    result = ''
    carry = 0

    print(a)
    print(b)

    for i in range(max_len  -1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(max_len)


res = add_binary('11', '1')
print(res)
