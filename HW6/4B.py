from itertools import permutations

getName = {}
c = [1, 9, 12, 18]
g = [2, 10, 11, 17]
a = [4, 5, 8, 13, 16, 19]
u = [3, 6, 7, 14, 15, 20]
for i in c:
    getName[i] = "C"
for i in g:
    getName[i] = "G"
for i in a:
    getName[i] = "A"
for i in u:
    getName[i] = "U"

CG = [[] for _ in range(24)]
AU = [[] for _ in range(720)]

matchings = 0

GPerms = list(permutations(g))
UPerms = list(permutations(u))

# connecting all possible C-G
for i in range(len(GPerms)):
    for j in range(len(c)):
        CG[i].append(min(c[j], GPerms[i][j]))
        CG[i].append(max(c[j], GPerms[i][j]))
# print(cg)

# connecting all possible A-U
for i in range(len(UPerms)):
    for j in range(len(a)):
        AU[i].append(min(a[j], UPerms[i][j]))
        AU[i].append(max(a[j], UPerms[i][j]))


def intersects(x, i, j, y):
    if x < j < i < y:
        return 1
    return 0


# remove intersecting CG in their perms
unsuitableCG = []
for i in range(len(CG)):
    chh = False
    for f in range(len(c)):
        # print(cg[i])
        for z in range(f + 1, len(c)):
            if CG[i][f * 2] < CG[i][z * 2]:
                chh += intersects(CG[i][f * 2], CG[i][f * 2 + 1], CG[i][z * 2], CG[i][z * 2 + 1])
            if CG[i][f * 2] > CG[i][z * 2]:
                chh += intersects(CG[i][z * 2], CG[i][z * 2 + 1], CG[i][f * 2], CG[i][f * 2 + 1])
    if chh:
        unsuitableCG.append(i)

for i in range(len(unsuitableCG)):
    del (CG[unsuitableCG[i] - i])

# remove intersecting AU in their perms
unsuitableAU = []
for i in range(len(AU)):
    chh = False
    for f in range(len(a)):
        for z in range(f + 1, len(a)):
            if AU[i][f * 2] < AU[i][z * 2]:
                chh += intersects(AU[i][f * 2], AU[i][f * 2 + 1], AU[i][z * 2], AU[i][z * 2 + 1])
            if AU[i][f * 2] > AU[i][z * 2]:
                chh += intersects(AU[i][z * 2], AU[i][z * 2 + 1], AU[i][f * 2], AU[i][f * 2 + 1])
    if chh:
        unsuitableAU.append(i)

for i in range(len(unsuitableAU)):
    del (AU[unsuitableAU[i] - i])

# choose onlu suitable combinations
for i in range(len(AU)):
    for j in range(len(CG)):
        chh = False
        for k in range(6):
            for l in range(4):
                if AU[i][k * 2] < CG[j][l * 2]:
                    chh += intersects(AU[i][k * 2], AU[i][k * 2 + 1], CG[j][l * 2], CG[j][l * 2 + 1])
                if AU[i][k * 2] > CG[j][l * 2]:
                    chh += intersects(CG[j][l * 2], CG[j][l * 2 + 1], AU[i][k * 2], AU[i][k * 2 + 1])

        if not chh:
            matchings += 1
            print("Matching №%s" % str(matchings))
            for _ in range(0, len(AU[i]), 2):
                print("{number1}({symb1}) - {number2}({symb2})".format(
                    number1=AU[i][_], number2=AU[i][_ + 1], symb1=getName[AU[i][_]], symb2=getName[AU[i][_ + 1]]))
            for _ in range(0, len(CG[j]), 2):
                print("{number1}({symb1}) - {number2}({symb2})".format(
                    number1=CG[j][_], number2=CG[j][_ + 1], symb1=getName[CG[j][_]], symb2=getName[CG[j][_ + 1]]))
            print()
