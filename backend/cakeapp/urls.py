from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

    path('cookers/<int:pk>', CookerRetrieveView.as_view()),
    path('cookers/update/<int:pk>', CookerUpdateView.as_view()),
    path('cookers/new', CookerCreateView.as_view()),
    path('cookers/all', CookerListView.as_view()),

    path('customers/<int:pk>', CustomerRetrieveView.as_view()),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view()),
    path('customers/new', CustomerCreateView.as_view()),
    path('customers/all', CustomerListView.as_view()),

    path('categories/all', CategoryListView.as_view()),
    path('types/all', TypeListView.as_view()),

    path('fillings/<int:pk>', FillingRetrieveView.as_view()),
    path('fillings/update/<int:pk>', FillingUpdateView.as_view()),
    path('fillings/new', FillingCreateView.as_view()),
    path('fillings/all', FillingListView.as_view()),

    path('products/<int:pk>', ProductRetrieveView.as_view()),
    path('products/update/<int:pk>', ProductUpdateView.as_view()),
    path('products/new', ProductCreateView.as_view()),
    path('products/all', ProductListView.as_view()),

    path('posts/<int:pk>', PostRetrieveView.as_view()),
    path('posts/update/<int:pk>', PostUpdateView.as_view()),
    path('posts/new', PostCreateView.as_view()),
    path('posts/all', PostListView.as_view()),

    path('recipes/<int:pk>', RecipeRetrieveView.as_view()),
    path('recipes/update/<int:pk>', RecipeUpdateView.as_view()),
    path('recipes/new', RecipeCreateView.as_view()),
    path('recipes/all', RecipeListView.as_view()),

    path('ratings/<int:pk>', RatingRetrieveView.as_view()),
    path('ratings/update/<int:pk>', RatingUpdateView.as_view()),
    path('ratings/new', RatingCreateView.as_view()),
    path('ratings/all', RatingListView.as_view()),

    path('feedbacks/<int:pk>', FeedbackRetrieveView.as_view()),
    path('feedbacks/update/<int:pk>', FeedbackUpdateView.as_view()),
    path('feedbacks/new', FeedbackCreateView.as_view()),
    path('feedbacks/all', FeedbackListView.as_view()),

    path('orders/<int:pk>', OrderRetrieveView.as_view()),
    path('orders/update/<int:pk>', OrderUpdateView.as_view()),
    path('orders/new', OrderCreateView.as_view()),
    path('orders/all', OrderListView.as_view()),

    path('comments_post/<int:pk>', CommentPostRetrieveView.as_view()),
    path('comments_post/update/<int:pk>', CommentPostUpdateView.as_view()),
    path('comments_post/new', CommentPostCreateView.as_view()),
    path('comments_post/all', CommentPostListView.as_view()),

    path('comments_recipe/<int:pk>', CommentRecipeRetrieveView.as_view()),
    path('comments_recipe/update/<int:pk>', CommentRecipeUpdateView.as_view()),
    path('comments_recipe/new', CommentRecipeCreateView.as_view()),
    path('comments_recipe/all', CommentRecipeListView.as_view()),

    path('replys_comment_post/<int:pk>', ReplyCommentPostRetrieveView.as_view()),
    path('replys_comment_post/update/<int:pk>', ReplyCommentPostUpdateView.as_view()),
    path('replys_comment_post/new', ReplyCommentPostCreateView.as_view()),
    path('replys_comment_post/all', ReplyCommentPostListView.as_view()),

    path('replys_comment_recipe/<int:pk>', ReplyCommentRecipeRetrieveView.as_view()),
    path('replys_comment_recipe/update/<int:pk>', ReplyCommentRecipeUpdateView.as_view()),
    path('replys_comment_recipe/new', ReplyCommentRecipeCreateView.as_view()),
    path('replys_comment_recipe/all', ReplyCommentRecipeListView.as_view()),
]