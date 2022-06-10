# Модуль интерфейса
from parser import complexculator
from log import add2log
def init():
    print('Программа - калькулятор')
    print('Умеет работать с комплексными числами')
    print('Напишите /help в коммандной строке, чтобы понять, как работать')
    
def _help():
    print('Команды:')
    print('\t /help - вывод справки')
    print('\t /exit или /quit  - выход из программы')
    print('\t /info - информация о разработчиках')
    print('')
    print('\t - посчитать простое выражение - пишем: 2+5*7')
    print('\t - посчитать выражение со скобками - пишем: 15/(7-(1+1))*3-(2+(1+1))')
    print('\t - посчитать выражение в комплексных числах- пишем: (2+3i)*(4+5i)')
    print('\t - посчитать навороченное выражение в комплексных числах- пишем: ((2+3i)*(4+5i))-3*((-3-6i)/8)')

def _info():
    print('Программа написана мегакрутыми парнями...')
    print('Надо список нас поставить...')
    

def interface():
    init()
    add2log('Начало работы','<')

    while True:
        inp = input('>>>')
        add2log(inp,'>')
        if inp.lower() == '/help':
            _help()
        elif inp.lower() == '/info':
            _info()
        elif input.lower() == '/exit':
            break
        elif input.lower() == '/quit':
            break
        else:
            res = complexculator(inp)
            print(res)
            add2log(res,'<')

    print('Завершение работы')
    add2log('Завершение работы','<')