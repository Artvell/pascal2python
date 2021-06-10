A = int(input('Введите длину: '))
B = int(input('Введите шириру: '))
L = int(input('Введите дистанцию: '))
P = (A+B)*2
Circle = L//P
L = L-P*Circle
if (L<=B):
    print('LEFT')
if ((L>B)and(L<=(A+B))):
    print('BOTTOM')
if ((L>(A+B))and(L<=(A+2*B))):
    print('RIGHT')
if ((L>A+2*B)and(L<=P)):
    print('TOP')
A = int(input('Введите длину: '))
B = int(input('Введите шириру: '))
L = int(input('Введите дистанцию: '))
P = (A+B)*2
Circle = L//P
L = L-P*Circle
if (L<=B):
    print('LEFT')
if ((L>B)and(L<=(A+B))):
    print('BOTTOM')
if ((L>(A+B))and(L<=(A+2*B))):
    print('RIGHT')
if ((L>A+2*B)and(L<=P)):
    print('TOP')
A = int(input('Введите длину: '))
B = int(input('Введите шириру: '))
L = int(input('Введите дистанцию: '))
P = (A+B)*2
Circle = L//P
L = L-P*Circle
if (L<=B):
    print('LEFT')
if ((L>B)and(L<=(A+B))):
    print('BOTTOM')
if ((L>(A+B))and(L<=(A+2*B))):
    print('RIGHT')
if ((L>A+2*B)and(L<=P)):
    print('TOP')
k = int(input())
t = int(input())
t = t%(2*k)
if t<=k:
    print(t)
else:
    print(2*k-t)
