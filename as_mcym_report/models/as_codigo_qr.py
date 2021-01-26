from . import amount_to_text_es
from odoo import api, models, fields,_
import qrcode
from bs4 import BeautifulSoup
import tempfile
import base64
from io import StringIO
import io
import logging
_logger = logging.getLogger(__name__)

class AcoountMove(models.Model):
    _inherit = "account.move"    

    def get_qrcode(self,cadena_qr): 
        try:
            qr_img = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=0)
            qr_img.add_data(cadena_qr)
            qr_img.make(fit=True)
            img = qr_img.make_image()
            # buffer = StringIO()
            buffer = io.BytesIO()
            img.save(buffer)
            qr_img = base64.b64encode(buffer.getvalue())
            return qr_img
        except:
            raise UserError(_('No se puedo generar el codigo QR'))     
