from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Cooker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default='Россия')
    city = models.CharField(max_length=100, default='Москва')
    phone = models.CharField(max_length=11)
    description = models.TextField()
    image = models.ImageField(default='default_cook.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} профиль'

    class Meta:
        verbose_name = 'Кондитер'
        verbose_name_plural = 'Кондитеры'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cat_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Type(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type_name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Filling(models.Model):
    user = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default='default_fil.jpg', upload_to='fillings_pics')

    def __str__(self):
        return f'Начинка: {self.name}'

    class Meta:
        verbose_name = 'Начинка'
        verbose_name_plural = 'Начинки'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 110:
            output_size = (250, 110)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Product(models.Model):
    PRODUCT_STATUS = [
        ('1', 'Черновик'),
        ('2', 'Опубликовано'),
        ('3', 'На модерации'),
        ]

    user = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=PRODUCT_STATUS, default='1', max_length=1)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    country = models.CharField(max_length=100, default='Россия')
    city = models.CharField(max_length=100, default='Москва')
    phone = models.CharField(max_length=11)
    yearOfBirth = models.CharField(max_length=4)
    image = models.ImageField(default='default_cust.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} профиль'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Post(models.Model):
    POST_STATUS = [
        ('1', 'Черновик'),
        ('2', 'Опубликовано'),
        ('3', 'На модерации'),
    ]

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    image_post = models.ImageField(upload_to='post_pics')
    video_url = models.URLField(null=True, blank=True, verbose_name="URL видео", help_text="URL видео")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=POST_STATUS, default='1', max_length=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['id']

    def save(self):
        super().save()

        img = Image.open(self.image_post.path)

        if img.height > 990 or img.width > 790:
            output_size = (990, 790)
            img.thumbnail(output_size)
            img.save(self.image_post.path)


class Recipe(models.Model):
    RECIPE_STATUS = [
        ('1', 'Черновик'),
        ('2', 'Опубликовано'),
        ('3', 'На модерации'),
    ]

    user = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    image_post = models.ImageField(upload_to='recipe_pics')
    video_url = models.URLField(null=True, blank=True, verbose_name="URL видео", help_text="URL видео")
    doc_url = models.URLField(blank=True, verbose_name="URL текста рецепта", help_text="URL текста рецепта")
    status = models.CharField(choices=RECIPE_STATUS, default='1', max_length=1)

    def __str__(self):
        return f'{self.name, self.created_on, self.user.user.username}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Rating(models.Model):
    RAITING_FIELD = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cooker = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    mark = models.IntegerField(choices=RAITING_FIELD, default='1')

    def __str__(self):
        return f'{self.customer.user.username, self.cooker.user.username, self.mark}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cooker = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    text_feed = models.TextField()

    def __str__(self):
        return f'{self.customer.user.username, self.cooker.user.username, self.created_on}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Order(models.Model):
    STATUS_ORDER = [
        ('1', 'Обрабатывается'),
        ('2', 'Принят'),
        ('3', 'Выполняется'),
        ('4', 'Готов')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cooker = models.ForeignKey(Cooker, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    filling = models.ForeignKey(Filling, on_delete=models.DO_NOTHING)
    weight = models.CharField(max_length=11)
    adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    created_on = models.DateTimeField(auto_now_add=True)
    date_need = models.DateTimeField()
    price = models.IntegerField()
    status = models.CharField(choices=STATUS_ORDER, default='1', max_length=1)

    def __str__(self):
        return f'{self.customer.user.username, self.cooker.user.username, self.created_on, self.date_need, self.status}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentPost(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author, self.created_on, self.post}'

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к постам'


class ReplyCommentPost(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author, self.created_on, self.comment}'

    class Meta:
        verbose_name = 'Ответ на комментарий к посту'
        verbose_name_plural = 'Ответы на комментарии к постам'


class CommentRecipe(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author, self.created_on, self.recipe}'

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к постам'


class ReplyCommentRecipe(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentRecipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author, self.created_on, self.comment}'

    class Meta:
        verbose_name = 'Ответ на комментарий к посту'
        verbose_name_plural = 'Ответы на комментарии к постам'