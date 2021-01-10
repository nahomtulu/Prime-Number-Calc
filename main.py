
def prime_checker(number):
  if number > 1:
    for i in range(2,number):
      if (number % i) == 0 :
        print(f"{number} is not a prime number")  
      else:
        print(f"{number} is a prime number")
      break
  else:
    print(f"{number} is not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
