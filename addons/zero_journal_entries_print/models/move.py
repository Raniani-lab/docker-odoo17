# -*- encoding: UTF-8 -*-
from odoo import api, fields, models, _
from odoo.tools.misc import formatLang, format_date, get_lang
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"



    def _get_report_je_filename(self):
        if any(move.is_invoice() for move in self):
            raise UserError(_("Only Journal Entries could be printed."))
        return 'Journal Entry - %s' % self.name
