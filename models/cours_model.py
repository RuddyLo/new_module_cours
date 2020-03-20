#-*- coding:utf-8 -*-

from openerp import models,fields, api
class openacademy_course (models.Model) :
	name= fields.Char(string="Libellé",required="True")
	state= fields.Selection([
		('draft','Draft'),
		('confirmed','Confirmed')],default='draft')
	description= fields.Text(string='Description', readonly=True,states= {'draft':[('readonly',False)]})
	responsible_id= fields.Many2one("res_partner",string="Responsable")
#erreurs