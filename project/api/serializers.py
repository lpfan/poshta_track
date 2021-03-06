from rest_framework import serializers
from rest_framework_mongoengine import serializers as mes

from api import models

class PackageSerializer(mes.DynamicDocumentSerializer):

    class Meta:
        model = models.Package
        fields = ('barcode', 'eventdescription', 'lastoffice',
                  'lastofficeindex', 'created',)
