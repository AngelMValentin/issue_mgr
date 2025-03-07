from django.urls import path
from issues import views

urlpatterns = [
    path("tickets/", views.IssueListView.as_view(), name='tickets'),
    path("create/", views.IssueCreateView.as_view(), name="issue-create"),
    path("<int:pk>/update/", views.IssueUpdateView.as_view(), name="issue-update"),
    path("<int:pk>/delete/", views.IssueDeleteView.as_view(), name="issue-delete"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="issue-detail"),
]

