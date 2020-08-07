from django.urls import path
from quotes.api.views import QuoteDetailAPIview, QuoteListCreateAPIView

"""
Task 4: Urls
same as task 3, urls are moved here when using ModelSerializer
"""

urlpatterns = [
    path("quotes/", QuoteListCreateAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", QuoteDetailAPIview.as_view(), name="quote-detail")
]