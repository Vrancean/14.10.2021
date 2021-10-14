a='A B C D E F G H I J K L M N O P Q R S T U V W X Y'
x=''
y=''
z=''
for i in a:
    b=chr(ord(i)+1)
    x+=b
    c=x.replace('!',' ')
    d=c.replace('[','A')
print('sirul:',d)
y=d
for i in d:
    v=d.replace('Z','A')
print(v)
z=v
q=v.replace(' ','-')
print(q)