from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .serializers import *
from .models import *


class IsCooker(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class CookerRetrieveView(generics.RetrieveAPIView):
    queryset = Cooker.objects.all()
    serializer_class = CookerSerializer


class CookerUpdateView(generics.UpdateAPIView):
    #queryset = Cooker.objects.all()
    serializer_class = CreateCookerSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Cooker.objects.filter(user=user)

        raise PermissionDenied()


class CookerCreateView(generics.CreateAPIView):
    queryset = Cooker.objects.all()
    serializer_class = CreateCookerSerializer


class CookerListView(generics.ListAPIView):
    queryset = Cooker.objects.all()
    serializer_class = CookerSerializer


class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class FillingRetrieveView(generics.RetrieveAPIView):
    queryset = Filling.objects.all()
    serializer_class = FillingSerializer


class FillingUpdateView(generics.UpdateAPIView):
    queryset = Filling.objects.all()
    serializer_class = CreateFillingSerializer


class FillingCreateView(generics.CreateAPIView):
    queryset = Filling.objects.all()
    serializer_class = CreateFillingSerializer


class FillingListView(generics.ListAPIView):
    queryset = Filling.objects.all()
    serializer_class = FillingSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RecipeRetrieveView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeUpdateView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = CreateRecipeSerializer


class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = CreateRecipeSerializer


class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RatingRetrieveView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingUpdateView(generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer


class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FeedbackRetrieveView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackUpdateView(generics.UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = CreateFeedbackSerializer


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = CreateFeedbackSerializer


class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CommentPostRetrieveView(generics.RetrieveAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentPostSerializer


class CommentPostUpdateView(generics.UpdateAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CreateCommentPostSerializer


class CommentPostCreateView(generics.CreateAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CreateCommentPostSerializer


class CommentPostListView(generics.ListAPIView):
    queryset = CommentPost.objects.all()
    serializer_class = CommentPostSerializer


class CommentRecipeRetrieveView(generics.RetrieveAPIView):
    queryset = CommentRecipe.objects.all()
    serializer_class = CommentRecipeSerializer


class CommentRecipeUpdateView(generics.UpdateAPIView):
    queryset = CommentRecipe.objects.all()
    serializer_class = CreateCommentRecipeSerializer


class CommentRecipeCreateView(generics.CreateAPIView):
    queryset = CommentRecipe.objects.all()
    serializer_class = CreateCommentRecipeSerializer


class CommentRecipeListView(generics.ListAPIView):
    queryset = CommentRecipe.objects.all()
    serializer_class = CommentRecipeSerializer


class ReplyCommentPostRetrieveView(generics.RetrieveAPIView):
    queryset = ReplyCommentPost.objects.all()
    serializer_class = ReplyCommentPostSerializer


class ReplyCommentPostUpdateView(generics.UpdateAPIView):
    queryset = ReplyCommentPost.objects.all()
    serializer_class = CreateReplyCommentPostSerializer


class ReplyCommentPostCreateView(generics.CreateAPIView):
    queryset = ReplyCommentPost.objects.all()
    serializer_class = CreateReplyCommentPostSerializer


class ReplyCommentPostListView(generics.ListAPIView):
    queryset = ReplyCommentPost.objects.all()
    serializer_class = ReplyCommentPostSerializer


class ReplyCommentRecipeRetrieveView(generics.RetrieveAPIView):
    queryset = ReplyCommentRecipe.objects.all()
    serializer_class = ReplyCommentRecipeSerializer


class ReplyCommentRecipeUpdateView(generics.UpdateAPIView):
    queryset = ReplyCommentRecipe.objects.all()
    serializer_class = CreateReplyCommentRecipeSerializer


class ReplyCommentRecipeCreateView(generics.CreateAPIView):
    queryset = ReplyCommentRecipe.objects.all()
    serializer_class = CreateReplyCommentRecipeSerializer


class ReplyCommentRecipeListView(generics.ListAPIView):
    queryset = ReplyCommentRecipe.objects.all()
    serializer_class = ReplyCommentRecipeSerializer