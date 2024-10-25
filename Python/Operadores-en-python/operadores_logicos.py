p = input("p = ingresa si/no: ")
p = p.lower() == "si"

q = input("q = ingresa si/no: ")
q = q.lower() == "si"

print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")
