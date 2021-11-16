from django.core.management.base import BaseCommand
from ...models import Author, Comments, AmountOfUpvotes


class Command(BaseCommand):

    def handle(self, *args, **options):
        author = Author.objects.all()
        comments = Comments.objects.all()
        amount_of_upvotes = AmountOfUpvotes.objects.all()
        author.delete()
        comments.delete()
        amount_of_upvotes.delete()

