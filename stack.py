# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('Mangga') #data pertama masuk
stack.append('Apel') #data kedua masuk
stack.append('Jeruk') #data ketiga masuk
stack.append('Melon')
stack.append('Anggur')
stack.append('Jambu')

print('-------DAFTAR BUAH-BUAHAN -------')
print(stack)

# pop() function to pop
print('\n Buah Yang di-POP dari list :')
print(stack.pop())

print('\n Daftar Buah setelah data terakhir di-POP :')
print(stack)

print('\n Buah Yang di-POP dari list :')
print(stack.pop())

print('\n Daftar Buah setelah data terakhir di-POP')
print(stack)
