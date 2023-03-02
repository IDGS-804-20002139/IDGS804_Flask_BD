from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

from wtforms import validators

class UserForm(Form):
    id=IntegerField('id',[validators.number_range(min=1,max=20,message='valor no valido')])
    nombre=StringField('nombre',
                       [validators.DataRequired(message='valor no valido')])
    apaterno=StringField('apaterno',
                         [validators.DataRequired(message='valor no valido')])
    email=EmailField('correo',
                     [validators.DataRequired(message='valor no valido')],
                     validators.Email(message='Ingresa un correo valido'))
    
