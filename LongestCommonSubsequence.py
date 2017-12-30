'''

l1
l2

ind1 = 0
ind2 = 0
lcs = []
while ind1 < len(l1) and ind2 < len(l2):
    if l1[ind1] in l2:
        lcs.append(l1[ind1])
        ind2 = l2.index(l1[ind1]) + 1
        continue

    if l2[ind2] in l1:
        lcs.append(l2[ind2])
        ind1 = l1.index(l2[ind2]) + 1
        continue
    ind1 += 1
    ind2 += 1

'''

l1 = 'AGGTAB'
l2 = 'GXTXAYB'
ind1 = 0
ind2 = 0
lcs = []

def find_longest_common_subsequence_from(ind, l1):
    pass

while ind1 < len(l1) and ind2 < len(l2):
    print 'lcs is', lcs
    if l1[ind1] in l2[ind2:]:
        lcs.append(l1[ind1])
        ind2 = l2.index(l1[ind1]) + 1
        continue

    if l2[ind2] in l1[ind1:]:
        lcs.append(l2[ind2])
        ind1 = l1.index(l2[ind2]) + 1
        continue
    ind1 += 1
    ind2 += 1
print lcs

