from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Carrera, Usuario, Instituto, Materia, MateriaCorrelativa

class institutoForms(forms.ModelForm):
      nombre_instituto = forms.CharField(max_length=30)
      email = forms.CharField(max_length=20)
      class Meta:
            model = Instituto
            fields = (
            'nombre_instituto',
            'email_instituto',
            'direccion',
            'localidad',
            'ciudad',
            )


class carreraForm(forms.ModelForm):
      nombre_carrera = forms.CharField( max_length=100)
      num_resolucion = forms.CharField(max_length=100)
      class Meta:
        model = Carrera
        fields =(
          'nombre_carrera',
          'num_resolucion',
          'duracion_carrera',
          'instituto',

        )

class materiaForm(forms.ModelForm):
      nombre_materia = forms.CharField( max_length=100)
      class Meta:
        model = Materia
        fields =(
          'nombre_materia',
          'carrera',
          'profesor'

        )

class usuarios_materiaForm(forms.ModelForm):
      nombre_materia = forms.CharField( max_length=100)
      class Meta:
        model = Materia
        fields =(
          'nombre_materia',
          'carrera',
          'profesor'

        )

class materiaCorrelativaForm(forms.ModelForm):
      nombre_materiaCorrelativa = forms.CharField( max_length=100)
      class Meta:
        model = MateriaCorrelativa
        fields =(
          'materia',
          'materia_correlativa'
        )

class registri_user_form(UserCreationForm):
    email = forms.EmailField(required=True)
    dni = forms.CharField(max_length=15)   

    password1 = None
    password2 = None

    class Meta:
        model = Usuario
        fields = ['email', 'nombres', 'apellidos', 'dni', 'groups', 'carrera']

    def clean(self):
        password = Usuario.objects.make_random_password(length=10,allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        self.cleaned_data['password1'] = password
        self.cleaned_data['password2'] = password

        return super().clean()

    def save(self, commit=True):
        Usuario = super().save(commit=False)

        
        Usuario.save()
        return Usuario



class profile_students_form(forms.ModelForm):   
  class Meta:
    model = Usuario
    fields = (
      'username',
      'nombres',
      'apellidos',
      'fecha_nac',
      'dni',
      'direccion',
      'localidad',
      'ciudad',
      'nacionalidad',
      'telefono_1',
      'telefono_2',
      'estado_civil',
      'sexo',
      

    )
    
class edit_profile_form(forms.ModelForm):   
  class Meta:
    model = Usuario
    fields = (
      'username',
      'email',
      'nombres',
      'apellidos',
      'fecha_nac',
      'dni',
      'direccion',
      'localidad',
      'ciudad',
      'nacionalidad',
      'telefono_1',
      'telefono_2',
      'estado_civil',
      'sexo',
      

    )

############################################################
