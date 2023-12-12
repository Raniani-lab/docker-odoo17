# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
class L10nLuMonthlyDeclarationWizard(models.TransientModel):
    _inherit = 'l10n.lu.monthly.declaration.wizard'

    def _get_fiduciary_matr_number(self):
        company = self.env.company
        return company.account_representative_id.l10n_lu_agent_matr_number or company.l10n_lu_official_social_security
