from django.contrib import admin

from  .models import Drama
admin.site.register(Drama)

from  .models import Terror
admin.site.register(Terror)

from  .models import Aventura
admin.site.register(Aventura)

from  .models import Ciencia_Ficcion
admin.site.register(Ciencia_Ficcion)

from .models import Thriller
admin.site.register(Thriller)

from .models import Suspenso
admin.site.register(Suspenso)