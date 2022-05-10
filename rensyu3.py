#BMI計算
# height = float(input('身長をm単位で入力して下さい＞'))
# weight = float(input('体重をｋｇ単位で入力して下さい＞'))
# bmi = weight / height **2
# print('BMI = ', bmi, sep=' ') #ctrl + /

#時速から秒速変換
# hspeed = float(input('時速（ｋｍ/ｈ）＞'))
# sspeed = hspeed*1000.0/60**2
# print('秒速　＝　', sspeed, 'm/s', sep=' ')

#10進数から2進数への変換関数（整数255以下まで）
# def binaryCalc(num): 
#     b128,b64,b32,b16,b8,b4,b2,b1 = 0,0,0,0,0,0,0,0 #0で初期化
#     first = num
#     while num != 0: #数字がある限り回す
#         if num >= 128:
#             b128 = 1
#             num -= 128
#         elif num >= 64:
#             b64 = 1
#             num -= 64
#         elif num >= 32:
#             b32 = 1
#             num -= 32
#         elif num >= 16:
#             b16 = 1
#             num -= 16
#         elif num >= 8:
#             b8 = 1
#             num -= 8
#         elif num >= 4:
#             b4 = 1
#             num -= 4
#         elif num >= 2:
#             b2 = 1
#             num -= 2
#         elif num >= 1:
#             b1 = 1
#             num -= 1
#     binary = str(b128)+str(b64)+str(b32)+str(b16)+str(b8)+str(b4)+str(b2)+str(b1)
#     print(first,'=',binary,sep=' ')


# num = int(input('10進数> '))
# binaryCalc(num)


#金種計算
# def moneyCalc(money):
#     rest = money
#     moneys = {
#         '一万円札':10000,'五千円札':5000,'千円札':1000,'五百円玉':500,'百円玉':100,'五十円玉':50,'十円玉':10,'五円玉':5,'一円玉':1
#     }
#     for key in moneys:
#         maisuu = rest // moneys[key]
#         rest %= moneys[key]
#         print(key,'=',maisuu,'枚',sep=' ')
        

# money = int(input('金額（円）＞'))
# print('金額：',money,'円',sep=' ')
# moneyCalc(money)

#BMI計算改良版
# def bmiCalc(height,weight):#BMI計算関数
#     bmi = weight / height **2
#     print('BMI = ', bmi, sep=' ')
#     if bmi < 18.5:
#         print('あなたは「'+'痩せすぎ'+'」です。')
#     elif bmi >= 18.5 and bmi < 25.0:
#         print('あなたは「'+'標準'+'」です。')
#     elif bmi >= 25.0 and bmi < 30.0:
#         print('あなたは「'+'肥満'+'」です。')
#     else:
#         print('あなたは「'+'高度肥満'+'」です。')

# height = float(input('身長をm単位で入力して下さい＞'))
# weight = float(input('体重をｋｇ単位で入力して下さい＞'))
# bmiCalc(height,weight)

#整数曜日変換
def weekDemand(num):
    weeks = {
    0:'日曜日',1:'月曜日',2:'火曜日',3:'水曜日',4:'木曜日',5:'金曜日',6:'土曜日'
    }
    if num > 6:
        print('0〜6までの整数を入力して下さい。')
    else:
        print(weeks[num])

#weekDemand(int(input('数(0-6)> ')))

#うるう年の判定
def leapYear(year):
    if year % 400 == 0:
        print(str(year)+'年はうるう年です。')
    elif year % 100 == 0:
        print(str(year)+'年はうるう年ではありません。')
    elif year % 4 == 0:
        print(str(year)+'年はうるう年です。')
    else:
        print(str(year)+'年はうるう年ではありません。')

#leapYear(int(input('西暦で年を入力して下さい> ')))

#あなたの誕生日は何曜日
def birthdayWeek(year,month,day):
    weeks = {
    0:'日曜日',1:'月曜日',2:'火曜日',3:'水曜日',4:'木曜日',5:'金曜日',6:'土曜日'
    }
    datestr = f'{year}年{month}月{day}日'
    weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
    print(f'{datestr}は{weeks[weekday]}です。')

#birthdayWeek(int(input('年> ')),int(input('月> ')),int(input('日> ')))

#ジャンケンするプログラム
import random

def janken(yours):
    #Rock-paper-scissors
    RPS = {
        0:'グー', 1:'チョキ', 2:'パー'
    }
    judge = ['あなたの勝ちです。','あなたの負けです。','あいこです。']

    print('ジャンケンポン!')
    cpu = random.randint(0,2)
    if yours == cpu:
        result = 2
        connect = 'も'
    else:
        connect = 'は'
        if yours > cpu:
            if yours == 2 and cpu == 0:
                result = 0
            else: result = 1
        else:
            if yours == 0 and cpu == 2:
                result = 1
            else: result = 0
            
    print(f'わたしは{RPS[cpu]}。あなた{connect}{RPS[yours]}。{judge[result]}')

#janken(int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> ')))

#数の比較
def numComparison(a,b,c):
    numbers = [a,b,c]
    new = sorted(numbers)
    
    print(new[0],new[1],new[2],sep=' ')   


#numComparison(int(input('数1> ')),int(input('数2> ')),int(input('数3> ')))

#べき乗計算
# n = int(input('数> '))
# fac = 1
# for i in range(1,n+1) :
#     fac *= i
# print(str(n)+'! =',fac,sep=' ')

#棒グラフ
def barGraph(num):
    print(f'{str(num)}:',('■'*num))

#barGraph(int(input('数> ')))

#棒グラフver2
def barGraphs(num):
    for n in range(1,num + 1):
        print(f'{str(n)}:',('■'*n),sep=' ')

#barGraphs(int(input('数> ')))

#データ数のわからない集計
def totalling(data):
    counter,gokei = 0,0
    while data >= 0 :
        counter += 1
        gokei += data
        data = int(input('データ入力(負の数で終了)> '))
    heikin = gokei/counter
    print(f'データ数:,{counter},合計:,{gokei},平均:,{heikin}')

#totalling(int(input('データ入力(負の数で終了)> ')))

#借金を返済しよう
def debtCalc(shakkin,riritsu,hensai):
    total,month = 0,0
    while shakkin > hensai :
        month += 1
        shakkin = shakkin*(1 + riritsu/12/100) - hensai
        print(str(month)+'月: 返済額',hensai,'円','残り',\
        int(shakkin),sep=' ')
        total += hensai
    month += 1
    shakkinInt: int = int(shakkin*(1 + riritsu/12/100))
    total += shakkinInt
    print(f'{month}月: 返済額{shakkinInt}円これで完済。返済総額: \
    {total}円',sep=' ')

#debtCalc(int(input('借金> ')),float(input('年利率(%)> ')),int(input('返済額> ')))

#モンテカルロ・シミュレーション 
def monteCarlo(n):
    nc = 0
    for i in range(0,n) :
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1 :
            nc += 1
    pi = 4.0 * nc / n
    print('PI =',pi,sep=' ')

monteCarlo(int(input('実行回数> '))) 
