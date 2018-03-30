# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DefaultProducTaxes(models.Model):
    _name = "product.taxes"
    _description = "Default multicompany taxes"

    tax_ids = fields.Many2many('account.tax', relation="sale_tax_ids_rel", string="Sale taxes", domain=[('type_tax_use', '=', 'sale')]) 
    supplier_tax_ids = fields.Many2many('account.tax', relation="purchase_tax_ids_rel", string="Supplier taxes", domain=[('type_tax_use', '=', 'purchase')]) 


class ProductDefaultTaxes(models.Model):
    _inherit = "product.template"

    taxes_id = fields.Many2many(compute="_set_taxes_default")
    supplier_taxes_id = fields.Many2many(compute="_set_taxes_default")

    company_id = fields.Many2one(default=False, compute="_set_company_default")

    @api.multi
    def _set_taxes_default(self):
        for prod in self:
            prod.taxes_id = self.env['product.taxes'].search([]).tax_ids
            prod.supplier_taxes_id = self.env['product.taxes'].search([]).supplier_tax_ids


    @api.multi
    def _set_company_default(self):
        for prod in self:
            prod.company_id = False


class PartnerCompanyDefault(models.Model):
    _inherit = "res.partner"

    company_id = fields.Many2one(default=False, compute="_set_company_default")

    @api.multi
    def _set_company_default(self):
        for prod in self:
            prod.company_id = False