guestlist = ["andrew tate" , "sean" , "joe"]
message = ("Hey, " + guestlist[0].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[1].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[2].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = guestlist[0].title() + " will not be able to attend tonights dinner"
print(message)
guestlist[0] = "donald trump"
print(guestlist)
message = ("Hey, " + guestlist[0].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[1].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[2].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = "we have found a bigger table, we will be inviting three more guests"
print(message.upper())
guestlist.insert(0, "Elon musk")
guestlist.insert(2, "naruto")
guestlist.append("sasuke")
print(guestlist)
message = ("Hey, " + guestlist[0].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[1].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[2].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[3].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[4].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = ("Hey, " + guestlist[5].title() + " it would be an honor for you to come to my dinner!")
print(message)
message = "my bad yall only two people can come, our new table hasn't arrived"
print(message.title())
sorry = guestlist.pop()
message = "Hey " + sorry.title() + " it is in my sincerest apologies that i will not be able to have you over for dinner"
print(message)
sorrry = guestlist.pop()
message = "Yo my bad " + sorrry.upper() + " the table ain't come through i can't have you over"
print(message)
sorrrry = guestlist.pop()
message = "Bruh " + sorrrry.lower() + " my wife told me the wrong date for the arrival of the table you can't come sowwy"
print(message)
nah = guestlist.pop()
message = "super sorry " + nah.title() + " my table hasn't arrived i won't be able to host you this weeekend"
print(message)
message = "Hey Mr. " + guestlist[0].title() + " I hope you can make it this weekend, It'll just be you, Mr. Trump, My wife and myself"
print(message)
message = "Yo Theeee " + guestlist[-1].title() + " don't forget to slide this weekend, It's gonna be you, me, my wife and the bro Elon musk."
print(message)
del guestlist[1]
del guestlist[0]
print(guestlist)
print(len(guestlist))