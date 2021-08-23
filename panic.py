phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


plist.pop()
plist.pop()
plist.pop()
plist.pop()
plist.pop()
plist.pop(0)
plist.pop(2)
plist.pop(3)
plist.insert(2, " ")
plist.insert(4, "a")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
