from django import forms
from .models import usuarios,tipos_de_usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        # Los campos que necesita en el formulario
        fields = ['correo', 'nombre', 'telefono', 'contraseña', 'id_tipo_usuario','id_plan']
        
class tipos_de_usuariosForm(forms.ModelForm):
    class Meta:
        model = tipos_de_usuarios
        # Los campos que necesita en el formulario
        fields = ['nombre']
        
