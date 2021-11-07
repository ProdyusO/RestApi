from django.db import models


class Author(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=50, unique=True)
    creation_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comments(models.Model):
    id_title = models.ForeignKey('Author', related_name='authors', on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    creation_date_of_comments = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_title


class AmountOfUpvotes(models.Model):
    id_title = models.ForeignKey('Author', on_delete=models.CASCADE)
    amount_of_upvotes = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.amount_of_upvotes
