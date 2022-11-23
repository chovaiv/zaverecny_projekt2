from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Test
from django.template import loader

def index(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

class TestChartView(TemplateView):
    template_name = 'graf/doughnut.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Test.objects.all()
        return context

def pridat(request):
  template = loader.get_template('graf/upravit.html')
  return HttpResponse(template.render({}, request))


def pridat_objekt(request):
  x = request.POST['jmeno_objektu']
  y = request.POST['pocet_objektu']
  z = request.POST['color']
  w = request.POST['borderColor']
  test = Test(jmeno_objektu = x, pocet_objektu = y, color = z, borderColor = w)
  test.save()
  return HttpResponseRedirect(reverse('index'))


def odstranit(request, id):
  test = Test.objects.get(id=id)
  test.delete()
  return HttpResponseRedirect(reverse('index'))

def upravit(request, id):
  test = Test.objects.get(id=id)
  context = {
    'test': test,
  }
  return HttpResponseRedirect(reverse('index'))

def upravit_objekt(request, id):
  jmeno_objektu = request.POST['jmeno_objektu']
  pocet_objektu = request.POST['pocet_objektu']
  color = request.POST['color']
  borderColor = request.POST['borderColor']
  test = Test.objects.get(id=id)
  test.jmeno_objektu = jmeno_objektu
  test.pocet_objektu = pocet_objektu
  test.color = color
  test.borderColor = borderColor
  test.save()
  return HttpResponseRedirect(reverse('index'))
