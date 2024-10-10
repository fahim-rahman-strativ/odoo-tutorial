# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags"
    _order = "name desc"


    name = fields.Char(required=True)
    color = fields.Integer()
    _sql_constraints = [
        ('tag_uniq', 'UNIQUE (name)', 'You can not have two tags with the same name !')
    ]

