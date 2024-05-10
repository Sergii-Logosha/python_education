# 10.05.24. Sergii Logosha sergiilogosha@gmail.com

print('Welcome to Tip Calculator!\n')

total_bill = float(input('What is the total bill? $'))
tips = float(input('What tip would you like to give, % (10, 15, 20, or 25): '))
number_of_people = int(input('How many people are sharing the bill? '))

bill_with_tips = total_bill * (1 + (tips / 100))
persons_share = bill_with_tips / number_of_people
print(f'Each person should pay: ${persons_share:.2f}')
