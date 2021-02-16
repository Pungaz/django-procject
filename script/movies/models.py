from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


def validate_length(value, length=6):
    if len(str(value)) != length:
        raise ValidationError(u'%s is not the correct length' % value)


def min_max(value):
    if 10 < value < 1:
        raise ValidationError(u'%s is not the correct number' % value)


class User(models.Model):
    username = models.CharField(validators=[validate_length], max_length=100, null=False)
    password = models.CharField(validators=[validate_length], max_length=100, null=False)
    admin = models.BooleanField(default=True)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[min_max])
    rented = models.BooleanField(default=False)
    rented_count = models.IntegerField(default=0)
    #release_date = models.IntegerField(null=False, max_length=4)
    release_date = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.title


class MovieUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rented = models.BooleanField(null=False)
    date = models.BigIntegerField(null=False, default=0)
