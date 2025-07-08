from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ImagenProducto, Recurso
from .forms import ProductoForm, ImagenProductoForm
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test


def es_admin(user):
    return user.is_superuser


# VISTA PRINCIPAL: LISTADO CON FILTROS
def lista_productos(request):
    productos = Producto.objects.all()

    # Filtros
    nombre = request.GET.get('nombre')
    categoria = request.GET.get('categoria')
    orden = request.GET.get('orden')
    stock = request.GET.get('stock')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    if nombre:
        productos = productos.filter(nombre__icontains=nombre)

    if categoria and categoria != 'todas':
        productos = productos.filter(categoria=categoria)

    if stock == 'si':
        productos = productos.filter(stock__gt=0)

    if precio_min:
        productos = productos.filter(precio_proveedor__gte=precio_min)

    if precio_max:
        productos = productos.filter(precio_proveedor__lte=precio_max)

    if orden == 'reciente':
        productos = productos.order_by('-id')
    elif orden == 'barato':
        productos = productos.order_by('precio_sugerido')
    elif orden == 'caro':
        productos = productos.order_by('-precio_sugerido')

    return render(request, 'productos/lista.html', {'productos': productos})


@user_passes_test(es_admin)
# CREAR PRODUCTO 
def crear_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)
        imagen_form = ImagenProductoForm(request.POST, request.FILES)

        if producto_form.is_valid():
            producto = producto_form.save()

            # Procesar imágenes múltiples 
            imagenes = request.FILES.getlist('imagen')
            for imagen in imagenes:
                ImagenProducto.objects.create(producto=producto, imagen=imagen)

            # Archivos múltiples (recurso)
            archivos_recurso = request.FILES.getlist('archivo')  # campo del RecursoForm
            for archivo in archivos_recurso:
                Recurso.objects.create(producto=producto, archivo=archivo)

            return redirect('lista_productos')  # Cambia por tu nombre de URL
        else:
            print(producto_form.errors, imagen_form.errors)
    else:
        producto_form = ProductoForm()
        imagen_form = ImagenProductoForm()

    return render(request, 'productos/crear.html', {
        'form': producto_form,
        'imagen_form': imagen_form,
    })


@user_passes_test(es_admin)
# EDITAR PRODUCTO desde el modal
def editar_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=producto_id)
        form = ProductoForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Formulario inválido'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)


@user_passes_test(es_admin)
def eliminar_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = get_object_or_404(Producto, id=producto_id)

            # Elimina las imágenes relacionadas
            producto.imagenes.all().delete()  # ← gracias al related_name='imagenes'

            # Elimina el archivo recurso si existe
            if producto.recurso:
                producto.recurso.delete(save=False)

            # Elimina el producto
            producto.delete()

    return redirect('lista_productos')
