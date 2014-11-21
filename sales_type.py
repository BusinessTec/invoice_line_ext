# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class sales_type(osv.osv):
	_inherit = 'sale.order'
    	_columns = {
    	          	'sales_type': fields.selection([
            ('wholesale', 'Distribuidores'),
            ('consignment', 'Consignación'),
            ('retail', 'Minoristas'),
            ('spares', 'Repuestos'),      
            ('other', 'Otro'),
            ], 'Tipo de Ventas', select=True, required=True),
    	}

