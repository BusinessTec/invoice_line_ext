# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm

class sales_type(osv.osv):
	_inherit = 'account.invoice.line'
	period_id = fields.many2one('account.period', string='Periodo',compute="_periodo", ondelete='cascade')
	
	@api.one
	@api.depends('invoice_id.period_id')
	def _periodo(self):
		self.period_id= self.invoice_id.period_id

