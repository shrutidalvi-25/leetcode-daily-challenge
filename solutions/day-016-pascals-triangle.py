class Solution:
    def generate(self, numRows):
        a = []

        for i in range(numRows):
            r = [1] * (i + 1)

            for j in range(1, i):
                r[j] = a[i-1][j-1] + a[i-1][j]

            a.append(r)

        return a
