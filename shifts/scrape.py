from __future__ import absolute_import, unicode_literals

import os

import mechanicalsoup
import requests
from bs4 import BeautifulSoup
from celery import shared_task

from users.models import AreaToWorkModel, HospitalListModel

from .forms import ShiftForm
from .models import Shifts


def scrape_own_site():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('http://br-tm.herokuapp.com/account/login')
    browser.select_form()
    browser['username'] = os.environ.get(BRTMUSERNAME)
    browser['password'] = os.environ.get(BRTMPASSWORD)
    browser.submit_selected()
    source = browser.open('http://br-tm.herokuapp.com/shifts/')
    soup = BeautifulSoup(source.text, 'lxml')
    row = soup.find_all('td')
    row_list = []
    for cell in row:
        row_list.append(cell.text)
    for cell in range(0,len(row_list),5):
        s = Shifts()
        s.area = AreaToWorkModel.objects.get(area=row_list[cell])
        s.hospital = HospitalListModel.objects.get(hospital=row_list[cell+1])
        s.start_time = f'{row_list[cell+2][6:10]}{row_list[cell+2][2:5]}-{row_list[cell+2][:2]}{row_list[cell+2][10:]}'
        s.end_time = f'{row_list[cell+3][6:10]}{row_list[cell+3][2:5]}-{row_list[cell+3][:2]}{row_list[cell+3][10:]}'
        s.save()