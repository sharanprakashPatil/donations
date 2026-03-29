from django.db import models

<<<<<<< HEAD
class HomeContent(models.Model):
    title = models.CharField(max_length=200, default="Make a Difference Today")
    quote = models.TextField(default="love for all , hate for none ...")
    subtitle = models.TextField(default="Welcome to our platform designed to connect people through compassion and giving. Select your portal to proceed.")

    class Meta:
        verbose_name_plural = "Home Content"

    def __str__(self):
        return self.title
=======
# Create your models here.
>>>>>>> 70875e671408b029b7d1f928a230940b9f2432a0
