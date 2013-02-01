##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Standard Cost Accounting',
    'version': '0.1',
    'author': 'Openstone, Oliver',
    'website': 'http://openerp.com - http://www.openstone.cn',
    'description': """
标准成本法下，采购价格差异以及生产成本差异记账。
=====================================================================================================================

略""",
    'images': ['images/account_standard_costing.jpeg'],
    'depends': ['product', 'purchase'],
    'category': 'Accounting & Finance',
    'demo': [],
    'data': ['product_view.xml',],
    'auto_install': False,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
