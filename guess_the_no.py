import random
n=random.randint(1, 100)
a=-1
guesses=0
while(a !=n):
   guesses +=1
   a = int(input("guess the number: "))
   if(a>n):
      print("lowe number please")
      guesses +=1
   elif(a<n):
      print("higher number please")   
      guesses +=1


print(f"you have guessed the number {n} correctily in {guesses} attempt")
