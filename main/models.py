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
    description = models.TextField()

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum([x.value for x in ratings]) // ratings.count()
        return 0

    def __str__(self):
        return self.title


class CategoryTikets(models.Model):
    name = models.TextField()
    baggage = models.TextField()
    hand_luggage = models.TextField()
    nutrtion = models.BooleanField()
    exchange_return = models.BooleanField()
    preferred_seat_selection = models.BooleanField()
    business_lounge = models.BooleanField()
    separate_landing = models.BooleanField()
    separate_reception_desk = models.BooleanField()

    def __str__(self) -> str:
        return self.name


class Tiket(models.Model):
    flight_name = models.CharField(max_length=40)
    category = models.ForeignKey(CategoryTikets, on_delete=models.CASCADE, related_name='category_tikets')
    departure = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='departure')
    arrival = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='arrival')
    departure_date = models.DateField()
    arrival_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_time = models.TextField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.flight_name




    
