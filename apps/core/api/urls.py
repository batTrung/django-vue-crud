from django.urls import path, include

from apps.accounts.api import views as accounts_views
from apps.bookstore.api import views as bookstore_views

from .views import ApiRoot


urlpatterns = [
    path(
        '',
        ApiRoot.as_view(),
        name=ApiRoot.name,
    ),

    # Accounts
    path(
        'account/check-email-exists/<str:email>/',
        accounts_views.CheckEmailExists.as_view(),
        name=accounts_views.CheckEmailExists.name,
    ),

    # Authentication
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Bookstore
    path(
        'book/<str:book_name>/',
        bookstore_views.BookCheckDuplicateName.as_view(),
        name=bookstore_views.BookCheckDuplicateName.name,
    ),
    path(
        'book/<str:book_name>/<slug:book_slug>/',
        bookstore_views.BookCheckDuplicateName.as_view(),
        name=bookstore_views.BookCheckDuplicateName.name,
    ),
    path(
        'books/',
        bookstore_views.BookList.as_view(),
        name=bookstore_views.BookList.name,
    ),
    path(
        'books/<slug:slug>/',
        bookstore_views.BookDetail.as_view(),
        name=bookstore_views.BookDetail.name,
    ),
]
