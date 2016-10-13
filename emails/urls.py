from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tickspotappd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^landing/', 'emails.views.email_template_page'),
    url(r'^summernote/', include('django_summernote.urls')),

)