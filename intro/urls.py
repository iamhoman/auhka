from django.urls import path

from intro.views import auhka, committee, intro, auhka_docs

app_name = 'intro'

urlpatterns = [
    path('auhka/', auhka, name='auhka'),
    path('committee/', committee, name='committee'),
    path('intro/', intro, name='intro'),
    path('auhka_docs/', auhka_docs, name='auhka_docs'),
]