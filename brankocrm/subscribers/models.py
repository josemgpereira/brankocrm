from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import stripe


class Subscriber(models.Model):
    user_rec = models.ForeignKey(User)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return u"%s Subscription Info" % self.user_rec

    def charge(self, request, email, fee):

        stripe.api_key = settings.STRIPE_SECRET_KEY

        token = request.POST['stripeToken']

        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        self.stripe_id = stripe_customer.id
        self.save()

        stripe.Charge.create(
            amount=fee,
            currency="usd",
            customer=stripe_customer.id
        )

        return stripe_customer
