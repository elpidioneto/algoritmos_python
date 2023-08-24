import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg",".jpeg"],
    "planilhas": [".xlsx",".csv",".xls"],
    "pdfs": [".pdf"],
    "json": [".json"],
    "apks": [".apk"],
    "videos": [".mp4",".mkv",".webm"],
    "zips": [".zip",".rar",".7z"],
    "executaveis": [".exe"],
    "certificados": [".pfx"],
    "iso's": [".iso"],
    "mapas_mentais": [".xmind"],
    "documentos": [".doc",".docx",".odt"],
    "SQL": [".sql"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")