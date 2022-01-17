# Generated by Django 3.2.6 on 2021-11-24 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название альбома')),
                ('songs_list', models.TextField(max_length=1024, verbose_name='Треклист')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='Описание появится позже', verbose_name='Описание')),
                ('stock', models.IntegerField(default=1, verbose_name='Наличие на складе')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('offer_of_the_week', models.BooleanField(default=False, verbose_name='Предложение недели')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField(default=0, verbose_name='Общеее кол-во товара')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('phone', models.CharField(max_length=20, verbose_name='Мобильный телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название жанра')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название медианосителя')),
            ],
            options={
                'verbose_name': 'Медианоситель',
                'verbose_name_plural': 'Медианосители',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя музыканта')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Музыкант',
                'verbose_name_plural': 'Музыканты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Мобильный телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ получен покупателем')], default='new', max_length=255, verbose_name='Статус заказа')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], max_length=255, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, max_length=255, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='MusicShop.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст уведомления')),
                ('read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.customer', verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='MusicShop.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='MusicShop.Album', verbose_name='Список ожидаемого'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Продукт корзины',
                'verbose_name_plural': 'Продукты корзины',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_cart', to='MusicShop.CartProduct', verbose_name='Продукты для корзины'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Исполнитель/группа')),
                ('slug', models.SlugField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.genre')),
                ('members', models.ManyToManyField(related_name='artist', to='MusicShop.Member', verbose_name='Участник')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.artist', verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='album',
            name='media_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicShop.mediatype', verbose_name='Носитель'),
        ),
    ]
