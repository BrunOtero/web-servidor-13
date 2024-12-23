from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class NameAndEmailForm(FlaskForm):
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    email = StringField('Qual é o seu email (Envio de notificação do novo usuário)?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')