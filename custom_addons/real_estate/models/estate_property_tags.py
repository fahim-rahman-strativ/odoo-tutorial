# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _description = "Estate Property Tags"


    name = fields.Char(required=True)
    # description = fields.Text()
    # postcode = fields.Char()
    # date_availability = fields.Date()
    # expected_price = fields.Float(required=True)
    # selling_price = fields.Float(readonly=True)
    # bedrooms = fields.Integer(default="2")
    # living_area = fields.Integer()
    # facades = fields.Integer()
    # garage = fields.Boolean()
    # garden = fields.Boolean()
    # garden_area = fields.Integer()
    # garden_orientation = fields.Selection(string='Garden-Orientation',
    #     selection=[('1', 'East'), ('2', 'West'), ('3', 'North'), ('4', 'South')],
    #     help="Orientation is used to point direction of the garden")
    # active = fields.Boolean(default=True)
    # status = fields.Selection(string='Status',
    #     selection=[('1', 'New'), ('2', 'Offer received'), ('3', 'Sold'), ('4', 'Cancelled'),('5','Offer accepted')], default="1")

