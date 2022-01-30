# Non part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Products cloud images',
    'category' : 'Sales',
    'depends' : ['sale', 'base'],
    'demo' : [],
    'author': 'Omega Software Service',
    'website': 'http://www.Vintage-Electronics.nl',
    'license': 'AGPL-3',

    'description': """
this app links many2many cloud images to products


""",
    'data': [
        'views/product_template.xml',
        'views/product_images.xml',
    ]
}
