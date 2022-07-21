from django.urls import path
from . import views

urlpatterns = [
    # home route
    path('', views.home, name='home'),
    # signup route
    path('account/signup/', views.signup, name='signup'),

    ###############
    ## account/Accounts
    ###############
    # # index route for account
    # path('account/', views.account_index, name="account"),
    # # detail route for account
    # path('account/<int:account_id>/', views.account_detail, name="account_detail"),
    # # create route for account
    # path('account/create/', views.AccountCreate.as_view(), name="account_create"),
    # # update route for account
    # path('account/<int:pk>/update', views.AccountUpdate.as_view(), name="account_update"),
    # # delete route for card
    # path('account/<int:pk>/delete/', views.AccountDelete.as_view(), name="account_delete"),


    # ###############
    # ## Contacts
    # ###############
    # # index route for contacts
    # path('contacts/', views.contacts_index, name="contacts"),
    # # detail route for contacts
    # path('contacts/<int:contact_id>/', views.contact_detail, name="contact_detail"),
    # # create route for contacts
    # path('contacts/create/', views.ContactCreate.as_view(), name="contact_create"),
    # # update route for contacts
    # path('contacts/<int:pk>/update', views.ContactUpdate.as_view(), name="contact_update"),
    # # delete route for card
    # path('contacts/<int:pk>/delete/', views.ContactDelete.as_view(), name="contact_delete"),

    # ###############
    # ## Products
    # ###############
    # # index route for contacts
    # path('products/', views.products_index, name="products"),
    # # detail route for contacts
    # path('products/<int:product_id>/', views.product_detail, name="product_detail"),
    # # create route for contacts
    # path('products/create/', views.ProductCreate.as_view(), name="product_create"),
    # # update route for contacts
    # path('products/<int:pk>/update', views.ProductUpdate.as_view(), name="product_update"),
    # # delete route for card
    # path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name="product_delete"),
    # # add a photo to a product
    # path('products/<int:product_id>/add_photo/', views.add_photo, name="add_photo"),

    #################
    ## Relationships
    #################
    # # 1:M account to transactions
    # path('account/<int:account_id>/add_trans/', views.add_trans, name="add_trans"),
    # # M:M associating a account to products
    # path('account/<int:account_id>/assoc_product/<int:product_id>/', views.assoc_product, name="assoc_product"),
    # # route for removing a product from a account
    # path('account/<int:account_id>/remove_product/<int:product_id>/', views.remove_product, name="remove_product"),
    # # M:M associating a contacts to account
    # path('account/<int:account_id>/assoc_contact/<int:contact>/', views.assoc_contact, name="assoc_contact"),
    # # route for removing a contact from a account
    # path('account/<int:account_id>/remove_contact/<int:contact>/', views.remove_contact, name="remove_contact"),

]
