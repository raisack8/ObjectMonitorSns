from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('main.urls')),
]



# 大元のurlsに記載することで、どのアプリケーションを使うかを指定しているっぽい。
# ＵＲＬの文字列について、どのアプリを呼びだすかを決定している

# path('account/', include('django.contrib.auth.urls')),
# 上の1行を追加すればDjangoに元から備わっているログイン機能を使える
# 自分でカスタマイズしたい場合は生きているソースを見る。