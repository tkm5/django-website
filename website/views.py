from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'Takumi'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_services'] = 9999999999
        context['skills'] = [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'React',
            'Vue',
            'Go',
        ]
        return context
