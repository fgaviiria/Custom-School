# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Data'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birthdate', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', readonly=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = (fields.Date.today() - record.birth_date).days // 365
            else:
                record.age = 0

    @api.constrains('subject_ids')
    def _check_subject(self):
        subjects = self.subject_ids
        for record in subjects:
            if len(record.students_ids) > record.max_students:
                raise ValidationError(f"FULL SUBJECT {record.name}")
