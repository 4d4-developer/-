#Pythonブートキャンプ[データ分析コース]のchapter1の問
my_list = []
for i in range(1,11):
    my_list.append(i)
print(my_list)    
num = int(input("好きな整数を入力してください："))
if num>0:
    print("numは正の数です")
elif num == 0:
    print("numは0です")
else:
    print("numは負の数です")
new_list = []
for p in range(1,31):
    if p%3 == 0:
        new_list.append(p)
print(new_list)
for s in range (1,31):
    if s%10 == 0:
        print("10の倍数")
    else:
        print(s)
numbers = [t for t in range(1,31)if t%3==0]
print(numbers)    


