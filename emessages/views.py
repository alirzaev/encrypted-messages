import cryptocode
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CreateEncryptedMessageForm, DecryptEncryptedMessageForm
from .models import EncryptedMessage


class MessageCreateView(FormView):
    form_class = CreateEncryptedMessageForm

    template_name = 'index.html'

    def form_valid(self, form):
        plain_text = form.cleaned_data['message']
        password = form.cleaned_data['password']

        encrypted_text = cryptocode.encrypt(plain_text, password)
        message = EncryptedMessage.objects.create(encrypted_text=encrypted_text)

        return redirect(reverse_lazy('message_decrypt', args=[message.id]))


class MessageDecryptView(FormView):
    form_class = DecryptEncryptedMessageForm

    template_name = 'message_decrypt.html'

    def get_form(self, form_class=None):
        message_id = self.kwargs['pk']
        _ = get_object_or_404(EncryptedMessage, pk=message_id)
        
        return super().get_form(form_class=form_class)


    def form_valid(self, form):
        message_id = self.kwargs['pk']
        password = form.cleaned_data['password']

        encrypted_text = get_object_or_404(EncryptedMessage, pk=message_id).encrypted_text
        plain_text = cryptocode.decrypt(encrypted_text, password)

        if not plain_text:
            form.add_error('password', 'Invalid password')

            return self.form_invalid(form)

        return render(self.request, 'message_decrypted.html', {
            'message': plain_text
        })
