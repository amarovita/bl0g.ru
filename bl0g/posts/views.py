from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import ListView

from posts.models import Post


class HomePage(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            if not self.request.user.is_superuser:
                return qs.filter(Q(published=True) | Q(author=self.request.user))
        else:
            return qs.filter(published=True)
        return qs


class PostDetail(DetailView):
    model = Post
