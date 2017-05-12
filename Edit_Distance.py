import copy
word1 = "b"
word2 = ""
n = len(word1)
m = len(word2)
        
print(n)
print(m)

inner = [0] * (m + 1)
d = [inner] * (n + 1)

for i in range(0, n + 1):
    c = i
    d[i][0] = c
    print(d)

for j in range(0, m + 1):
    c = j
    d[0][j] = c
    print(d)

print(d)


#for i in range(1, n + 1):
#    for j in range (1, m + 1):
#        r = d[i-1][j-1] + (0 if word1[i - 1] == word2[j - 1] else 1)
#        d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, r)
#
#        print("d[" + str(i) + "][" + str(j) + "] = " + str(d[i][j]))