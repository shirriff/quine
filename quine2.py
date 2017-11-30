a="from PIL import Image,ImageDraw;i=Image.new('RGB',(1200,100));d=ImageDraw.Draw(i);"
b="for n in range(1,1180,13): d.arc((n,n%26,n+37,99-n%26),0,360,fill='white')"
c="l=260;d.rectangle((l,11,986,90),fill='black');d.text((l,10),'a=%r'%a);d.text((l,20),'b=%r'%b);d.text((l,30),'c=%r'%c)"
e="d.text((l,40),'e=%r'%e);d.text((l,50),a);d.text((l,60),b);d.text((l,70),c);d.text((l,80),e);i.save('q.png')"
from PIL import Image,ImageDraw;i=Image.new('RGB',(1200,100));d=ImageDraw.Draw(i);
for n in range(1,1180,13): d.arc((n,n%26,n+37,99-n%26),0,360,fill='white')
l=260;d.rectangle((l,11,986,90),fill='black');d.text((l,10),'a=%r'%a);d.text((l,20),'b=%r'%b);d.text((l,30),'c=%r'%c)
d.text((l,40),'e=%r'%e);d.text((l,50),a);d.text((l,60),b);d.text((l,70),c);d.text((l,80),e);i.save('q.png')
