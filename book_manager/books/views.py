from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BookForm
from .models import Book

# Create your views here.

# daftar buku pakai listView
class BookListView(ListView):
    model = Book 
    template_name = 'book_list.html' # template yang dipakai
    context_object_name = 'books' # nama variabel yang dipakai di template
    paginate_by = 10  # untuk paginasi

    # buat mencari data-nya
    def get_queryset(self): 
        query = self.request.GET.get('search') # ambil data dari form search
        if query:
            return Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
        return Book.objects.all() # kalau ngga ada data yang dicari, tampilkan semua data

# buat tambahin buku pakai CreateView
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'  # template yang dipakai
    success_url = '/books/' # masuk ke halaman daftar buku
    form_class = BookForm # form yang dipakai dari forms.py

    def form_valid(self, form): 
        return super().form_valid(form) # ngecek form

# buat update buku pakai UpdateView
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    form_class = BookForm # form yang dipakai dari forms.py
    success_url = reverse_lazy('book_list') # kalau confirm, masuk ke halaman daftar buku

# buat delete buku pakai DeleteView
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list') # kalau confirm, masuk ke halaman daftar buku