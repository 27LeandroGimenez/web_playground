from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from applications.registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    paginate_by = 2
    model = Profile
    template_name = 'profiles/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
