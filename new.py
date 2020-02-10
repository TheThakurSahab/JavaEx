
# def gcd(a, b):
#     while(b!=0):
#         t=a
#         a=b
#         b=t%b
    
#     return a

# print(gcd(20,8))

a = [5,3,2,4,1,7,9,11,3]
max = 0
smax = 0
for i in range(8):
    if a[i]>max:
        smax = max
        max = a[i]
print(smax)