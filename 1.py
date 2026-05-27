# c=[6,True]
# a=[2,3,4,5,"4"]
# e=a[-3]
# e=e+1
# a[-3]=e
# print(a)
# d=c+a
# b=[True,False,d]
# print(type(a))
# print(type(b))
# print(a+b)
# a="我真的很帅"
# print(a[-2:-5:-3])
# a=([1,2,3,4,5],21,42,True)
a=[[1,2,3,4,5],21,42,True]
b=a[0]
b[2]=100
print(b)