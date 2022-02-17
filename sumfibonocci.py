#sum of Fibonocci series
a=-1
b=1
n=int(input('enter no.of numbers:'))
sum=0
for i in range(1,n+1):
   c=a+b
   sum=sum+c
   a=b
   b=c
print('sum of Fibonocci series:',sum )
