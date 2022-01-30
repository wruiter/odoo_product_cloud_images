# -*- coding: utf-8 -*-
#############################################################################
#
#    Neobis ICT Dienstverlening B.V.
#
#    Copyright (C) 2021-TODAY Neobis ICT Dienstverlening B.V.(<https://www.neobis.nl>)
#    Author: Walter Ruiter(<https://www.neobis.nl>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name' : 'Products cloud images',
    'version': '15.0.0.0.1',
    'category' : 'Sales',
    'depends' : ['sale', 'base'],
    'demo' : [],
    'author': 'Neobis ICT Dienstverlening B.V.',
    'website': 'http://www.neobis.nl',
    'license': 'AGPL-3',

    'description': """
this app links many2many cloud images to products.
Under salel/configuration there is a list of all the images each linked to one or more products.
On the product there is a notebookpage with all the related images.
""",
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/product_images.xml',
    ]
}
