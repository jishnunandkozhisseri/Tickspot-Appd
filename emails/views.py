from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings

from emails.forms import EmailForms

import urllib2
import urllib
import sys
import datetime
import getpass
from xml.dom.minidom import parseString
from calendar import monthrange

# Create your views here.

def email_template_page(request):
	if request.method == "POST":
		form = EmailForms(request.POST)
		if form.is_valid():
			content_data = form.cleaned_data.get("content_data")
			print "------------->",content_data
			response = create_entry_to_tickspot(content_data)
			if response:
				print "Done..................."
	else:
		form = EmailForms()
	return render_to_response('emails/landing_page.html', locals(), context_instance=RequestContext(request))

def create_entry_to_tickspot(content_data):
	current_day = int(datetime.datetime.now().strftime("%d"))
	current_month = int(datetime.datetime.now().strftime("%m"))
	current_year = int(datetime.datetime.now().strftime("%Y"))
	date_from = datetime.datetime(current_year, current_month, current_day).date()
	dict_data = {'notes': content_data} 
	s = urllib.urlencode(dict_data)
	result = urllib2.urlopen("%s/create_entry?email=%s&password=%s&project_id=%s&task_id=%s&hours=%s&date=%s&%s" % (
            settings.API_ENDPOINT,
            settings.USERNAME,
            settings.PASSWORD,
            settings.PROJECT_ID,
            settings.TASK_ID,
            8,
            date_from.strftime("%Y%m%d"),
	    	s
        ))
        data = result.read()
        result.close()
        return True