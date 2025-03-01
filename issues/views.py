from django.shortcuts import render

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = IssueListView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        role = Role.objects.get(name="")

# Create your views here.
