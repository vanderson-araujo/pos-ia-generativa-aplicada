"""
Pillow trabalha com imagens.
Instale com:
pip install pillow
"""

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Instale a biblioteca com: pip install pillow")
else:
    imagem = Image.new("RGB", (300, 120), color="white")
    desenho = ImageDraw.Draw(imagem)
    desenho.rectangle((20, 20, 280, 100), outline="black", width=3)
    desenho.text((40, 50), "Estudando Python", fill="black")
    imagem.save("imagem_exemplo.png")
    print("Imagem criada: imagem_exemplo.png")

