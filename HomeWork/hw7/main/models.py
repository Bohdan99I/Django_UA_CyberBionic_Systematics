from django.db import models

class CustomerReview(models.Model):
    name = models.CharField(max_length=255)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
