from django.db import models

# Create your models here.
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField("Client name", max_length=100)
    email = models.EmailField("Client email")
    content = models.TextField("Message from client", max_length=10000)
    timestamp = models.DateTimeField("Time of message", auto_now_add=True)

    def __str__(self):
        return str(self.email)
