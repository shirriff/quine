s="from PIL import Image,ImageFont,ImageDraw;f=ImageFont.load_default();i=image.new('RGB',(1200,100));d=ImageDraw.Draw(i);d.text((27,27),'s=%r'%s,font=f);d.text(27,62),s);i.save('quine.png')"
from PIL import Image,ImageFont,ImageDraw;f=ImageFont.load_default();i=Image.new('RGB',(1200,100));d=ImageDraw.Draw(i);d.text((27,27),'s=%r'%s,font=f);d.text((27,62),s);i.save('quine.png')
