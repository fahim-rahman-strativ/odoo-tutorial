# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from tokenize import String

from docopt import Required

from odoo import fields, models
from odoo.exceptions import ValidationError




class EstatePropertyOffers(models.Model):
    _name = "estate.property.offers"
    _description = "Estate Property Offers"
    _order = "price desc"


    price = fields.Float()
    status = fields.Selection(string='Status',
         selection=[('1', 'Accepted'), ('2', 'Refused')])
    partner_id = fields.Many2one(comodel_name="res.partner", Required = True)
    property_id = fields.Many2one(comodel_name="estate.property", String="Offers", Required = True)
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price >= 0 )',
         'Price must be a positive amount.')]

    def accept_offer(self):
        self.status = "1"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
        # return True

    def refuse_offer(self):
        for record in self:
                record.status = "2"
        return True



