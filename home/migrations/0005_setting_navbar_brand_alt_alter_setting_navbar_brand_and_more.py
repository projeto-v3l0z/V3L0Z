# Generated by Django 5.0 on 2023-12-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_socialmedia_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='navbar_brand_alt',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Texto Alternativo da Logo da Navbar'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='navbar_brand',
            field=models.ImageField(blank=True, null=True, upload_to='home/images/logos', verbose_name='Logo da Navbar'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='social_network',
            field=models.CharField(choices=[('alexa', 'Alexa'), ('behance', 'Behance'), ('discord', 'Discord'), ('dribbble', 'Dribbble'), ('facebook', 'Facebook'), ('github', 'Github'), ('gitlab', 'Gitlab'), ('google', 'Google'), ('instagram', 'Instagram'), ('line', 'Line'), ('linkedin', 'Linkedin'), ('mastodon', 'Mastodon'), ('medium', 'Medium'), ('messenger', 'Messenger'), ('microsoft-teams', 'Microsoft Teams'), ('opencollective', 'Opencollective'), ('paypal', 'Paypal'), ('pinterest', 'Pinterest'), ('quora', 'Quora'), ('reddit', 'Reddit'), ('signal', 'Signal'), ('sina-weibo', 'Sina Weibo'), ('skype', 'Skype'), ('slack', 'Slack'), ('snapchat', 'Snapchat'), ('sourceforge', 'Sourceforge'), ('spotify', 'Spotify'), ('stack-overflow', 'Stack Overflow'), ('strava', 'Strava'), ('substack', 'Substack'), ('telegram', 'Telegram'), ('tencent-qq', 'Tencent QQ'), ('threads', 'Threads'), ('threads-fill', 'Threads Fill'), ('tiktok', 'Tiktok'), ('twitch', 'Twitch'), ('twitter', 'Twitter'), ('twitter-x', 'Twitter X'), ('vimeo', 'Vimeo'), ('wechat', 'Wechat'), ('whatsapp', 'Whatsapp'), ('wordpress', 'Wordpress'), ('yelp', 'Yelp'), ('youtube', 'Youtube'), ('link', 'Outra')], max_length=100, verbose_name='Rede Social'),
        ),
    ]
