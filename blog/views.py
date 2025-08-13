from django.shortcuts import render
from .models import BlogPost

class BlogListView(ListView):
    queryset = BlogPost.objects.filter(is_published=True)
    template_name = 'blog/blog_list.html'
    paginate_by = 6 

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_published=True)
    
    