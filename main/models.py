from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Country(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='country')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    text = models.TextField()

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum([x.value for x in ratings]) // ratings.count()
        return 0

    def __str__(self):
        return self.title
    



class Tiket(models.Model):
    title = models.CharField(max_length=40)
    departure_place = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='departure')
    arrival_place = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='arrival')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.title
