from django.shortcuts import render, get_object_or_404, redirect
from .models import usuarios,tipos_de_usuarios,tipos_de_planes
from .forms import UsuarioForm,tipos_de_usuariosForm,tipos_de_planform

def usuario_add(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuario_form.html', {'form': form})

def usuario_list(request):
    usuario = usuarios.objects.all()
    return render(request, 'usuario_list.html', {'usuario': usuario})
def usuario_edit(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_form.html', {'form': form})

def usuario_delete(request, pk):
    usuario = get_object_or_404(usuarios, pk=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuarios': usuario})

def tipo_de_usuario_add(request):
    if request.method == "POST":
        form = tipos_de_usuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_usuario_list')
    else:
        form = tipos_de_usuariosForm()
    return render(request, 'tipo_de_usuario_form.html', {'form': form})

def tipo_de_usuario_list(request):
    t_usuario = tipos_de_usuarios.objects.all()
    return render(request, 'tipo_de_usuario_list.html', {'t_usuario': t_usuario})

def tipo_de_usuario_edit(request, pk):
    tipo_de_usuario = get_object_or_404(tipos_de_usuarios, pk=pk)
    if request.method == "POST":
        form = tipos_de_usuariosForm(request.POST, instance=tipo_de_usuario)
        if form.is_valid():
            form.save()
            return redirect('tipo_usuario_list')
    else:
        form = tipos_de_usuariosForm(instance=tipo_de_usuario)
    return render(request, 'tipo_de_usuario_form.html', {'form': form})

def tipo_de_usuario_delete(request, pk):
    tipo_de_usuario = get_object_or_404(tipos_de_usuarios, pk=pk)
    if request.method == "POST":
        tipo_de_usuario.delete()
        return redirect('tipo_usuario_list')
    return render(request, 'tipo_usuario_confirm_delete.html', {'tipo_de_usuario': tipo_de_usuario})


def tipo_de_plan_add(request):
    if request.method == "POST":
        form = tipos_de_planform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_plan_list')
    else:
        form = tipos_de_planform()
    return render(request, 'tipo_de_plan_form.html', {'form': form})

def tipo_de_plan_list(request):
    t_plan = tipos_de_planes.objects.all()
    return render(request, 'tipo_de_plan_list.html', {'t_plan': t_plan})

def tipo_de_plan_edit(request, pk):
    tipo_de_plan = get_object_or_404(tipos_de_planes, pk=pk)
    if request.method == "POST":
        form = tipos_de_planform(request.POST, instance=tipo_de_plan)
        if form.is_valid():
            form.save()
            return redirect('tipo_plan_list')
    else:
        form = tipos_de_planform(instance=tipo_de_plan)
    return render(request, 'tipo_de_plan_form.html', {'form': form})

def tipo_de_plan_delete(request, pk):
    tipo_de_plan = get_object_or_404(tipos_de_usuarios, pk=pk)
    if request.method == "POST":
        tipo_de_plan.delete()
        return redirect('tipo_plan_list')
    return render(request, 'tipo_de_plan_confirm_delete.html', {'tipo_de_plan': tipo_de_plan})
