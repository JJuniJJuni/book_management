from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from users.views import check_email

from .models import Book
from .models import BookInfo


@method_decorator(login_required, name='dispatch')
@method_decorator(check_email, name='dispatch')
class BookList(View):
    def get(self, request):
        paginator = Paginator(Book.objects.all().order_by('id'), 10)
        page = request.GET.get('page')
        books = paginator.get_page(page)
        return render(request, 'list.html', {
            'books': books,
        })


@method_decorator(login_required, name='dispatch')
@method_decorator(check_email, name='dispatch')
class BookData(View):
    def get(self, request, book_id):
        try:
            info = BookInfo.objects.get(book=book_id)
        except ObjectDoesNotExist:
            name = Book.objects.get(id=book_id).name
            messages.error(request, "'{}'의 해당 상세 정보가 없습니다.".format(name))
            return redirect(reverse('list'))
        else:
            return render(request, 'info.html', context={
                'info': info
            })
