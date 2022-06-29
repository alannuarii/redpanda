from import_export import resources
from .models import Feeder

class FeederResource(resources.ModelResource):
    class Meta:
        model = Feeder
        