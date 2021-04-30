########################################### For döngüsü listeler değer okuma

#mynewlist=[("a","b"),("c","d")]
#for (x,y) in mynewlist:
 #   print(x,y)



#mydictionary={"key1":100,"key2":200}

#print(mydictionary.items())
#print(mydictionary.keys())
#print(mydictionary.values())

#for key,value in mydictionary.items():
#    print(key,value)

###################################### Break - Continue - Pass

mylist = [1,2,3,4,5,6,7,8,10]

for num in mylist:
    if num == 4:
        break
    print(num*5)

for item in mylist:
    if item == 7:
        continue
    print(item)

