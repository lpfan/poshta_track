from datetime import datetime

import mongoengine
from django.db import models


class Package(mongoengine.DynamicDocument):
    eventdescription = mongoengine.fields.StringField()
    lastofficeindex = mongoengine.fields.StringField()
    lastoffice = mongoengine.fields.StringField()
    code = mongoengine.fields.StringField()
    barcode = mongoengine.fields.StringField(required=True)
    created = mongoengine.fields.DateTimeField(default=datetime.now())
    updated = mongoengine.fields.DateTimeField(required=False)
    client_id = mongoengine.fields.IntField(min_value=0)

    meta = {
        'indexes': [
            'barcode',
            'client_id'
        ]
    }
