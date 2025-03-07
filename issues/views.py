from django.shortcuts import render


from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.views.generic import (
    ListView
)
from .models import Issue, Status 

from accounts.models import Role, CustomUser




class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        role = Role.objects.get(name="product owner")
        team_po = (
            CustomUser.objects
            .filter(team=user.team)
            .filter(role=role)
        )
        to_do = Status.objects.get(name="to do")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        in_progress = Status.objects.get(name="in progress")
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        done = Status.objects.get(name="done")
        context["done_list"] = (
            Issue.objects
            .filter(status=done)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        return context

# Create your views here.
