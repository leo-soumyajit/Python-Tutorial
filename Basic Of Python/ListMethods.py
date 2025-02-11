#list.append() append anything at the last of the list
list = [1,2,3,4,5,6]
print(list)
list.append(7)
print(list)
list.append("Kanu")
list.append("Dhoni")
print(list)

#list.sort() sort in ascending order sort(reverse=true) descending order

numbers = [100,22,3,10,45,12,1,3]
print(numbers)
numbers.sort() #ascending order
print(numbers)
numbers.sort(reverse=True) #descending order
print(numbers)

#list.reverse() used to reverse the whole list
lists = [1,23,41,4,5]
lists.reverse()
print(lists)

#index() used to give the index of an item (1st occurrence)
num = [1,23,41,4,5]
print(num.index(1))

#count() used to count item in list

ramdom = [1,2,6,33,1,1,4,6,73,6,8,0,7,5,18,5,7]
print(ramdom.count(7))

#copy() its used when we need a newList without modifying oldList
old = ["Messi","Neymar Jr","Suarez","Ronaldo","Zlatan","Lewa"]
print(old)
newList = old.copy()
print(newList)

#insert() used to add item to a perticuler index

listt = [1,2,3,4,5]
listt.insert(5,"newItem")
print(listt)

#extend() concat two list list1.extend(list2)
#now list1 has his own items and also list2's items

fruits = ["apple","guava","grapes"]
foods = ["chicken","mutton","burger"]
foods.extend(fruits)
print(foods)

#also using + we can concat two list
list1 = [1,2,3,4]
list2 = [10,11,12,13]
print(list1+list2)