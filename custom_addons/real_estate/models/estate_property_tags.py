# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags"


    name = fields.Char(required=True)
    _sql_constraints = [
        ('tag_uniq', 'UNIQUE (name)', 'You can not have two tags with the same name !')
    ]

