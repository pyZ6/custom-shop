from django.views.generic.edit import UpdateView

from .models import MagazineModel

class MagazineUpdateView(UpdateView):
    model = MagazineModel
    template_name = "magazine/geeksmodel_form.html"
    fields = ["title", "description"]
    success_url = "/"