from odoo import api,fields,models

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Hospital Patient"

    name=fields.Char(string='Name',required=True)
    age=fields.Integer(string='Age')
    gender=fields.Selection([
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER'),
    ],required=True,default='male')
    note=fields.Text(string='Desciption')