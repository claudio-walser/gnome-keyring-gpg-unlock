import os
import gnupg



class GpgSecret(object):

  gpg = gnupg.GPG()
  outputEncoding = 'utf-8'

  def decrypt(self, file: str) -> str:
    if not os.path.exists(file):
      raise Exception(f'File {file} not found. No such file or directory')
    return self.gpg.decrypt_file(file).data.decode(self.outputEncoding)


  def encrypt(self, message:str, public_key: str, file: str) -> bool:
    encrypted = str(self.gpg.encrypt(message, public_key))
    del message # remove message from memory

    with open(file, 'w') as file:  # Use file to refer to the file object
      file.write(encrypted)
      file.close()

    return True