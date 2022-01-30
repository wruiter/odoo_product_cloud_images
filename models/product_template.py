# -*- coding: utf-8 -*-
# Non part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    image_ids = fields.Many2many('product.images', string='Images')

