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

weekDemand(int(input('数(0-6)> ')))







    
    

