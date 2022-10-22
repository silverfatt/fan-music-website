from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Participant, Album, Track, Photo

menu_base = [{'title': 'Участники группы',
         'url_name': "participants"},
             {'title': 'Альбомы',
         'url_name': "albums"},
             {'title': 'Галерея',
         'url_name': "gallery"},
             {'title': 'О группе',
         'url_name': 'about'},
             ]


class ExtendMenuMixin:
    def extend_menu(self):
        return [{'title': 'Войти', 'url_name': 'login'} if self.request.user.is_anonymous else {'title': 'Выйти',
                                                                                                'url_name': 'logout'}]


class MainPage(generic.TemplateView, ExtendMenuMixin):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Главная страница'
        return context


class AlbumsList(generic.ListView, ExtendMenuMixin):
    model = Album

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Альбомы'
        return context


class PatricipantsList(generic.ListView, ExtendMenuMixin):
    model = Participant

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Участники'
        return context


class ParticipantDetail(generic.DetailView, ExtendMenuMixin):
    model = Participant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Участники'
        return context


class AlbumDetail(LoginRequiredMixin, generic.View, ExtendMenuMixin):
    template_name = "main/album.html"
    login_url = "/login/"
    redirect_field_name = 'main_page'

    def get(self, request, *args, **kwargs):
        current_album = Album.objects.get(pk=self.kwargs['pk'])
        tracks = Track.objects.filter(album_id=self.kwargs['pk'])
        return render(request, self.template_name, {'menu': menu_base + self.extend_menu(), 'title': current_album.title, 'tracks': tracks,
                                                    'album': current_album})


class AboutView(generic.View, ExtendMenuMixin):
    template_name = "main/about.html"

    def get(self, request, *args, **kwargs):
        band_info = Participant.objects.filter(name='Sabaton').first()
        print(band_info.name)
        return render(request, self.template_name,
                      {'menu': menu_base + self.extend_menu(), 'title': "О группе", 'band': band_info})


class PhotoList(generic.ListView, ExtendMenuMixin):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Галерея'
        return context


class PhotoDetail(generic.DetailView, ExtendMenuMixin):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_base + self.extend_menu()
        context['title'] = 'Галерея'
        return context
