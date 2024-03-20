import os
from dotenv import load_dotenv

load_dotenv()

credentials_h = {
            'client_id': os.environ.get('CLIENT_ID_H'),
            'client_secret': os.environ.get('CLIENT_SECRET_H'),
            'sandbox': True,
            'certificate': os.environ.get('CERTIFICATE_H')
}

credentials_p = {
            'client_id': os.environ.get('CLIENT_ID_P'),
            'client_secret': os.environ.get('CLIENT_SECRET_P'),
            'sandbox': False,
            'certificate': os.environ.get('CERTIFICATE_P')
}
