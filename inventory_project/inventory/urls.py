from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # CRUD Endpoints for Inventory Management
    path('items/', views.create_item, name='create_item'),
    path('items/<int:item_id>/', views.read_item, name='read_item'),
    path('items/<int:item_id>/update/', views.update_item, name='update_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
