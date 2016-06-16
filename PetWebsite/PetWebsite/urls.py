from django.conf.urls import patterns, include, url
from django.contrib import admin
from PetWebsite.views import adopt,sssl,adopted,found,homepage,notice,lost,process,bringmedetail,takemehome,login,signup,contact,team,bringmedetail
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'petsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sssl/$', sssl),

    url(r'^sssl/homepage.html$', homepage),
    url(r'^sssl/adopt.html$', adopt),
    url(r'^sssl/adopted.html$', adopted),
    url(r'^sssl/notice.html$', notice),
    url(r'^sssl/found.html$', found),
    url(r'^sssl/lost.html$', lost),
    url(r'^sssl/process.html$', process),
    url(r'^sssl/login.html$', login),
    url(r'^sssl/signup.html$', signup),
    url(r'^sssl/takemehome.html$', takemehome),
    url(r'^sssl/bringmedetail.html$', bringmedetail),
    url(r'^sssl/team.html$', team),
    url(r'^sssl/contact.html$', contact),
    url(r'^sssl/bringmedetail.html$', bringmedetail),

)
