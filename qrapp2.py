from pyzbar.pyzbar import decode
from PIL import Image 

def lerQR():
    
    d = decode(Image.open("Foto.png"))

    print(d[0].data.decode())  
    
    return d
