def main():
  words = input("Please input some text: ")
  nicer = convert(words)
  print(nicer)

def convert(text):
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")
  return text

main()