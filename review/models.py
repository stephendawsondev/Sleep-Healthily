from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(
        validators=[MinLengthValidator(
            50, "Review must be greater than 50 characters")],
        max_length=400
    )
    rating = models.IntegerField()
    helpful_votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def helpful(self):
        self.helpful_votes += 1
        self.save()
        return self.helpful_votes
