from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_on')
    list_filter = ('status',)


@admin.register(Cooker)
class CookerAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Filling)
class FillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'price')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status', 'user')
    list_filter = ('status',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status', 'created_on')
    list_filter = ('status',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cooker', 'mark')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cooker', 'created_on')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cooker', 'created_on', 'date_need', 'price', 'status')
    list_filter = ('status',)


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on')


@admin.register(CommentRecipe)
class CommentRecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'created_on')


@admin.register(ReplyCommentPost)
class ReplyCommentPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'comment', 'created_on')


@admin.register(ReplyCommentRecipe)
class ReplyCommentRecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'comment', 'created_on')