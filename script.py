from unittest import case


x,y = 1000,10000
def calc(x,y,mode) :
    type = '-'
    if mode == '-':
        type = '-'
        result = x - y
    elif mode == '+':
        type = '+'
        result = x + y
    elif mode == '*':
        type = '×'
        result = x * y
    elif mode == '%': #割り算の商と余り
        type = '÷'
        sho = x // y
        amari = x % y
    elif mode == '/':
        type = '÷'
        result = x / y
    
    if mode == '%':
        print(x,type,y,'=',sho,'余り',amari, sep=' ')
    else:
        print(x,type,y,'=',result,sep=' ')
    

calc(x,y,'+')
calc(x,y,'-')
calc(x,y,'*')
calc(x,y,'%') 
calc(x,y,'/')



