import base64
import io
from PIL import ImageTk, Image
import static
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3+
    import tkinter as tk


def buildAndReturnLabel(base64i,typeimg):

    #print(base64i)
    #b=base64i+'' #je transforme la base64 en string
    #c=b.split(",") #je split la data des infos
    #d=c[1] #la data se situe derriere la virgule
    received = base64.b64decode(base64i) #je la decode
    infos=typeimg #typeimg renvoi l'extension (le format)

    img = Image.open(io.BytesIO(received)) #on ouvre l'image pour la traiter

    if "png" in infos: #on l'enregistre dans le format correspondant a typeimg
        imgConstruite="static/images/tmp/test.png"
        img.save(imgConstruite)
    else:
        imgConstruite = "static/images/tmp/test.png"
        img.save(imgConstruite)

    return imgConstruite