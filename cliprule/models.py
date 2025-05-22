from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=120)

    def __str__(self):
        return self.quote

class Clipath(models.Model):
    CATEGORY_CHOICES = [
        ('UP', 'UP'),
        ('DOWN', 'DOWN'),
    ]

    image = models.ImageField(upload_to='clipath/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    code = models.TextField()
    sender = models.EmailField(blank=True, help_text='Sender Email Address.')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.image} - {self.category} - {self.code[:30]} - {self.sender} - {'Active' if self.active else 'InActive'}"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.date}"