# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Business Tec Systems S.A.(<http://businesstec.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'invoice_line_ext',
    'version': '1.0',
    'author': 'Business Tec Systems',
    'summary': 'Extending model for graph view with period_id, categ_id',
    'description': """
Invoice Line Extension
=======================
Creates a fields margin% and (read only) price for calculating product price to be used in pricelist
    """,
    'website': 'https://businesstec.net',
    'images': [],
    'depends': ['account', 'product'],
    'sequence': 18,
    'data': [
      
    ],
    'installable': True,
    'auto_install': False,
}
