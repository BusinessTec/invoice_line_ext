# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm

class sales_type(osv.osv):
	_inherit = 'account.invoice.line'
	period_id_ref = fields.many2one('account.period', string='Periodo',compute="_periodo",readonly=True)
	
	@api.one
	@api.depends('invoice_id.period_id')
	def _periodo(self):
		self.period_id_ref= self.invoice_id.period_id

