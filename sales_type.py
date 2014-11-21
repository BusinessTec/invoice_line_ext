# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm

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

