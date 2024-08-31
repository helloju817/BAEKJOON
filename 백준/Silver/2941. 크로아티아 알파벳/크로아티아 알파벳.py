import sys
word = sys.stdin.read().strip()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for pattern in alphabet:
    word = word.replace(pattern, "K")

ans = len(word)
print(ans)
