import csv
import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact

#enviou o formulário, valida os dados e define o usuário logado como dono
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato criado com sucesso!')
            return redirect('contact:index')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

#Busca o contato (se for do usuário), carrega os dados atuais e salva 
@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('contact:index')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

#Verifica se o contato é do usuário e só apaga se houver a confirmação
@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contato excluído com sucesso!')
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )

@login_required(login_url='contact:login')
def import_contacts(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            messages.error(request, 'Por favor, envie um arquivo CSV válido.')
            return redirect('contact:index')

        try:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string) # Pula o cabeçalho

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                Contact.objects.create(
                    first_name=column[0],
                    last_name=column[1],
                    phone=column[2],
                    email=column[3],
                    show=True,
                    owner=request.user,
                )
            
            messages.success(request, 'Contatos importados com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao ler o arquivo: {e}')
        
        return redirect('contact:index')

    return render(
        request,
        'contact/import.html',
        {'site_title': 'Importar Contatos - '}
    )
