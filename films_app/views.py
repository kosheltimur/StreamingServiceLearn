from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .models import Film
from .forms import ReviewForm

# Create your views here.

def render_all_films(request: HttpRequest):
    all_films = Film.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success': True, 'message' : "Форма успішно відправлена"})
        else:
            pass
    else:
        form = ReviewForm()
    # 
    return render(
        request= request, 
        template_name = 'films_app/film.html',
        context= {
            "films": all_films,
            "form": form
        }
    )

def add_to_favourite(request: HttpRequest, film_pk: int):
    response = redirect("all_films")
    all_cookies = request.COOKIES.get("favourites")
    if all_cookies:
        if film_pk not in all_cookies:
            all_cookies += ' ' + str(film_pk)
    else:
        all_cookies = str(film_pk)
    response.set_cookie("favourites", all_cookies)
    return response 


def render_favourite_films(request):
    all_cookies = request.COOKIES.get("favourites")
    if all_cookies:
        list_favourites_pk =  all_cookies.split(" ")
        objects_favourite_films = Film.objects.filter(pk__in = list_favourites_pk)
    else:
        objects_favourite_films = []
    return render(request, 'films_app/favourite_film.html', {"objects_favourite_films": objects_favourite_films} )
# 
filter_now = []
# 
def get_by_filter(request, genre):
    global filter_now
    
    if genre in filter_now:
        filter_now.remove(genre)
    else:
        filter_now.append(genre)
    print(filter_now)
    
    if filter_now != []:
        films = Film.objects.filter(genre__in = filter_now)
    else:
        films = Film.objects.all()
    print(films)
    return render(request, "films_app/inclusion_tags/films_render.html", context={"films": films})