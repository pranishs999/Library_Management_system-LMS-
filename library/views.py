from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Patron, Borrow
from .forms import BookForm, BorrowForm, PatronForm

# Home View
class HomeView(TemplateView):
    template_name = 'home.html'

# List Views
class BookListViews(ListView):
    template_name = "book_list.html"
    model = Book
    context_object_name = 'books'
    
class PatronListViews(ListView):
    template_name = "patron_list.html"
    model = Patron
    context_object_name = 'patrons'
    
class BorrowListViews(ListView):
    template_name = "borrow_list.html"
    model = Borrow
    context_object_name = 'borrows'

# Create Views
class AddBookViews(CreateView):
    template_name = "add_book.html"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

class AddPatronViews(CreateView):
    template_name = "add_user.html"
    model = Patron
    form_class = PatronForm
    success_url = reverse_lazy('patron_list')

class AddBorrowViews(CreateView):
    template_name = "add_borrow.html"
    model = Borrow
    form_class = BorrowForm
    success_url = reverse_lazy('borrow_list')

# Edit Views
class EditBookViews(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title', 'author', 'isbn', 'category', 'total_copies', 'available_copies', 'published_date']
    success_url = reverse_lazy('book_list')

class EditPatronViews(UpdateView):
    model = Patron
    template_name = 'edit_patron.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('patron_list')

class EditBorrowViews(UpdateView):
    model = Borrow
    template_name = 'edit_borrow.html'
    fields = ['borrow_date', 'return_date']
    success_url = reverse_lazy('borrow_list')

# Delete Views
class DeleteBookViews(DeleteView):
    model = Book
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('book_list')

class DeleteBorrowViews(DeleteView):
    model = Borrow
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('borrow_list')

class DeletePatronViews(DeleteView):
    model = Patron
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('patron_list')

# Search Views
def search_patron(request):
    if 'membership_id' in request.GET:
        membership_id = request.GET['membership_id']
        patron = Patron.objects.filter(membership_id=membership_id)
        return render(request, 'search_patron.html', {'patron': patron})
    return render(request, 'search_patron.html')

def search_borrow_by_user_and_book(request):
    if 'membership_id' in request.GET and 'isbn' in request.GET:
        membership_id = request.GET['membership_id']
        isbn = request.GET['isbn']
        patron = Patron.objects.get(membership_id=membership_id)
        book = Book.objects.get(isbn=isbn)
        borrow = Borrow.objects.filter(patron=patron, book=book)
        return render(request, 'search_borrow.html', {'borrow': borrow})
    return render(request, 'search_borrow.html')

# Dashboard View
def dashboard(request):
    total_books = Book.objects.count()
    total_patrons = Patron.objects.count()
    borrowed_books = Borrow.objects.filter(return_date__isnull=True)  # Books that are not returned yet
    return render(request, 'dashboard.html', {
        'total_books': total_books,
        'total_patrons': total_patrons,
        'borrowed_books': borrowed_books
    })
