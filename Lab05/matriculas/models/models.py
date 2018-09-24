# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class matriculas(models.Model):
#     _name = 'matriculas.matriculas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Alumno(models.Model):
    _name = 'matriculas.alumno'

    name = fields.Char(string="Nombre y apellidos")
    edad = fields.Integer(string="Edad")
    localidad = fields.Char(string="Localidad")
    provincia = fields.Char(string="Provincia")
    email = fields.Char(String="Email")
    matriculas_ids = fields.One2many(
        'matriculas.matricula', 'alumno_id', string="Matrículas del alumno")


class Curso(models.Model):
    _name = 'matriculas.curso'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    duracion = fields.Integer(string="Horas de duración")
    area_ids = fields.Many2many('matriculas.area')


class Matricula(models.Model):
    _name = 'matriculas.matricula'

    name = fields.Char()
    fecha_matricula = fields.Date(string="Fecha de Matrícula")
    curso_id = fields.Many2one('matriculas.curso', string="Curso")
    alumno_id = fields.Many2one('matriculas.alumno', string="Alumno")


class Area(models.Model):
    _name = "matriculas.area"

    name = fields.Char(String="Nombre")
    description = fields.Text(string="Descripción")
    encargado = fields.Text(string="Jefe de área")
    curso_ids = fields.Many2many('matriculas.curso')
