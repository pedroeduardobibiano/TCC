from django.urls import path
from app_cad_usuarios import views
urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('recipe/', views.recipe, name='recipe'),

    path('listagem/', views.tccs, name='tccs'),
    path('cadastra/', views.cria_tcc, name='cria_tcc'),

    path('cadastrar_user/', views.cadastrar, name='cadastrar_usuario'),
    path('login/', views.login, name='login_usuario'),
 #   path('edita/<int:pk>/', views.edita_tcc, name='edita_tcc'),
 #   path('exclui/<int:pk>/', views.exclui_tcc, name='exclui_tcc'),

]
