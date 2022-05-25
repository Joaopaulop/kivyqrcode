from pyzbar.pyzbar import decode
from PIL import Image 

d = decode(Image.open("frame.png"))

print(d[0].data.decode())