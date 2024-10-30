original = input("Input: ")

result = ""
vowels = list("aeiouAEIOU")
for char in original:
  if not char in vowels:
    result += char

print(f"Output: {result}")
