from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class CookerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cooker
        fields = '__all__'


class CreateCookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooker
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class FillingSerializer(serializers.ModelSerializer):
    cooker = CookerSerializer()

    class Meta:
        model = Filling
        fields = '__all__'


class CreateFillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filling
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = CookerSerializer()
    category = CategorySerializer()
    type = TypeSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = CookerSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    user = CookerSerializer()
    category = CategorySerializer()
    type = TypeSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    cooker = CookerSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    cooker = CookerSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Feedback
        fields = '__all__'


class CreateFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    cooker = CookerSerializer()
    customer = CustomerSerializer()
    product_name = ProductSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CommentPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = CommentPost
        fields = '__all__'


class CreateCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = '__all__'


class CommentRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()

    class Meta:
        model = CommentRecipe
        fields = '__all__'


class CreateCommentRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentRecipe
        fields = '__all__'


class ReplyCommentPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    comment = CommentPostSerializer()

    class Meta:
        model = ReplyCommentPost
        fields = '__all__'


class CreateReplyCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyCommentPost
        fields = '__all__'


class ReplyCommentRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()
    comment = CommentRecipeSerializer()

    class Meta:
        model = ReplyCommentRecipe
        fields = '__all__'


class CreateReplyCommentRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyCommentRecipe
        fields = '__all__'