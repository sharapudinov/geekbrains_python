expenses = int(input('затраты (в рублях) '))
proceeds = int(input('выручка (в рублях) '))

profit = proceeds - expenses
if profit < 0:
    print(f'убыток составил {profit} руб.')
elif profit == 0:
    print('пустая трата времени')
else:
    print('вы получили прибыль {}руб., при рентабельности {:.2%}'.format(profit,profit/expenses))
    person_count=int(input('назовите число сотрудников '))
    print(f'удельная прибыль составила {profit/person_count}руб. на сотрудника ')


