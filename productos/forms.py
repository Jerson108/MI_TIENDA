import os
from django import forms
from .models import Producto, ImagenProducto, CATEGORIAS, Recurso


class ProductoForm(forms.ModelForm):
    categoria = forms.ChoiceField(
        choices=CATEGORIAS,
        widget=forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'detalles': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3
            }),
            'precio_proveedor': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'precio_sugerido': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }

# ⬇️ Esta clase debe ir FUERA de ProductoForm
class ImagenProductoForm(forms.ModelForm):
    imagen = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full border border-gray-300 rounded-xl p-2 file:bg-blue-600 file:text-white file:px-4 file:py-1 file:rounded file:cursor-pointer hover:file:bg-blue-700'
        })
    )

    class Meta:
        model = ImagenProducto
        fields = ['imagen']

# ⬇️ Este es el nuevo formulario para subir varios recursos
#class RecursoForm(forms.ModelForm):
 #   archivo = forms.FileField(
  #      widget=forms.ClearableFileInput(attrs={
   #         'multiple': True,
    #        'class': 'w-full border border-gray-300 rounded-xl p-2 file:bg-blue-600 file:text-white file:px-4 file:py-1 file:rounded file:cursor-pointer hover:file:bg-blue-700'
     #   }),
      #  required=False,
       # label="Archivos de recursos (PDF, Word, Imágenes, Videos)"
    #)

    #class Meta:
     #   model = Recurso
      #  fields = ['archivo']