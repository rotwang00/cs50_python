greeting = input("What's your greeting? ")

greeting = greeting.lstrip().lower()

if greeting == "hello":
  print("$0")
elif greeting[0] == "h":
  print("$20")
else:
  print("$100")
  