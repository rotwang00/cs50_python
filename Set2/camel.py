"""
PEDAC

Problem: Given a filename in camel case, convert it to snake case

Example: firstName ==> first_name

Data structure: No additional structures

Algorithm:

  Ask user for input
  Begin infinite while loop  
  Reset while loop flag
  Loop through the string with "for char in s"
  If char is uppercase:
    Replace it with "_" and lowercase version of char
    Set while loop flag
    Break out of string loop
  When there are no more uppercase letters, the while loop will terminate
  Print output to screen in the format
    snake_case: [snake case version]
 

"""

name = input("camelCase: ")

found = True
while found:
  found = False
  for char in name:
    if char.isupper():
      name = name.replace(char, "_" + char.lower())
      found = True
      break

print(f"snake_case: {name}")