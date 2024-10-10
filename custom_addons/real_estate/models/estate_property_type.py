# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name desc"


    name = fields.Char(required=True)

    property_ids = fields.One2many("estate.property.type.list", "model_id")
    _sql_constraints = [
        ('type_uniq', 'UNIQUE (name)', 'You can not have two property types with the same name !')
    ]

class EstatePropertyTypeList(models.Model):
    _name = "estate.property.type.list"
    _description = "Estate Property Type List"

    model_id = fields.Many2one("estate.property.type")
    title = fields.Char()
    expected_price = fields.Float()
    status= fields.Char()
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")