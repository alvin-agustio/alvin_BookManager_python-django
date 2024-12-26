from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
    ]
    
    title = models.CharField(max_length=100, blank=False) # title, tidak boleh kosong
    author = models.CharField(max_length=50, blank=False) # author, tidak boleh kosong
    published_date = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES) # pilihan genre
    summary = models.TextField(blank=True, null=True) # summary boleh kosong (opsional)

    def __str__(self):
        return self.title