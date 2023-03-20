veg = ["apples", "celary", "i don't know leaves maby?"]
vagitarian = ["apples", "celary", "i don't know leaves maby?"]
vegan =  ["Hemp","flax" , "chia seeds"]
nope = ["burgur", "bacon", "eggs"]

print("do you have any dietary requirements?")
print("veg (vagitarian), vegan, Nope")

Diet_Req = input().lower()

if Diet_Req == "vegan":
  print("Take va look at these options")
  print(vegan)

if Diet_Req == "vagitarian":
  print("ohhhh so you're difficault. Here are your options:")
  print(veg)

if Diet_Req == "veg":
  print("ohhhh so you're difficault. here are your options")
  print(veg)

if Diet_Req == "nope":
  print("ahh you're one of those Here are your options:")
  print(nope)
