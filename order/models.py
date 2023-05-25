from django.db import models
from account.models import User
from main.models import Country, Tiket


class Order(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='orders'
	)
	is_paid = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	@property
	def total_price(self):
		items = self.items.all()
		if items.exists():
			return sum([item.tiket.price * item.quantity for item in items])
		return 0
        


class OrderItem(models.Model):
	order = models.ForeignKey(
		Order,
		on_delete=models.CASCADE,
		related_name='items'
	)
	tiket = models.ForeignKey(
		Tiket,
		on_delete=models.CASCADE
	)
	quantity = models.PositiveIntegerField(default=1)
	
