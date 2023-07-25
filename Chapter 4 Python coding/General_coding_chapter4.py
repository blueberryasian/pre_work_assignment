burgers = ["innout" , "mcdo" , "arbys", "toms" , "jack"]
for burger in burgers:
 #print(burger)
 print(burger.title() + ", has yummy burgers!")
 print("I can't wait to try the new burgers you have on the menu, " + burger.title() + "!\n")
#Since the next line isn't indented it only prints once
print("Thank you, everyone! Those burgers were gas!")
print("The first three items in this list are:")
print(burgers[0:3])
print("Three items from the middle of this list are:")
print(burgers[1:4])
print("The last three items in this list are:")
print(burgers[-3:])
