f1 = open("D:\\ai\ml_phd\medical19\\files.txt", "r", encoding="utf8")
f2 = open("D:\\ai\ml_phd\medical19\\answers.txt", "w")
s = []
k = []
for i in f1:
    if i not in s:
        s.append(i)
        f2.write(i)
    k.append(i)

print(len(s), len(k))