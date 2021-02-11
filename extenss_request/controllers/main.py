from odoo import http
from odoo.http import request

class Lead(http.Controller):
    
    @http.route('/crm/ff/', website=True, auth='public')
    def crm_ff(self, **kw):
        #return "Prueba CRM"
        # ext_ffs = request.env['crm.lead'].sudo().search([])
        return request.render("extenss_request.crm_ff_template_page", {})
        #     'ext_ffs': ext_ffs
        # })