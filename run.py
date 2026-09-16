# Dunder __builtins__, __init__

message = "PYTHON: Everything is object!"
print(message)
result = type(message)
print("result", result)

''' in pyton, there are builtin tools:
(1) types > int float str list dict
(2) functions > print() input() len() type() range() sum() min() max()
(3) constants > True False None
'''
print(dir(__builtins__))
