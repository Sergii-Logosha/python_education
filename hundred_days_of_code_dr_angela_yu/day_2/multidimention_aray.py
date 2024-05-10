row_1 = [0, 0, 0]
row_2 = [0, 0, 0]
row_3 = [0, 0, 0]

maping = [row_1, row_2, row_3]
print(f'{row_1}\n{row_2}\n{row_3}\n')

x_position = input('Enter x-position: ')

x = int(x_position[0])
y = int(x_position[1])

selected_row = (maping[y - 1])
selected_row[x - 1] = 'X'

print(f'{row_1}\n{row_2}\n{row_3}\n')
print(maping)
