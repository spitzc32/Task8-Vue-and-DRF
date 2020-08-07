from rest_framework import serializers
from quotes.models import Quote

"""
Task 4: Serializers
Uses the class ModelSerializer derived from serializer to copy the attributes of the model Quote.
Solution Derived from excercises
"""

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = "__all__"
