# book_orders/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookOrderForm
from .models import Book

def book_order(request):
    if request.method == 'POST':
        form = BookOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookOrderForm()

    return render(request, 'book_orders/book_order.html', {'form': form})

def load_books(request):
    selected_class_id = request.GET.get('selected_class')
    books = Book.objects.filter(available_classes__id=selected_class_id)
    return JsonResponse(list(books.values('id', 'name', 'price')), safe=False)

def success(request):
    return render(request, 'book_orders/success.html')
