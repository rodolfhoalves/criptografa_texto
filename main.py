from cryptography.fernet import Fernet

class cripto:


    def gera_chave():

        chave_gerada = Fernet.generate_key()
        chave_gerada_convetida_para_string = chave_gerada.decode('utf-8')
        print("CHAVE GERADA: ", chave_gerada_convetida_para_string)


    def criptografar(chave, texto_claro):

        cipher_suite = Fernet(chave)
        encoded_text = bytes(texto_claro, 'utf-8') # Encode to bytes utf-8
        encrypted_text = cipher_suite.encrypt(encoded_text) #required to be bytes

        print("TEXTO CRIPTOGRAFADO: ", encrypted_text.decode("utf-8"))


    def descriptografar(chave, texto_criptografado):
        
        encoded_text = bytes(texto_criptografado, 'utf-8')
        cipher_suite = Fernet(chave)
        ciphered_text = encoded_text
        unciphered_text = (cipher_suite.decrypt(ciphered_text))

        texto_claro = bytes(unciphered_text).decode("utf-8") # convert to string

        print(texto_claro)





if __name__ == "__main__":

    # Gera chave
    cripto.gera_chave() 

    cripto.criptografar("cu4tD7nZm54wDhSQ7Birp-nwElORiTkD51MnxUuL7yc=", "oi")

    cripto.descriptografar("cu4tD7nZm54wDhSQ7Birp-nwElORiTkD51MnxUuL7yc=",
     "gAAAAABgZoQFBuCWiOi2EI4uvQ-sY4tc3FIfbl1VFjtsHxIr0nOwH9F3EsTYapjTMev7MM9s-mMxuyNPJ9TEraOUr4aEvaAyoQ=="
    )

