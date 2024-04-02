from django.contrib import admin
from .models import campus
from .models import areaprojeto
from .models import pessoa
from .models import projeto
from .models import bolsa
from .models import meta

# Register your models here.
admin.site.register (campus)
admin.site.register (areaprojeto)
admin.site.register (pessoa)
admin.site.register (projeto)
admin.site.register (bolsa)
admin.site.register (meta)