from odoo import models, fields, api


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        res = super(EstateProperty).action_sold()
