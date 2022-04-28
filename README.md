# Paletter

Biblioteca python criada para gerar montagem com paleta de cores a partir de imagens.

## ▪ Requisitos

- Pillow; `pip3 install pillow`
- Colorthief. `pip3 install colorthief`

## ▪ Como utilizar

Para utilizar a biblioteca, basta importá-la para seu projeto e inicializar uma "sessão" com a classe `Paletter()`.

### ▪ Importação

```python
from paletter import Paletter
```

### ▪ Criação de "Sessão"

```python
img = Paletter("path/to/image.jpg")
```

## ▪ Funções

### ▪ `get_bytes()`

Essa função serve para retornar os bytes da imagem montada com a paleta de cores. Não é necessária a passagem de argumentos.

```python
bytes = img.get_bytes()
```

É possível converter os bytes para _BytesIO_ utilizando a biblioteca _io_.

```python
from io import BytesIO
from paletter import Paletter


img = Paletter("path/to/image.jpg")
bytes = img.get_bytes()
bytesio = BytesIO(bytes)
```

Essa conversão pode ser útil para utilizar a imagem como arquivo em outra função sem que a imagem seja salva.

### ▪ `get_image()`

Essa função também serve para retornar a imagem montada com a paleta de cores, no entanto, diferentemente da função `get_bytes()`, o retorno desta é do tipo `Image.Image`.

```python
imagem = img.get_image()
```

Essa função é útil para, por exemplo, manipular a imagem de outras maneiras com a biblioteca Pillow.

## ▪ Demonstração

Visando demonstrar facilmente e visualmente o funcionamento da biblioteca, criei um simples aplicativo web em Django. Para iniciar esta aplicação e testá-la, é preciso executar o arquivo `manage.py` dentro da pasta "paletter_web".

### ▪ Inicialização da Aplicação Web:
```console
$ python3 manage.py runserver
```

Tendo inicializado a aplicação, simplesmente navegue para o endereço `127.0.0.1:8000` em seu navegador.

### ▪ Envio(s):
<div align="center">
  <img src="https://i.imgur.com/EY20I1h.png" width="800"></img>
</div>

### ▪ Retorno(s):
<div align="center">
  <img src="https://i.imgur.com/gtY0NAe.png" width="800"></img>
  <img src="https://i.imgur.com/oazPwpR.png" width="800"></img>
</div>

