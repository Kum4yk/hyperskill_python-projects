roots = input().split()
affixes = input().split()
word = input()
is_word = False
for root in roots:
    if word.startswith(root):
        for suffix in affixes:
            if word == root + suffix:
                is_word = True
                break
    elif word.endswith(root):
        for prefix in affixes:
            if word == prefix + root:
                is_word = True
                break
if is_word:
    print("It is a word")
else:
    print("It is not a word")
