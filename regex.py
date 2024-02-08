#REGULAR EXPRESSION
import re
dir(re)
a = "Today is monday"
b = "shreyaprakash@gmail.com"
c = "hello"
d = "xyz,yz,xyzz,xyyz,xxzzy,zyz,xxy"
e = re.search(r"^xyz",d)
print(e)
f = re.search(r"xxy$",d)
print(f)

chat1='you ask lot of question 1232454567, abc@xyz.com 345267654'
chat2='here it is:(123)-567-8912, abc@xyz.com'
chat3='yes, phone:1234567891 email:abc@xyz.com'
pattern='\d{10}'
matches=re.findall(pattern,chat1)
print(matches)

pattern='\(\d{3}\)'
match =re.findall(pattern,chat2)
print(match)

pattern="[a-zA-Z]@[a-zA-Z]{3}.[a-z]{3}"
matches=re.findall(pattern,chat2)
print(matches)
