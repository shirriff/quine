a="from PIL import Image,ImageDraw;i=Image.new('RGB',(1200,100));d=ImageDraw.Draw(i);[d.arc((n+7,n%26,n+46,100-n%26),0,360,fill='white') for n in range(2,1150,13)]"
from PIL import Image,ImageDraw;i=Image.new('RGB',(1200,100));d=ImageDraw.Draw(i);[d.arc((n+7,n%26,n+46,100-n%26),0,360,fill='white') for n in range(2,1150,13)]
b="l=91;d.rectangle((l, 32,1070, 67), fill='black'); d.text((l, 31),'a=%r'%a); d.text((l, 40),a); d.text((l,49),'b=%r'%b); d.text((l, 58), b); i.save('quine4.png')"
l=91;d.rectangle((l, 32,1070, 67), fill='black'); d.text((l, 31),'a=%r'%a); d.text((l, 40),a); d.text((l,49),'b=%r'%b); d.text((l, 58), b); i.save('quine4.png')
