import csv
import string

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact, Category

#Lista os contatos visíveis do mais novo para o mais antigo
@login_required(login_url='contact:login')
def index(request):
    category_id = request.GET.get('category')
    letter = request.GET.get('letter')
    
    contacts = Contact.objects.filter(show=True, owner=request.user)

    if category_id:
        contacts = contacts.filter(category_id=category_id)
    
    if letter:
        contacts = contacts.filter(last_name__istartswith=letter)

    contacts = contacts.order_by('-id')
    categories = Category.objects.all()

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
        'categories': categories,
        'alphabet': string.ascii_uppercase,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

# Filtra contatos
@login_required(login_url='contact:login')
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True, owner=request.user)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

#Busca pelo ID
@login_required(login_url='contact:login')
def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

@login_required(login_url='contact:login')
def export_contacts(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="meus_contatos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Sobrenome', 'Telefone', 'Email', 'Criado em'])

    contacts = Contact.objects.filter(show=True, owner=request.user).order_by('-id')
    for contact in contacts:
        writer.writerow([
            contact.first_name,
            contact.last_name,
            contact.phone,
            contact.email,
            contact.created_date.strftime('%d/%m/%Y %H:%M')
        ])

    return response

@login_required(login_url='contact:login')
def dashboard(request):
    user_contacts = Contact.objects.filter(owner=request.user)
    
    total_contacts = user_contacts.count()
    
    # Conta quantos contatos possuem foto cadastrada
    total_with_picture = user_contacts.exclude(picture='').exclude(picture__isnull=True).count()
    
    category_data = user_contacts \
        .values('category__name') \
        .annotate(total=Count('id')) \
        .order_by('-total')

    latest_contacts = user_contacts.order_by('-id')[:5]

    context = {
        'total_contacts': total_contacts,
        'total_with_picture': total_with_picture,
        'category_data': category_data,
        'latest_contacts': latest_contacts,
        'site_title': 'Dashboard - '
    }

    return render(request, 'contact/dashboard.html', context)
