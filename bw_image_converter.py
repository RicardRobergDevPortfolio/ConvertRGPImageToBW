from PIL import Image
import os


def rgb_para_cinza(imagem_rgb):
    """Converte uma imagem RGB para escala de cinza usando a fórmula standard."""
    return imagem_rgb.convert("L")  # "L" é o modo para escala de cinza


def binarizar(imagem_cinza, limiar=127):
    """Binariza uma imagem em escala de cinza com um limiar."""
    return imagem_cinza.point(lambda p: 255 if p >= limiar else 0)


def processar_imagens():
    for arquivo in os.listdir():
        # Ignora arquivos já convertidos
        if "_convertido.jpg" in arquivo:
            continue

        # Verifica se o arquivo é uma imagem JPG
        if arquivo.lower().endswith(".jpg"):
            try:
                # Abre a imagem original
                imagem = Image.open(arquivo)

                # Converte para escala de cinza
                imagem_cinza = rgb_para_cinza(imagem)

                # Binariza a imagem
                imagem_binarizada = binarizar(imagem_cinza)

                # Salva a imagem binarizada com o sufixo _convertido
                nome_convertido = arquivo.replace(".jpg", "_convertido.jpg").replace(".JPG", "_convertido.jpg")
                imagem_binarizada.save(nome_convertido)

                print(f"Imagem {arquivo} convertida e salva como {nome_convertido}")

            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")


# Chama a função para processar as imagens da pasta atual
processar_imagens()
