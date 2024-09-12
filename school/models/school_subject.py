# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Relational Model'

    name = fields.Char(string='Name', required=True)
    credits_id = fields.Integer(string='Credits')
    max_students = fields.Integer(string='Maximum Students')
    active = fields.Boolean(string='Active', default=True)
    students_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')

    @api.constrains('students_ids')
    def _check_max_students(self):
        for record in self:
            if len(record.students_ids) > record.max_students:
                raise ValidationError("FULL SUBJECT")
