from django.db import models
from django.contrib.auth.models import User
import uuid

from django.utils import timezone


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField('Criado em', default=timezone.now)
    updated = models.DateTimeField('Alterado em', auto_now=True)


class Profile(Base):
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "perfil do usuário {}".format(self.user)


class Catalog(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.ForeignKey('CatalogItem', on_delete=models.CASCADE, verbose_name='Titulo')
    comments = models.ManyToManyField('Comment', verbose_name='Comentarios', blank=True, null=True)

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class CatalogItem(Base):
    TYPE_CLASSIFICATION = (
        ('a', 'Anime'),
        ('s', 'Series'),
        ('m', 'Movie'),
        ('o', 'OVA'),
    )

    name = models.CharField('Nome', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.TextField('Resumo', max_length=1000)
    genre = models.ManyToManyField('Genre', verbose_name='Genero')
    classification_type = models.CharField('Tipo', max_length=1, choices=TYPE_CLASSIFICATION, blank=True, default='s')
    season = models.CharField('Temporada', max_length=50)
    episodes = models.IntegerField('Episodios Diponiveis')
    watched = models.IntegerField('Episodios Vistos')
    release = models.DateField('Data de lançamento')
    in_producing = models.BooleanField('Nova Temporada', blank=True)
    new_season_preview = models.BooleanField('Prevista Nova Temporada', blank=True)
    new_season_in = models.DateField('Data Nova Temporada', null=True, blank=True)
    image = models.ImageField('Capa')

    class Meta:
        verbose_name = 'Iten Catalogo'
        verbose_name_plural = 'Itens Catalogo'

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Genre(Base):
    name = models.CharField('Nome', max_length=200)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Language(Base):
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'idiomas'

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Author(Base):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobre nome', max_length=100)
    date_of_birth = models.DateField('Data de nascimento', null=True, blank=True)
    date_of_death = models.DateField('Data de falecimento', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Comment(Base):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name='Usuario')
    comment = models.CharField('Comentario', max_length=100)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        """String for representing the Model object."""
        return self.user
