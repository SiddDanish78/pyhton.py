# Input funcation  by chat gpt pahele in easy language  

# 1-  input() ye hai input function 
# 2- input() funcation python ko kehta hai user se kuch poochho aur uska jawab lelo
variable = input("Kya poochhna hai?") # jo user keyboard se likhega vo variable me store ho jayega 
print (variable)
 
# ye dekh lo real life example 
name = input("what is your name")
print ("hellow",name)

# 🔹 Jab bhi tum input() use karte ho,
# to jo bhi user likhta hai, wo Python hamesha "text" (string) samajhta hai
# Chahe user number hi likhe — wo bhi text ban jaata hai.

# Example 1 

age = input ("enter your age")
print (age + 6) # TypeError: ye number aur string ko to add krega nahi 
print(age +"6")   # agar aise likhunga to jo age dunga maan lo x diya aayega (x6) kuy ki 6 ko string me likha to python isko text samaj rha hai ok 

# to iska solution ye hai 

age = int(input ("enter your age "))
print (age +6)

# | User Input | Python Samjhta Hai | Solution                  |
# | ---------- | ------------------ | ------------------------- |
# | `"21"`     | Text (string)      | Use `int()` to convert    |
# | `"3.5"`    | Text (string)      | Use `float()` to convert  |
# | `"true"`   | Text (string)      | Not boolean automatically |


