# -*- coding: utf-8 -*-
from odoo import fields, models, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class QRCodeGenerator(models.Model):
    _name = "popup.wizardz"
    _description = "QR Code Generator Wizard"

    purchase_limit_amount = fields.Integer('Purchase Limit Amount')

