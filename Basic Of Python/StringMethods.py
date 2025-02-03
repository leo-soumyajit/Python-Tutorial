#Strings are Immutable#

a = "Soumyajit"
print(a.upper()) #converts the upper case
print(a.lower()) #converts the lower case

str1 = "    Hows the josh?  "
print(str1.strip()) #remove trailing and extra spaces

str2 = "Hows the josh? !!!!!"
print(str2.rstrip("!")) #remove extra characters

str3 = "Dhoni is the captain cool"
print(str3.replace("Dhoni","Mahi")) #replace old String with new String

str4 = "Messi is the Goat of football"
print(str4.split(" ")) #converts into List with white space

str5 = "soumyajiTTT"
print(str5.capitalize()) #converts only 1st Character into capital letter rest of them are smaller

str6 = "Welcome to Python Programming"
print(str6)
print(str6.center(50)) #this method centered the output as per the parameter given by user

str7 = "Welcome to Python Programming"
print(str7.count("Python")) #counts the particular character's or String's occurrence and give the count number

str8 = "Welcome to Python Programming !!!"
print(str8.endswith("!")) #checks if the String is endsWith a given value or not
print(str8.endswith("come",3,7)) # can pass range also

str9 = "Sachin Tendulkar is the God of cricket"
print(str9.find("God")) #searches the first occurrence of given value if found gives index number if not -1

str10 = "Sachin Tendulkar is the God of cricket"
print(str10.index("God")) #similer to find() but if value not found throws exception

str11 = "AeiouAbc123"
print(str11.isalnum()) #returns True if entire String contains A-Z,a-z,0-9 if other character contains gives False

str12 = "AeiouAbc"
print(str12.isalpha()) #similer to isalnum() but only gives True when String contains A-Z,a-z otherwise False

str13 = "soumyajit"
print(str13.islower()) # checks if String contains only smaller letter

str14 = "Welcome to Python Programming !!!"
print(str14.isprintable()) #returns True if all the value of given String are printable if not returns False

str15 = "    "
print(str15.isspace()) #returns True if String contains only white spaces otherwise false

str16 = "Welcome To Python Programming !!!"
print(str16.istitle()) #returns True if first letter of each word is capital

str17 = "WORLD HEALTH ORGANIZATION !!!"
print(str17.isupper()) #returns True if all the letters of String is capital otherwise False

str18 = "WORLD HEALTH ORGANIZATION !!!"
print(str18.startswith("WORLD")) #returns True the String starts with particular String

str19 = "Java is better than Python"
print(str19.swapcase()) #converts lower case into upper and vice varca

str20 = "java is better than Python"
print(str20.title()) #capitalise each letter of the String


