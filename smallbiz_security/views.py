from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import FormView
from .models import Resource, Source, Category, ResourceRequest, Survey
from .forms import SearchForm, ResourceRequestForm, SurveyForm


# Create your views here.


def main(request):
    template = loader.get_template('smallbiz_security/index.html')
    return HttpResponse(template.render())


def resource_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    resources = set()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "ResourceName"
        if search_in == "ResourceName":
            resources = Resource.objects.filter(ResourceName__icontains=search)
        else:
            fname_sources = Source.objects.filter(
                SourceName__icontains=search
            )

            for source in fname_sources:
                for resource in source.resource_set.all():
                    resources.add(resource)

            fname_categories = Category.objects.filter(
                CategoryName__icontains=search
            )

            for category in fname_categories:
                for resource in category.resource_set.all():
                    resources.add(resource)

    return render(
        request,
        "smallbiz_security/search-results.html",
        {"form": form, "search_text": search_text, "resources": resources},
    )


def resource_list(request):
    context = {}
    context["resource_list"] = Resource.objects.all(
    ).order_by('ResourceName').values()

    return render(request, 'smallbiz_security/resource-list.html', context)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Record saved successfully.")


class ResourceRequestFormView(FormView):
    template_name = 'smallbiz_security/resource-request-form.html'
    form_class = ResourceRequestForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SurveyFormView(FormView):
    template_name = 'smallbiz_security/survey-form.html'
    form_class = SurveyForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
