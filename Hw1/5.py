x = float(input('x: '))
y = float(input('y: '))

if x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0:
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть')
elif not x or not y:
    print('точка лежит на оси')
