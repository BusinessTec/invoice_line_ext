# -*- coding: utf-8 -*- 
from openerp import models, fields, api

class invoice_line(models.Model):
        _inherit = 'account.invoice.line'
        period_id_ref = fields.Many2one('account.period', string='Periodo',compute="_periodo",readonly=True, store=True)


        @api.one
        @api.depends('invoice_id.period_id')
        def _periodo(self):
                self.period_id_ref= self.invoice_id.period_id
