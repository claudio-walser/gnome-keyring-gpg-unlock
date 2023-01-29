import os
import gnupg


class Secret(object):

  gpg = gnupg.GPG()
  outputEncoding = 'utf-8'

  def decrypt(self, file: str) -> str:
    if not os.path.exists(file):
      raise Exception(f'File {file} not found. No such file or directory')
    decrypted = self.gpg.decrypt_file(file)

    return decrypted.data.decode(self.outputEncoding)
