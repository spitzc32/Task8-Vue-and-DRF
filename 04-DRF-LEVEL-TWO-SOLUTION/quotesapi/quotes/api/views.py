from rest_framework import generics

from quotes.models import Quote
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.serializers import QuoteSerializer

"""
Task 4: Views
same as task 3, views are moved here when using ModelSerializer

"""

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class QuoteDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]