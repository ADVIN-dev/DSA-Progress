class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [] # Negative
        b = [] # Postive
        c = []
        i = j = 0

        while (i < len(nums)):
            if (nums[i] < 0):
                a.append(nums[i])
                i += 1
            else :
                b.append(nums[i])
                i += 1

        if (len(a) == 0):
            return [j * j for j in b]

        elif (len(b) == 0):
            a.reverse()
            return [i * i for i in a]

        a.reverse()

        i = j = 0

        for i in range(len(a)):
            a[i] = a[i] * a[i]

        for j in range(len(b)):
            b[j] = b[j] * b[j]

        i = j = 0

        while (i < len(a) and j < len(b)):
            if (a[i] < b[j]):
                c.append(a[i])
                i += 1

            else:
                c.append(b[j])
                j += 1

        while (i < len(a)):
            c.append(a[i])
            i += 1

        while (j < len(b)):
            c.append(b[j])
            j += 1

        return c