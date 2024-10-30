import string

def main():
  letters = list(string.ascii_uppercase)
  digits = list(string.digits)

  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  pass



main()
