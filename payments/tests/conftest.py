import datetime
from decimal import Decimal

import pytest
from pytz import UTC

from payments.factories import OrderFactory, OrderLineFactory
from payments.models import Order
from resources.models import Reservation
from resources.tests.conftest import *  # noqa


@pytest.fixture()
def two_hour_reservation(resource_in_unit, user):
    """A two-hour reservation fixture with actual datetime objects"""
    return Reservation.objects.create(
        resource=resource_in_unit,
        begin=datetime.datetime(2119, 5, 5, 10, 0, 0, tzinfo=UTC),
        end=datetime.datetime(2119, 5, 5, 12, 0, 0, tzinfo=UTC),
        user=user,
        event_subject='some fancy event',
        host_name='esko',
        reserver_name='martta',
        state=Reservation.WAITING_FOR_PAYMENT
    )


@pytest.fixture()
def order_with_products(two_hour_reservation):
    order = OrderFactory.create(
        order_number='abc123',
        status=Order.WAITING,
        payer_first_name='Seppo',
        payer_last_name='Testi',
        payer_email_address='test@example.com',
        payer_address_street='Test street 1',
        payer_address_zip='12345',
        payer_address_city='Testcity',
        reservation=two_hour_reservation
    )
    OrderLineFactory.create(
        quantity=1,
        product__name="Test product",
        product__pretax_price=Decimal('10.00'),
        product__tax_percentage=Decimal('24.00'),
        order=order
    )
    OrderLineFactory.create(
        quantity=1,
        product__name="Test product 2",
        product__pretax_price=Decimal('10.00'),
        product__tax_percentage=Decimal('24.00'),
        order=order
    )
    return order