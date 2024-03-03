s = "rjiewirjwejrqjqjq"
r = []
for char in set(s):
    r.append(s.count(char))

print(max(r))