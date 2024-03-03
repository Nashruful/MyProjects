e = 1_000_000
print(f"House Price = {e}$")
x = input("what is the percantege you want to pay? : ")
words = x.split()
valid_percantege = []

for word in words:
    if '%' in word:
        percantege_str = ''.join(filter(lambda char: char.isdigit() or char == '.', word))
        percantege = float(percantege_str)
        valid_percantege.append(percantege)
print("this is the percanteges you got from your text: " +str(valid_percantege))
for percantege in valid_percantege:
    paid_amount = e * percantege / 100
    remaining = e - paid_amount
    print(f"For paying {percantege}%, you pay {paid_amount}$. {remaining}$ is remaining.")
