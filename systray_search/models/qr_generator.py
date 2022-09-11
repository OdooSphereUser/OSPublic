# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def name_get(self):
        if self._context.get('show_short'):
            new_res = []
            for category in self:
                name = category.name
                new_res.append((category.id, name))
            return new_res
        else:
            return super(ProductCategory, self).name_get()