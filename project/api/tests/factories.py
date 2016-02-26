import random
import string

import factory

from api import models


def _generate_random_string():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])


class PackageFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = models.Package
    barcode = _generate_random_string()
