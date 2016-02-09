from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from .forms import ContactForm
from django.shortcuts import get_object_or_404
from brankocrm.accounts.models import Account


@login_required()
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)

    return render(request, 'contacts/contact_detail.html', {'contact': contact})


@login_required()
def contact_cru(request, uuid=None, account=None):
    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        if contact.owner != request.user:
            return HttpResponseForbidden()
    else:
        contact = Contact(owner=request.user)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            if request.is_ajax():
                return render(request, 'contacts/contact_item_view.html', {'account': account, 'contact': contact})
            else:
                reverse_url = reverse('brankocrm.accounts.views.account_detail',args=(account.uuid,))
                return HttpResponseRedirect(reverse_url)
    else:
        form = ContactForm(instance=contact)

    if request.GET.get('account', ''):
        account = Account.objects.get(id=request.GET.get('account', ''))

    variables = {
        'form': form,
        'contact': contact,
        'account': account
    }

    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
        template = 'contacts/contact_cru.html'

    return render(request, template, variables)
