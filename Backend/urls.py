from django.urls import path
from Backend import views


urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categories/', views.category_page, name="categories"),
    path('our_categories/', views.category_display, name="our_categories"),
    path('save_category/', views.save_category, name="save_category"),
    path('category_edit/<int:cat_id>/', views.category_edit, name="category_edit"),
    path('UpdateCategory/<int:cat_id>/', views.UpdateCategory, name="UpdateCategory"),
    path('DeleteCategory/<int:cat_id>/', views.DeleteCategory, name="DeleteCategory"),
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    path('admin_page/', views.admin_page, name="admin_page"),
    path('Admin_Login/', views.Admin_Login, name="Admin_Login"),
    path('AdminLogout/', views.AdminLogout, name="AdminLogout"),


    path('add_products/', views.product_page, name="add_products"),
    path('save_product/', views.save_product, name="save_product"),
    path('our_products/', views.display_product_page, name="our_products"),
    path('product_edit/<int:pro_id>/', views.product_edit, name="product_edit"),

]