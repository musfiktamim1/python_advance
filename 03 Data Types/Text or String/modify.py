a = "Hello , World "

print(a)
print(a.upper())
print(a.lower())
print(a.strip()) #remove white space
print(a.replace("l","k"))
print(a.split(",")) #spliting by char
print(a.capitalize()) #first charecter capital and all small
print(a.casefold()) #convert lower case
print(a.center(50,"O")) #centering text
print(a.count("l")) # counting carecter
print(a.encode(encoding="ascii",errors="backslashreplace"))
print(a.endswith("World "))
print("HE\tHE\tJE".expandtabs(20)) #define tab spaces
print(a.find("l")) #finding the first index of l - start index for ingnore first one

#formate
print("this is my {age}".format(age=20))

print("this is my {age:.2f}".format(age=20)) # .2f for 2 decimal value
print("this is {name} or {age}".format(name="musfik",age=20))
print("this is {0} or {1}".format("musfik",20))
print("this is {} or {}".format("musfik",20))
print("this is {} or {:.3f}".format("musfik",20))


# formate map 
print("this is my {age} or this is my {name}".format_map({"name":"MUSFIK","age":20}))

print(a.index("l"))

print("abc20".isalnum()) #is alphabet or number
print("abc20".isalpha()) #is all aphabet
print("abc".isalpha()) #is all aphabet
print("is".isascii()) #if in this asccii

print("20".isdecimal()) #if all charecter is number
print("20".isdigit())
print("musfik tamim".isidentifier()) #is identitfirer or not
print(a.islower()) #is all charecter is lower
print(a.isupper()) #is all charecter is uper
print("20".isnumeric()) #is numeric
print("20a\t".isprintable())
print("  ".isspace()) #is only spaces
print("Hello Wolrd".istitle())

print("#".join("abc")) #every charecter after #
print("#".join(("abc","def","ghi")))

print("banana".ljust(20,"@"),"end")
print("banana".rjust(20,"@"),"end")
print("  Ab c  ".lstrip())
print("  ABC   ".rstrip())
#make trans
mytable = str.maketrans("am","bd")
print("musfiktamim".translate(mytable))
print("this is my name and".partition("name"))