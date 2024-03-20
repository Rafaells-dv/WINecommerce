import os
from dotenv import load_dotenv

load_dotenv()

credentials_h = {
            'client_id': 'Client_Id_3e8b0d2b528839d31913ae02f3982980e3fd1d74',
            'client_secret': 'Client_Secret_304d68cc3dea0e1c2347c5594e0382e359e486fc',
            'sandbox': True,
            'certificate': 'D:\Efi\certificados\homologacao-539200-win - homo_cert.pem'
        }

credentials_p = {
            'client_id': os.environ.get('CLIENT_ID_P'),
            'client_secret': os.environ.get('CLIENT_SECRET_P'),
            'sandbox': False,
            'certificate': os.environ.get('CERTIFICATE_P')
}
