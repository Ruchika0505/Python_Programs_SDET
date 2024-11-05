a=10
b=20

print(a)
print(b)

del a # delete the variable a from memory

print(a) # it should not be printed [NameError: name 'a' is not defined]
print(b)

