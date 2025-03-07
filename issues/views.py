from django.shortcuts import render, redirect


from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.views.generic import (
    ListView, UpdateView, CreateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
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
    

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = "issues/new.html"
    fields = ["name", "summary", "description", "reporter", "assignee", "status"]

    def form_valid(self, form):
        form.instance.creator = self.request.user 
        form.save()
        return redirect("issue-detail", pk=form.instance.pk)
    
class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = "issues/edit.html"
    fields = ["name", "summary", "description", "reporter", "assignee", "status"]

    def get_success_url(self):
        return reverse_lazy("tickets")

class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = "issues/delete.html"
    success_url = reverse_lazy("tickets")

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = "issues/detail.html"

# Create your views here.
