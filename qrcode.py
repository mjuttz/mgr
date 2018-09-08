import pyqrcode
import secrets
import string
import hashlib
import unicodedata

class QrCode():
    def __init__(self,username):
        self.username = username
        self.code = self.generate_code()
        self.hash = self.create_hash()

    def generate_code(self):
        return ''.join(secrets.choice(string.ascii_letters + string.digits
            ) for _ in range(16)).encode('utf-8')

    def create_hash(self):
        return hashlib.sha224(self.code).hexdigest()

    def create_qr(self):
        qr_name = unicodedata.normalize('NFKD',self.username).replace(u'ł','l'
            ).encode('ascii','ignore').decode("utf-8",'ignore')
        return pyqrcode.create(self.code).png(qr_name + '.png', scale = 6)
