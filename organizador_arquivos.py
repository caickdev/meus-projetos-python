import os
import shutil
from datetime import datetime

def organizar_pasta(diretorio):
    """
    Organiza arquivos na pasta 'diretorio' movendo-os para subpastas por extensão.
    Ex: .pdf → Documentos/, .jpg/.png → Imagens/, .docx → Word/, etc.
    """
    if not os.path.exists(diretorio):
        print(f"Pasta {diretorio} não existe!")
        return

    categorias = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.csv', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Outros': []  # o que não cair nas outras
    }

    for categoria in categorias:
        pasta_destino = os.path.join(diretorio, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

    arquivos_movidos = 0
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()
            movido = False
            for categoria, exts in categorias.items():
                if extensao in exts:
                    destino = os.path.join(diretorio, categoria, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {categoria}/")
                    arquivos_movidos += 1
                    movido = True
                    break
            if not movido:
                destino = os.path.join(diretorio, 'Outros', arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} → Outros/")
                arquivos_movidos += 1

    print(f"\nOrganização concluída! {arquivos_movidos} arquivos movidos.")

# Teste: mude para uma pasta de teste sua (ex: Downloads ou uma pasta vazia que você crie)
pasta_teste = r"D:\TesteOrganizacao"  # <-- MUDE PARA UMA PASTA REAL SUA (crie uma vazia e coloque alguns arquivos de teste)
organizar_pasta(pasta_teste)