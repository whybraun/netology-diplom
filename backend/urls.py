from django.urls import path

from backend.views import PartnerUpdate, PartnerState, PartnerOrders, ContactView, CategoryView, ProductInfoView, ShopView, BasketView, OrderView

app_name = 'backend'

urlpatterns = [
    path('partner-update/', PartnerUpdate.as_view(), name='partner_update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]