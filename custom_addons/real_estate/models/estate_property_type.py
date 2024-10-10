# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"


    name = fields.Char(required=True)
    _sql_constraints = [
        ('type_uniq', 'UNIQUE (name)', 'You can not have two property types with the same name !')
    ]