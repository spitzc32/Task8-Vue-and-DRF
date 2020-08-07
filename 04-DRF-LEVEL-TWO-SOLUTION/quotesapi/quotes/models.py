from django.db import models

"""
Task 4: Models
Our objects that is used by the ModelSerializer to hold the properties of our API
Solutions derived from excercises.
"""

class Quote(models.Model):
    quote_author = models.CharField(max_length=50)
    quote_body = models.TextField()
    context = models.CharField(max_length=240, blank=True)
    source = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_author
