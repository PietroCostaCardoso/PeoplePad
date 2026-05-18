from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contact/export/', views.export_contacts, name='export_contacts'),
    path('contact/dashboard/', views.dashboard, name='dashboard'),
    path('contact/import/', views.import_contacts, name='import_contacts'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # user
    path('user/create/', views.register, name='register'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
