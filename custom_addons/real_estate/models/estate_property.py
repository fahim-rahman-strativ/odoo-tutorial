# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"


    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',
        selection=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')],
        help="Orientation is used to point direction of the garden")

