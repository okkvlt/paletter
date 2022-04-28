from io import BytesIO

from colorthief import ColorThief
from PIL import Image


class Paletter:
    """
    Inicializa a classe.
    
    Args:
        img: caminho para a imagem + nome da imagem [str]
    
    Ex:
        Paletter('images/pic.jpg')
    """
    
    def __init__(self, img: str):
        self.img = img

    def get_image(self) -> Image.Image:
        """
        Gera a nova imagem com a paleta de cores ao lado e retorna objeto do tipo Image.
        
        Returns:
            [Image.Image]: imagem pronta.
        """
        
        image = Image.open(self.img)
        x, y = image.size

        background = Image.new('RGB', (int(x + (x / 5)), int(y)), 'black')
        background.paste(image, (0, 0))

        with BytesIO() as i:
            image.save(i, 'JPEG')
            i.seek(0)

            colors = ColorThief(i)
            palette = colors.get_palette(color_count=5)

        for i, pal in enumerate(palette):
            width = int(x / 5)
            height = int(y / 5)

            color = Image.new('RGB', (width, height), pal)
            background.paste(color, (x, i*height))

        return background

    def get_byte(self) -> bytes:
        """
        Gera a nova imagem com a paleta de cores ao lado e retorna os bytes.
        
        Returns:
            [bytes]: imagem pronta.
        """
        
        img = self.get_image()
        
        bytes = BytesIO()
        img.save(bytes, "JPEG")
        
        bytes.seek(0)
        bytes = bytes.getvalue()
        
        return bytes