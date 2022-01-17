from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericTabularInline


from .models import *


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    model = Member
    readonly_fields = ('image_url',)


class MembersInline(TabularInline):

    model = Artist.members.through


class ImageGalleryInline(GenericTabularInline):

    model = ImageGallery
    readonly_fields = ('image_url',)


@admin.register(Album)
class ArtistAlbum(admin.ModelAdmin):

    inlines = [ImageGalleryInline]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    inlines = [MembersInline, ImageGalleryInline]
    exclude = ('members',)


admin.site.register(MediaType)
admin.site.register(Genre)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Notification)
admin.site.register(ImageGallery)

