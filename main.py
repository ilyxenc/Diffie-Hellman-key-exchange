import functions as fn

a, b = fn.rand(5), fn.rand(5) # генерация закрытых ключей A и B
p = fn.randPrime(10) # простое число размерности 300
g = fn.primitiveRoot(p) # первообразный корень

print('Закрытый ключ a           :', a)
print('Закрытый ключ b           :', b)
print('Случайное простое число p :', p)
print('Первообразный корень g    :', g)
print('\n')

# генерация открытого ключа A
A = fn.power(g, a, p)
print('Открытый ключ A :', A)

# генерация открытого ключа B
B = fn.power(g, b, p)
print('Открытый ключ B :', B)
print('\n')

# общий секретный ключ
KA = fn.power(B, a, p)
print('Секретный ключ от ключа B :', KA)
KB = fn.power(A, b, p)
print('Секретный ключ от ключа A :', KB)
print(KA == KB)
