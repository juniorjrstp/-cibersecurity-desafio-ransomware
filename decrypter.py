import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt.ransowaretroll"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de criptografia
chave = b"testeransonwares"
aes = pyaes.AESModeOfOperationCTR(chave)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## salvar o arquivo criptografado
new_file = "teste.txt"
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
