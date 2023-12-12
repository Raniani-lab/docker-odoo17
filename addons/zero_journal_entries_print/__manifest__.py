# -*- encoding: UTF-8 -*-
{
    'name': 'Print Journal Entries (PDF)',
    'version': '7.1.0',
     "author": 'Zero Systems',
     "company": 'Zero for Information Systems',
     "website": "https://erpzero.com",
     "email": "sales@erpzero.com",
    'live_test_url': 'https://youtu.be/uFuRsQfYNsk',
    'category': 'Accounting',
    'sequence': 1,
    'summary': 'Print Journal Entries PDF',
    'description': """
    this module use for print journal Entries in PDF report"
    """,
    'depends': ['account'],
    'data': [
        'report/report.xml'
    ],
    "price": 0.00,
    "currency": 'EUR',
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/journal.png'],
}
