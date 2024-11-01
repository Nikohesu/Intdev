from django import forms
from .models import usuarios,tipos_de_usuarios,tipos_de_planes

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
        
class tipos_de_planform(forms.ModelForm):
    class Meta:
        model = tipos_de_planes
        # Los campos que necesita en el formulario
        fields = ['tipo_de_plan',"duracion_meses","valor","id_pago"]
        