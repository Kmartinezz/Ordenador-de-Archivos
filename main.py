#Agregar siesque el archivo existe
import tkinter 
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os

messagebox.showinfo(title = "Selecciona Carpeta", message = "Selecciona la carpeta que quieres ordenar")

askFolder=askdirectory()

if __name__ == "__main__":
    for filename in os.listdir(askFolder):
        name, extension = os.path.splitext(askFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".JPG", ".PNG"]:
            if os.path.exists(askFolder + "/Image/"):
                pictureFolder = askFolder + "/Image/"
                os.rename(askFolder + "/" + filename, pictureFolder + filename)
            else:
                os.mkdir(askFolder + "/Image/")
                pictureFolder = askFolder + "/Image/"
                os.rename(askFolder + "/" + filename, pictureFolder + filename)


        if extension in [".xlsx", ".xls"]:
            if os.path.exists(askFolder + "/Excel/"):
                excelFolder = askFolder + "/Excel/"
                os.rename(askFolder + "/" + filename, excelFolder + filename)
            else:
                os.mkdir(askFolder + "/Excel/")
                excelFolder = askFolder + "/Excel/"
                os.rename(askFolder + "/" + filename, excelFolder + filename)

        
        if extension in [".pdf", ".PDF"]:
            if os.path.exists(askFolder + "/PDF/"):
                pdfFolder = askFolder + "/PDF/"
                os.rename(askFolder + "/" + filename, pdfFolder + filename)
            else:
                os.mkdir(askFolder + "/PDF/")
                pdfFolder = askFolder + "/PDF/"
                os.rename(askFolder + "/" + filename, pdfFolder + filename)

        
        if extension in [".docx", ".doc"]:
            if os.path.exists(askFolder + "/Word/"):
                wordFolder = askFolder + "/Word/"
                os.rename(askFolder + "/" + filename, wordFolder + filename)
            else:
                os.mkdir(askFolder + "/Word/")
                wordFolder = askFolder + "/Word/"
                os.rename(askFolder + "/" + filename, wordFolder + filename)


        if extension in [".pptx"]:
            if os.path.exists(askFolder + "/PPT/"):
                pptFolder = askFolder + "/PPT/"
                os.rename(askFolder + "/" + filename, pptFolder + filename)
            else:
                os.mkdir(askFolder + "/PPT/")
                pptFolder = askFolder + "/PPT/"
                os.rename(askFolder + "/" + filename, pptFolder + filename)


        if extension in [".exe"]:
            if os.path.exists(askFolder + "/Ejecutables/"):
                exeFolder = askFolder + "/Ejecutables/"
                os.rename(askFolder + "/" + filename, exeFolder + filename)
            else:
                os.mkdir(askFolder + "/Ejecutables/")
                exeFolder = askFolder + "/Ejecutables/"
                os.rename(askFolder + "/" + filename, exeFolder + filename)


        if extension in [".rar", ".zip"]:
            if os.path.exists(askFolder + "/RAR/"):
                rarFolder = askFolder + "/RAR/"
                os.rename(askFolder + "/" + filename, rarFolder + filename)
            else:
                os.mkdir(askFolder + "/RAR/")
                rarFolder = askFolder + "/RAR/"
                os.rename(askFolder + "/" + filename, rarFolder + filename)


        if extension in [".txt"]:
            if os.path.exists(askFolder + "/Text/"):
                textFolder = askFolder + "/Text/"
                os.rename(askFolder + "/" + filename, textFolder + filename)    
            else:
                os.mkdir(askFolder + "/Text/")
                textFolder = askFolder + "/Text/"
                os.rename(askFolder + "/" + filename, textFolder + filename) 
