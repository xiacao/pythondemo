import sys
try:
    weight, height = eval(input("请输入你的体重和身高(kg, m):"))
except:
    print("数值输入错误,请重新运行程序！")
    sys.exit()
BMI = weight/(height*height)
print("BMI : {0}".format(BMI))
if BMI < 18.5:
    print("体重偏瘦")
elif BMI < 24:
    print("体重正常")
elif BMI < 28:
    print("体重偏胖")
else :
    print("体重肥胖")
print("{0:^10}{1:^10}{2:^10}".format("体重","国际标准", "国内标准"))
print("{0:^10}{1:^10}{2:^10}".format("偏瘦","<18.5", "<18.5"))
print("{0:^10}{1:^10}{2:^10}".format("正常","18.5~25", "28.5~24"))
print("{0:^10}{1:^10}{2:^10}".format("偏胖","25~30", "24~28"))
print("{0:^10}{1:^10}{2:^10}".format("肥胖",">=30", ">=28"))
    
