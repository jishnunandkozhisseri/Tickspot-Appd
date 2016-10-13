from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings

from emails.forms import SomeForm
from django.core.mail import EmailMessage

import urllib2
import urllib
import sys
import datetime
import getpass
from xml.dom.minidom import parseString
from calendar import monthrange
import re

# Create your views here.
TAG_RE = re.compile(r'<[^>]+>')

def email_template_page(request):
	if request.method == "POST":
		form = SomeForm(request.POST)
		if form.is_valid():
			content_data = form.cleaned_data.get("foo")
			tick_time = form.cleaned_data.get("time")
			current_day = int(datetime.datetime.now().strftime("%d"))
			current_month = int(datetime.datetime.now().strftime("%m"))
			current_year = int(datetime.datetime.now().strftime("%Y"))
			date_from = datetime.datetime(current_year, current_month, current_day).date()
			email_subject = "Status Update "+ str(date_from)
			body_header = "<div>Hi John,</div><p>Please find the updates on my task for "+ str(date_from) +"<br></p>"
			body_footer = "<p><span>Thanks &amp; Regards<div><br></div><div>Jishnunand P K</div><div>+91 9995599449</div></span><br></p>"
			body = body_header + content_data + body_footer
			email = EmailMessage(email_subject, body, to=['jishnunand@gmail.com'], cc=["sushma.shetty305@gmail.com"])
			email.content_subtype = 'html'
			response = email.send()
			if response:
				s = remove_tags(content_data)
				res = create_entry_to_tickspot(s, tick_time, date_from)
				print "Done..................."
	else:
		try:
			form = SomeForm()
		except Exception, e:
			print e
	return render_to_response('emails/landing_page.html', locals(), context_instance=RequestContext(request))

def create_entry_to_tickspot(content_data, tick_time, date_from):
	dict_data = {'notes': content_data} 
	encode_data = urllib.urlencode(dict_data)
	result = urllib2.urlopen("%s/create_entry?email=%s&password=%s&project_id=%s&task_id=%s&hours=%s&date=%s&%s" % (
            settings.API_ENDPOINT,
            settings.USERNAME,
            settings.PASSWORD,
            settings.PROJECT_ID,
            settings.TASK_ID,
            tick_time,
            date_from.strftime("%Y%m%d"),
	    	encode_data
        ))	
	data = result.read()
	result.close()
	return True


def remove_tags(text):
	return TAG_RE.sub('\n', text)