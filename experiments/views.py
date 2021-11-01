from django.template import loader
from django.http import HttpResponse
from .models import Experiment


def index(request):
    latest_experiment_list = Experiment.objects.order_by('-pub_date')[:5]
    template = loader.get_template('experiments/index.jinja')
    context = {
        'latest_experiment_list': latest_experiment_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, experiment_id):
    return HttpResponse("You're looking at question %s." % experiment_id)


def results(request, experiment_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % experiment_id)


def vote(request, experiment_id):
    return HttpResponse("You're voting on question %s." % experiment_id)
