from cryptography.fernet import Fernet
#
#
# def encrypt_password(message):
#     global key, crypter, Encryption
#     key = Fernet.generate_key()
#     crypter = Fernet(key)
#     print(crypter)
#     msg = message.encode()
#     print(msg)
#     Encryption = crypter.encrypt(msg)
#     print(Encryption )
#     Encrypted = str(Encryption, 'utf8')
#     print("Encrypted Password is : "+ str(Encrypted))
#
# def decrypt_password():
#     key = Fernet.generate_key()
#     crypter = Fernet(key)
#     print(crypter)
#     Decryption = crypter.decrypt("gAAAAABhJGeKJc0WqmxiV9_QaHdvL52wplfd4vogmmPsmrc0nlELCjNuYixcSw4mPWAkkmkp1U1KKQ_HmI2h4uS9BtYAs2Xe0TR8q8eg1NDVEVqYv_nClfU=")
#     print(Decryption)
#     Decrypted = str(Decryption,'utf8')
#     print(Decrypted)
#     print("Decrypted Password is : " + str(Decrypted))
#
#
# # decrypt_password("gAAAAABhJL6oBnVNe04VhnA8Xv_rS2E4gl5nSccnQs9Mt8GVB1sQZ9QcXSEABRFRJIwO8q72VOuaVDxWK20jvI348C833PjFGg==")
# # encrypt_password("Hello")
# decrypt_password()
#
#
#
#
#

with open("key.key","rb") as f:
    key=f.read()
f = Fernet(key)

with open('enc_text.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('decrypt.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)