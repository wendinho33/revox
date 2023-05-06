from django.urls import path
from onirix.views import IndexView,pricing_view,Contact_us,PaymentsView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contact', Contact_us.as_view(), name='contact'),
    path('pricing', pricing_view, name='pricing'),
    path('pay', PaymentsView.as_view(), name='payments'),
]
