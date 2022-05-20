from collections import Counter

class DuplicateValues:

    def DuplicateValues(self, n):

        a = []
        b = []
        for i in range(len(n)):
            result = Counter(n[i])
            for j in range(len(list(result.values()))):
                if ((list(result.values()))[j]) > 1:
                    a.append((list(result.keys()))[j])
                    b.append((list(result.values()))[j])

        for i in range(len(a)):

            print(a[i], "->", b[i])


n = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
print("The list is:")
print(n)

print("\nThe duplicate values are:")
duplicate = DuplicateValues()
duplicate.DuplicateValues(n)
