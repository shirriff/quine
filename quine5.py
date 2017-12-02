a="from PIL import Image,ImageDraw as D;i=Image.new('RGB',(1100,100));d=D.Draw(i);[d.ellipse((n,(n*7%120)-8,n+8,n*7%120),'white')for n in range(-11,1100,2)]"
from PIL import Image,ImageDraw as D;i=Image.new('RGB',(1100,100));d=D.Draw(i);[d.ellipse((n,(n*7%120)-8,n+8,n*7%120),'white')for n in range(-11,1100,2)]
b="l=91;d.rectangle((l,29,1031, 64),'black'); d.text((l, 28),'a=%r'%a); d.text((l, 37),a); d.text((l,46),'b=%r'%b); d.text((l, 55), b); i.save('quine5.png')"
l=91;d.rectangle((l,29,1031, 64),'black'); d.text((l, 28),'a=%r'%a); d.text((l, 37),a); d.text((l,46),'b=%r'%b); d.text((l, 55), b); i.save('quine5.png')
