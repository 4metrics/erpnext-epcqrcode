import io
from segno import helpers

import frappe
from werkzeug.wrappers import Response

@frappe.whitelist()
def get_code():
  pName = frappe.request.args.get('name', default='', type=str)
  pIBAN = frappe.request.args.get('iban', default='', type=str)
  pAmount = frappe.request.args.get('amount', default=0, type=float)
  pText = frappe.request.args.get('text', default='', type=str)
  pReference = frappe.request.args.get('reference', default='', type=str)
  pBIC = frappe.request.args.get('bic', default='', type=str)
  pPurpose = frappe.request.args.get('purpose', default='', type=str)
  pScale = frappe.request.args.get('scale', default=4, type=int)
  pBorder = frappe.request.args.get('border', default=2, type=int)

  qrcode = helpers.make_epc_qr(name=pName, iban=pIBAN, amount=pAmount, text=pText, reference=pReference, bic=pBIC, purpose=pPurpose)
  buffer = io.BytesIO()
  qrcode.save(buffer, kind='png', scale=pScale, border=pBorder)
  buffer.seek(0)

  response = Response()
  response.mimetype = 'image/png'
  response.data = buffer.read()
  return response
