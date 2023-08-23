from pyexpat import model
from your_app.models import Order, Item

class User(model.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

class Item(models.Model):
	name = models.CharField(max_length=100)
	sku_code = models.CharField(max_length=20, unique=True)
	price = models.FloatField()
	create_timestamp = models.DateTimeField()
	created_by = models.ForeignKey(User)

class Order(models.Model):
	date = models.DateField()
	item = models.ForeignKey(Item)
	quantity = models.IntegerField()
	ordered_by = models.ForeignKey(User)


# List the Orders with quantity more than 10
orders_with_quantity_more_than_10 = Order.objects.filter(quantity__gt=10)
print("Orders with quantity more than 10:", orders_with_quantity_more_than_10)

# List the Orders which are having "Samsung" in their Item’s name
orders_with_samsung_item = Order.objects.filter(item__name__icontains="Samsung")
print("Orders with Samsung in Item's name:", orders_with_samsung_item)

# Print the total sum of the quantity of all orders of the item_id 23
total_quantity_item_23 = Order.objects.filter(item_id=23).aggregate(total_quantity=models.Sum('quantity'))['total_quantity']
print("Total quantity of item_id 23:", total_quantity_item_23)
