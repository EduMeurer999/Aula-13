import os
import zipfile
os.chdir(os.getcwd()+"\\AulaPython\\Arquivos\\Documentos")
zip = zipfile.ZipFile('varios.zip')
print(zip.namelist())
fileInfo = zip.getinfo('Novo(a) Texto OpenDocument.odt')
print(fileInfo.file_size/1024)
newZip = zipfile.ZipFile('variosPdf.zip', 'w')
newZip.write('Aula 12 Diretorios Arquivos.pdf', 'Aula 13 Zip Data e Hora.pdf')
newZip.close()
zip.extract('python.odt')