#find the sum of digits using while loop
n=456
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)