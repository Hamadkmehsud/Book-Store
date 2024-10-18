from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Countries(models.Model):
    country = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.country + ' ' + self.code

class Address(models.Model):
    street = models.CharField(max_length=30)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=20)

    def full_address(self):
        return self.street + " " + str(self.postal_code) + " " + self.city

    def __str__(self):
        return self.full_address()
        
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) 

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

class BookStore(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #CASCADE will deleted all books related to the author
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    is_bestselling = models.BooleanField(null=False)
    slug = models.SlugField(default="",db_index=True,primary_key=True ,null=False)
    countries = models.ManyToManyField(Countries, null=False, related_name='bookstore')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)  # Corrected save call

    def get_absolute_url(self):
        return reverse("book_details", kwargs={'slug': self.slug})
    
  
    def __str__(self):
        return f'Title : {self.title}, Author : {self.author}, Rating : ({self.rating}), Is Best Selling Book : ({self.is_bestselling}, Country Published : {self.countries})'

    