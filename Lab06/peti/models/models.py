# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class peti(models.Model):
#     _name = 'peti.peti'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Proyecto(models.Model):
    _name = 'petis.proyecto'

    name = fields.Char(string="Nombre del proyecto")
    duracion = fields.Integer(string="Duración en dias")
    fecha_inicio = fields.Date(string="Fecha de inicio")
    encargado = fields.Text(string="Descripción")
    detalles_ids = fields.One2many('petis.detalle', 'proyecto_id', string="Detalle de las actividades")

class Actividad(models.Model):
    _name = 'petis.actividad'

    name = fields.Char(string="Nombre de la actividad")
    description = fields.Text(string="Descripción")
    duracion = fields.Integer(string="Duración en horas")
    prioridad = fields.Selection([('a', 'Alta prioridad'), ('m', 'Mediana Prioridad'), ('b', 'Baja Prioridad')], string='Prioridad')

class Detalle(models.Model):
    _name = 'petis.detalle'

    name = fields.Char()
    fecha_limite = fields.Date(string="Fecha límite de la actividad")
    fecha_realizada = fields.Date(string="Fecha en la que se realizó la actividad")
    usuario = fields.Char(string="Nombre del usuario")
    description = fields.Text(string="Descripción")
    estado = fields.Selection( [('0', 'Por hacer'), ('1', 'Terminado')])
    archivo = fields.Binary(string="Suba el archivo correspondiente")
    actividad_id = fields.Many2one('petis.actividad', string="Actividad")
    proyecto_id = fields.Many2one('petis.proyecto', string="Proyecto")
