# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from pickle import FALSE

from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"


    name = fields.Char(required=True)
    description = fields.Text()
    property_type_id = fields.Many2one("estate.property.type", string="Property type")
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True,
                              default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, tracking=True)
    tag_ids = fields.Many2many(comodel_name="estate.property.tags")
    offer_ids = fields.One2many("estate.property.offers", "property_id", string= "Offers")

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
    garden_orientation = fields.Selection(string='Garden-Orientation',
        selection=[('east', 'East'), ('west', 'West'), ('north', 'North'), ('south', 'South')],
        help="Orientation is used to point direction of the garden")
    active = fields.Boolean(default=True)
    status = fields.Selection(string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer received'), ('offer_accepted', 'Offer accepted'), ('cancelled', 'Cancelled'),('sold','Sold')], default="new")
    total_area = fields.Float(compute='_compute_total', readonly=True)
    # best_price = fields.Float(compute='_compute_best', readonly=True)

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0 )','Price must be a positive amount.'),
        ('check_selling_price', 'CHECK(selling_price >= 0 )', 'Price must be a positive amount.')
    ]

    # ('check_minimum_selling_price', 'CHECK(selling_price >= (0.9*expected_price)',
    #  'Selling price must be a positive amount.'),
    # AND selling_price >= 0 AND offer_ids.price >= 0

    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            record.total_area = record.living_area
            if record.garden :
                record.total_area = record.living_area+record.garden_area

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.constrains('expected_price', 'selling_price')
    def _check_date_end(self):
        for record in self:
            if record.selling_price < (record.expected_price*0.9):
                raise ValidationError("Price must be 90 percent of expected price or higher")

    def action_sold(self):
        for record in self:
            if record.status =="cancelled":
                raise ValidationError("Cancelled properties can't be sold.")
            else:
                record.status = "sold"
        return True

    def action_cancel(self):
        for record in self:
            if record.status == "sold":
                raise ValidationError("Sold properties can't be cancelled.")
            else:
                record.status = "cancelled"
        return True

    # @api.model
    # def ondelete(self, vals):
    #     if self.env['estate.property'].browse(vals['status']) != "new":
    #         raise UserError("Can't delete this property!")
    #     elif self.env['estate.property'].browse(vals['status']) != "cancelled":
    #         raise UserError("Can't delete this property!")
    #     else:
    #         return True

    @api.ondelete(at_uninstall=False)
    def _unlink_if_new_or_cancelled(self):
        if self.status != "new" or self.status != "cancelled":
            raise UserError("Can't delete this property")

    # @api.model
    # def create(self):
    #     if self.offer_ids:
    #         self.status = "offer_received"

    # def accept_offer(self):
    #     for record in self:
    #             record.selling_price = record.offer_ids.price
    #     return True


    # @api.depends('offer_ids.price')
    # def _compute_best(self):
    #     for record in self:
    #         record.best_price = record.offer_ids
    #         if record.best_price < record.offer_ids:
    #             record.best_price = record.offer_ids
    #             return





