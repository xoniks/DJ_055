from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # self_author_title = str(title) + ' : ' + str(author)

    def __str__(self):
        return self.title

