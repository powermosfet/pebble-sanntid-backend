from django.http import HttpResponse
from gtfs.models import Stop
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import View
import json

def dictify(ob):
    r = { f.name: getattr(ob, f.name) for f in ob.__class__._meta.fields }
    r['api_url'] = '/api/gtfs/stops/{}'.format(ob.pk)
    return r

class JsonMixin(object):
    def get(self, *args, **kwargs):
        return HttpResponse(json.dumps(self.get_data(*args, **kwargs)), content_type = 'application/json')

class StopDetail(View, SingleObjectMixin, JsonMixin):
    model = Stop

    def get_data(self, *args, **kwargs):
        return dictify(self.get_object())

class StopList(View, MultipleObjectMixin, JsonMixin):
    model = Stop

    def get_data(self, *args, **kwargs):
        return [ dictify(ob) for ob in self.get_queryset() ]
