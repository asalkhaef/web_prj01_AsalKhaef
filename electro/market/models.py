from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from decimal import Decimal

User = get_user_model()


class Cart(models.Model):
    discount = models.ForeignKey(
        'Discount', on_delete=models.SET_NULL, null=True, blank=True)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart'
    )

    def __str__(self) -> str:
        return f"{self.user}'s cart"

    def get_total_cost(self):
        total_cost = Decimal(0)
        cart_items = self.cart_items.all()
        for item in cart_items:
            item: CartItem = item
            total_cost += item.get_price()

        return total_cost

    def get_discount_value(self):
        discount: Discount = self.discount

        if discount is None:
            return None

        applicable_products_cost = Decimal(0)
        cart_items = self.cart_items.all()
        for item in cart_items:
            item: CartItem = item

            if discount.is_product_applicable(item.product):
                applicable_products_cost += item.get_price()

        if discount.type == Discount.DiscountType.PERCENTAGE:
            discount_value_to_apply = discount.value * applicable_products_cost / 100
            if discount.max_price_limit is not None and discount_value_to_apply > discount.max_price_limit:
                return 0
            else:
                return discount_value_to_apply
        elif discount.type == Discount.DiscountType.VALUE:
            discount_value_to_apply = discount.value
            if discount.max_price_limit is not None and discount_value_to_apply > discount.max_price_limit:
                return 0
            else:
                return discount_value_to_apply

    def get_net_price(self):
        total_cost = self.get_total_cost()
        discount_value = self.get_discount_value() or 0
        net = total_cost - discount_value
        return net


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    color = models.ForeignKey(
        'Color', on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
        if self.color is None and not self.product.colors.all():
            return

        # If product has colors, but nothing is selected
        if self.color is None and self.product.colors.all():
            raise ValidationError({
                'color': ValidationError(
                    'Must select a color for this product.',
                    code='invalid'
                ),
            })

        # If product doesn't have colors, but user has selected something
        if self.color is not None and not self.product.colors.all():
            raise ValidationError({
                'color': ValidationError(
                    "Can't select a color for this product.",
                    code='invalid'
                ),
            })

        print(self.color not in self.product.colors.all())

        # Check if the color is among the product's colors
        if self.color not in self.product.colors.all():
            raise ValidationError({
                'color': ValidationError(
                    'Invalid color for this product.',
                    code='invalid'
                ),
            })

    def __str__(self) -> str:
        return f"{self.product} (x{self.quantity})"

    def get_price(self):
        base_price = self.product.get_latest_price()
        if base_price is None:
            base_price = 0
        extra_cost = Decimal(0)

        if self.color:
            color: Color = self.color
            extra_cost += color.extra_cost

        return (base_price + extra_cost) * self.quantity


class Discount(models.Model):
    class DiscountType(models.TextChoices):
        VALUE = "VALUE"
        PERCENTAGE = "PERCENTAGE"

    code = models.CharField(max_length=20)
    type = models.CharField(
        max_length=10, choices=DiscountType, default=DiscountType.VALUE)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    max_price_limit = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0)], null=True, blank=True)

    applicable_products = models.ManyToManyField(
        'Product', blank=True)
    applicable_categories = models.ManyToManyField(
        'Category', blank=True)

    def __str__(self) -> str:
        return f"Discount {self.code}"

    def is_product_applicable(self, product: 'Product') -> bool:
        if self.applicable_products.contains(product):
            return True

        for category in self.applicable_categories.all():
            category: Category = category

            if category.is_inside_category(product.category):
                return True

        return False


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=520)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, default=None, null=True, blank=True)

    def get_latest_price(self) -> Decimal | None:
        latest_price_entry = self.prices.order_by('-date').first()
        return latest_price_entry.price if latest_price_entry else None

    def __str__(self) -> str:
        return self.title


def media_upload_path(instance, filename):
    return f"media/{instance.product.id}/{filename}"


class Media(models.Model):
    MEDIA_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    type = models.CharField(max_length=5, choices=MEDIA_CHOICES)
    file = models.FileField(upload_to=media_upload_path)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='media')
    alt = models.CharField(max_length=100)


class ProductPriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                MinValueValidator(0)])
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prices")

    class Meta():
        verbose_name_plural = "Product prices history"

    def __str__(self) -> str:
        return f"{self.product} priced {self.price} on {self.date}"


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)
    extra_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='colors')

    def __str__(self) -> str:
        return f"{self.name} ({self.hex_code})"


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='subcategories', default=None, null=True, blank=True)
    level = models.IntegerField(default=0, validators=[
                                MinValueValidator(0), MaxValueValidator(5)])

    class Meta():
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.parent_category:
            self.level = self.parent_category.level + 1
        else:
            self.level = 0

        if self.level >= 5:
            raise ValidationError("Category level cannot be greater than 5.")

        super().save(*args, **kwargs)

    def is_inside_category(self, cat: 'Category') -> bool:
        if cat == self:
            return True

        if not self.subcategories:
            return False

        for subcategory in self.subcategories.all():
            if subcategory.is_inside_category(cat):
                return True

        return False


class Banner(models.Model):
    BANNER_TYPES = (
        ('head_banner', 'HeadBanner'),
        ('ad_banner', 'AdBanner'),
    )
    banner_type = models.CharField(
        max_length=50, default="null", choices=BANNER_TYPES)
    title = models.CharField(max_length=100, default="null")
    description = models.TextField(default="null")
    image = models.ImageField(upload_to='banners/')
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.banner_type}"
