{
    'name': 'Financial factoring',
    'version': '1.0',
    'summary': 'Definition of the Financial factoring',
    'description': 'Definition of the Financial factoring',
    'author': 'Mastermind Software Services',
    'depends': ['base','mail','extenss_credit','board','sale'],
    'application': True,
    'website': 'https://www.mss.mx',
    'category': 'Uncategorized',
    'data': [
        'security/extenss_ff_security.xml',
        'security/ir.model.access.csv',
        'views/credit_ff_view.xml',
        'views/credit_ff_lines_active_view.xml',
        'views/credit_ff_dispersion_view.xml',
        'views/credit_ff_initial_pay_view.xml',
        'views/credit_ff_pre_notice_view.xml',
        # 'views/credit_dn_early_set_view.xml',
        # 'views/credit_dn_adv_pay_view.xml',
        # 'views/credit_dn_moras_view.xml',
        # 'views/credit_dn_acct_portfolio_view.xml',
        # 'views/credit_dn_payment_balance_view.xml',
        # 'views/credit_dn_condonation_view.xml',
        # 'views/credit_dn_conciliation_view.xml',
        # 'views/credit_dn_collection_view.xml',
        ],
}