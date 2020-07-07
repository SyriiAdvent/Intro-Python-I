user_num = int(input("Select a number: "))

if user_num > 1:
  for num in range(2, user_num):
    if user_num % num == 0:
      print(f"{user_num} is not a prime number.")
      break
  else:
      print(f"{user_num} is a prime number.")
else:
  print(f"{user_num} is not a prime number.")