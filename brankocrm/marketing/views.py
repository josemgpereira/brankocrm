from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    """
    assign template_name to home.html
    """
    template_name = 'marketing/home.html'
