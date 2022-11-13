from import_export import resources
from .models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        managed = True
        model = Person
