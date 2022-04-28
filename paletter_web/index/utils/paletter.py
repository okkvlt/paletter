from io import BytesIO
from turtle import back

from cairo import HINT_STYLE_SLIGHT

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

        if x >= y:
            size_x = 5 + int(x) + 5  # 5 esquerda, 5 direita
            size_y = 5 + int(y) + 5 + int(y / 4) + 5  # 5 cima, 5 meio, 5 baixo
        else:
            # 5 esquerda, 5 meio, 5 direita
            size_x = 5 + int(x) + 5 + int(x / 4) + 5
            size_y = 5 + int(y) + 5  # 5 cima, 5 baixo

        size = (size_x, size_y)

        background = Image.new('RGB', size, 'white')
        background.paste(image, (5, 5))

        with BytesIO() as i:
            image.save(i, 'JPEG')
            i.seek(0)

            colors = ColorThief(i)
            palette = colors.get_palette(color_count=11)

        for i, color in enumerate(palette):
            """
            Cálculo matemático que indica
            os pixels de cada quadrado de
            cor na imagem resultante.
            """
            if x >= y:
                width = int((int(x) / 10) - 4.5)
                height = int(y / 4)

                pos_x = 7 + i * width + (i * 5)
                pos_y = 5 + int(y) + 5
            else:
                width = int(x / 4)
                height = int((int(y) / 10) - 4.5)

                pos_x = 5 + int(x) + 5
                pos_y = 7 + i * height + (i * 5)

            color_image = Image.new("RGB", (width, height), color)
            background.paste(color_image, (pos_x, pos_y))

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
