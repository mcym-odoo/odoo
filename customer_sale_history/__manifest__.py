# © 2018-Today Ahorasoft (http://www.Ahorasoft.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Customer Sale History",

    'summary': """
        User can view the products which the customer have
        purchased just in a View easily.With the help of
        this module you can learn more about your Customers
        and their shopping habits.""",


    'description': """
        This module will help the user to see
        the shopping history of the customer Easily.
    """,

    'author': "Ahorasoft",
    'website': "http://www.ahorasoft.com",
    'license': "AGPL-3",

    'category': 'Sales',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'installable': True,
}