#Printing odd numbers sum upto n:
n=int(input('Enter n value:'))
sum=0
for i in range(1,n+1):
   if i%2==1:
      sum=sum+i
print("Sum of odd numbers up to",n,'is',sum)

#Printing even numbers sum upto n:
n=int(input('Enter n value:'))
sum=0
for i in range(2,n+1):
   if i%2==0:
      sum=sum+i
print("Sum of even numbers up to",n,'is',sum)
