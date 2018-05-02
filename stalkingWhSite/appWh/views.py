#from .models import
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
#from .forms import
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Count
import os
import sys
from selenium import webdriver
import math


def index(request):
    cwd = os.getcwd()
    driver = webdriver.Chrome(cwd+'/chromedriver')
    driver.get('http://web.whatsapp.com')
    qrCode = driver.find_element_by_class_name('_2EZ_m')
    qrCodeHtml=qrCode.get_attribute('innerHTML')


    return render(request, 'index.html', {'qrCodeHtml':qrCodeHtml})
