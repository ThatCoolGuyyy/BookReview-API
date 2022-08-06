from tkinter import CASCADE
from django.db import models

class Books(models.Model):
    BookName = models.CharField(max_length=150)
    Author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=100)
    numofPages = models.CharField(max_length=100)
    bookWebsite = models.CharField(max_length=100)

    def __str__(self):
        return self.BookName
    
    
class Review(models.Model):
    Heading = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name ="reviews")
    description = models.CharField(max_length=100)
    createDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Heading