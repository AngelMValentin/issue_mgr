from django.urls import path
from issues import views

urlpatterns = [
    path("tickets/", views.IssueListView.as_view(), name='tickets'),
]

