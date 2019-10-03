from django.urls import path

from .views import paginaInicioView,\
    paginaAboutView, paginaProdutoView,\
    paginaHomeView, paginaCadastroView,\
    paginaContatoView, paginaLoginView

from .views import ProdutoListView, ProdutoDetailView, \
    OrcamentoListView, OrcamentoDetailView

urlpatterns = [
    path('', paginaInicioView, name='inicio'),
    path('sobre', paginaAboutView, name='sobre'),
    # path('produto', paginaProdutoView, name='produto'),
    path('cadastro', paginaCadastroView, name='cadastro'),
    path('contato', paginaContatoView, name='contato'),
    path('login', paginaLoginView, name='login'),
    path('home', ProdutoListView.as_view(), name='home'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('orcamentos', OrcamentoListView.as_view(), name='orcamento'),
    path('orcamentos/<int:pk>/', OrcamentoDetailView.as_view(),
         name='orcamento_detail'),
]
