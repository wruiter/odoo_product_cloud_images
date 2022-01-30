# -*- coding: utf-8 -*-
# Non part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

from odoo import fields, models


class ProductImages(models.Model):
    _name = 'product.images'
    _order = 'sequence'

    name = fields.Char('Name', required=True, translate=True)
    url = fields.Char('URL', required=True, translate=False)
    sequence = fields.Integer('Sequence', help="Determine the display order")
    product_ids = fields.Many2many('product.template', string='Images')

