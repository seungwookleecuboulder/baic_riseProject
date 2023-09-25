from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Subject, Poverty, Interview
from .forms import SubjectForm, CSVUploadForm, InterviewForm
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta, date
import calendar

import io
import zipfile
import csv

## views
def poverty_list(request):
    povertylines = Poverty.objects.all()
    return render(request, 'poverty_list.html', {'povertylines': povertylines})
def poverty_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rise_project_povertylines.csv"'

    writer = csv.writer(response)
    writer.writerow(['year', 'familysize', 'old', 'adult', 'kid', 'pline'])

    queryset = Poverty.objects.all()
    for row in queryset:
        writer.writerow([row.year, row.familysize, row.old, row.adult, row.kid, row.pline])

    return response
def poverty_upload(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            header = next(csv_data) # header

            for row in csv_data:
                year = row[0]
                familysize = row[1]
                old = row[2]
                adult = row[3]
                kid = row[4]
                pline = row[5]
                try:
                    poverty = Poverty.objects.get(year=year, familysize=familysize, old=old, adult=adult, kid=kid)
                    pass
                except ObjectDoesNotExist:
                    Poverty.objects.create(
                        year=year,
                        familysize=familysize,
                        old=old,
                        adult=adult,
                        kid=kid,
                        pline=pline
                    )
            return redirect('/povertyList')
    else:
        form = CSVUploadForm()

    return render(request, 'poverty_upload.html', {'form': form})
def poverty_delete(request, year):
    objs = Poverty.objects.filter(year=year)
    objs.delete()
    return redirect('/povertyList')


def interview_list(request):
    interviews = Interview.objects.all()
    return render(request, 'interview_list.html', {'interviews': interviews})
def interview_new(request, interview_id=None):
    subject_id=None
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview_id = form.cleaned_data.get('interview_id')
            subject_id = form.cleaned_data.get('subject_id')
            if interview_id is not None and Interview.objects.filter(interview_id=interview_id).exists():
                form.add_error('interview_id', 'Interview ID already exists.')
            elif Subject.objects.filter(subject_id=subject_id).exists() is False:
                form.add_error('subject_id', 'Subject ID not exists.')
            else:
                Interview.objects.create(
                    interview_id=form.cleaned_data.get('interview_id'),
                    subject_id=form.cleaned_data.get('subject_id'),
                    researcher=form.cleaned_data.get('researcher'),
                    interview_type=form.cleaned_data.get('interview_type'),
                    interview_date=form.cleaned_data.get('interview_date'),
                    financial_supporter_type=form.data.get('financial_supporter_type'),
                    household_adult=form.data.get('household_adult'),
                    household_child=form.data.get('household_child'),
                    financial_familiy_adult=form.data.get('financial_familiy_adult') or 0,
                    financial_familiy_child=form.data.get('financial_familiy_child') or 0,
                    move_date=form.data.get('move_date') or None,
                    housing_comments=form.data.get('housing_comments') or None,
                    conception_date=form.data.get('conception_date') or None,
                    tri1_date=form.data.get('tri1_date') or None,
                    tri2_date=form.data.get('tri2_date') or None,
                    tri3_date=form.data.get('tri3_date') or None,
                    birth_date=form.data.get('birth_date') or None,
                    scan_date=form.data.get('scan_date') or None,
                    event_comments=form.data.get('event_comments') or None,

                    object_type_1=form.data.get('object_type_1') or None,
                    object_working_hour_1=form.data.get('object_working_hour_1') or None,
                    object_hourly_wage_1=form.data.get('object_hourly_wage_1') or None,
                    object_monthly_income_1=form.data.get('object_monthly_income_1') or None,
                    object_start_date_1=form.data.get('object_start_date_1') or None,
                    object_end_date_1=form.data.get('object_end_date_1') or None,
                    object_comment_1=form.data.get('object_comment_1') or None,

                    object_type_2=form.data.get('object_type_2') or None,
                    object_working_hour_2=form.data.get('object_working_hour_2') or None,
                    object_hourly_wage_2=form.data.get('object_hourly_wage_2') or None,
                    object_monthly_income_2=form.data.get('object_monthly_income_2') or None,
                    object_start_date_2=form.data.get('object_start_date_2') or None,
                    object_end_date_2=form.data.get('object_end_date_2') or None,
                    object_comment_2=form.data.get('object_comment_2') or None,

                    object_type_3=form.data.get('object_type_3') or None,
                    object_working_hour_3=form.data.get('object_working_hour_3') or None,
                    object_hourly_wage_3=form.data.get('object_hourly_wage_3') or None,
                    object_monthly_income_3=form.data.get('object_monthly_income_3') or None,
                    object_start_date_3=form.data.get('object_start_date_3') or None,
                    object_end_date_3=form.data.get('object_end_date_3') or None,
                    object_comment_3=form.data.get('object_comment_3') or None,

                    object_type_4=form.data.get('object_type_4') or None,
                    object_working_hour_4=form.data.get('object_working_hour_4') or None,
                    object_hourly_wage_4=form.data.get('object_hourly_wage_4') or None,
                    object_monthly_income_4=form.data.get('object_monthly_income_4') or None,
                    object_start_date_4=form.data.get('object_start_date_4') or None,
                    object_end_date_4=form.data.get('object_end_date_4') or None,
                    object_comment_4=form.data.get('object_comment_4') or None,

                    object_type_5=form.data.get('object_type_5') or None,
                    object_working_hour_5=form.data.get('object_working_hour_5') or None,
                    object_hourly_wage_5=form.data.get('object_hourly_wage_5') or None,
                    object_monthly_income_5=form.data.get('object_monthly_income_5') or None,
                    object_start_date_5=form.data.get('object_start_date_5') or None,
                    object_end_date_5=form.data.get('object_end_date_5') or None,
                    object_comment_5=form.data.get('object_comment_5') or None,

                    object_type_6=form.data.get('object_type_6') or None,
                    object_working_hour_6=form.data.get('object_working_hour_6') or None,
                    object_hourly_wage_6=form.data.get('object_hourly_wage_6') or None,
                    object_monthly_income_6=form.data.get('object_monthly_income_6') or None,
                    object_start_date_6=form.data.get('object_start_date_6') or None,
                    object_end_date_6=form.data.get('object_end_date_6') or None,
                    object_comment_6=form.data.get('object_comment_6') or None,

                    object_type_7=form.data.get('object_type_7') or None,
                    object_working_hour_7=form.data.get('object_working_hour_7') or None,
                    object_hourly_wage_7=form.data.get('object_hourly_wage_7') or None,
                    object_monthly_income_7=form.data.get('object_monthly_income_7') or None,
                    object_start_date_7=form.data.get('object_start_date_7') or None,
                    object_end_date_7=form.data.get('object_end_date_7') or None,
                    object_comment_7=form.data.get('object_comment_7') or None,

                    object_type_8=form.data.get('object_type_8') or None,
                    object_working_hour_8=form.data.get('object_working_hour_8') or None,
                    object_hourly_wage_8=form.data.get('object_hourly_wage_8') or None,
                    object_monthly_income_8=form.data.get('object_monthly_income_8') or None,
                    object_start_date_8=form.data.get('object_start_date_8') or None,
                    object_end_date_8=form.data.get('object_end_date_8') or None,
                    object_comment_8=form.data.get('object_comment_8') or None,

                    object_type_9=form.data.get('object_type_9') or None,
                    object_working_hour_9=form.data.get('object_working_hour_9') or None,
                    object_hourly_wage_9=form.data.get('object_hourly_wage_9') or None,
                    object_monthly_income_9=form.data.get('object_monthly_income_9') or None,
                    object_start_date_9=form.data.get('object_start_date_9') or None,
                    object_end_date_9=form.data.get('object_end_date_9') or None,
                    object_comment_9=form.data.get('object_comment_9') or None,

                    object_type_10=form.data.get('object_type_10') or None,
                    object_working_hour_10=form.data.get('object_working_hour_10') or None,
                    object_hourly_wage_10=form.data.get('object_hourly_wage_10') or None,
                    object_monthly_income_10=form.data.get('object_monthly_income_10') or None,
                    object_start_date_10=form.data.get('object_start_date_10') or None,
                    object_end_date_10=form.data.get('object_end_date_10') or None,
                    object_comment_10=form.data.get('object_comment_10') or None,
                )
                return redirect('/interviewList')
    else:
        form = InterviewForm()

    if interview_id is not None:
        parts = interview_id.split('_')
        if len(parts) > 0:
            subject_id = parts[0]

    return render(request, 'interview_new.html', {'form': form, 'interview_id': interview_id, 'subject_id': subject_id})
def interview_update(request, interview_id):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        try:
            interview = Interview.objects.get(interview_id=interview_id)
            Interview.objects.filter(interview_id=interview_id).update(
                researcher=form.data.get('researcher'),
                interview_type=form.data.get('interview_type'),
                interview_date=form.data.get('interview_date'),
                financial_supporter_type=form.data.get('financial_supporter_type'),
                household_adult=form.data.get('household_adult'),
                household_child=form.data.get('household_child'),
                financial_familiy_adult=form.data.get('financial_familiy_adult') or 0,
                financial_familiy_child=form.data.get('financial_familiy_child') or 0,
                move_date=form.data.get('move_date') or None,
                housing_comments=form.data.get('housing_comments') or None,
                conception_date=form.data.get('conception_date') or None,
                tri1_date=form.data.get('tri1_date') or None,
                tri2_date=form.data.get('tri2_date') or None,
                tri3_date=form.data.get('tri3_date') or None,
                birth_date=form.data.get('birth_date') or None,
                scan_date=form.data.get('scan_date') or None,
                event_comments=form.data.get('event_comments') or None,

                object_type_1=form.data.get('object_type_1') or None,
                object_working_hour_1=form.data.get('object_working_hour_1') or None,
                object_hourly_wage_1=form.data.get('object_hourly_wage_1') or None,
                object_monthly_income_1=form.data.get('object_monthly_income_1') or None,
                object_start_date_1=form.data.get('object_start_date_1') or None,
                object_end_date_1=form.data.get('object_end_date_1') or None,
                object_comment_1=form.data.get('object_comment_1') or None,

                object_type_2=form.data.get('object_type_2') or None,
                object_working_hour_2=form.data.get('object_working_hour_2') or None,
                object_hourly_wage_2=form.data.get('object_hourly_wage_2') or None,
                object_monthly_income_2=form.data.get('object_monthly_income_2') or None,
                object_start_date_2=form.data.get('object_start_date_2') or None,
                object_end_date_2=form.data.get('object_end_date_2') or None,
                object_comment_2=form.data.get('object_comment_2') or None,

                object_type_3=form.data.get('object_type_3') or None,
                object_working_hour_3=form.data.get('object_working_hour_3') or None,
                object_hourly_wage_3=form.data.get('object_hourly_wage_3') or None,
                object_monthly_income_3=form.data.get('object_monthly_income_3') or None,
                object_start_date_3=form.data.get('object_start_date_3') or None,
                object_end_date_3=form.data.get('object_end_date_3') or None,
                object_comment_3=form.data.get('object_comment_3') or None,

                object_type_4=form.data.get('object_type_4') or None,
                object_working_hour_4=form.data.get('object_working_hour_4') or None,
                object_hourly_wage_4=form.data.get('object_hourly_wage_4') or None,
                object_monthly_income_4=form.data.get('object_monthly_income_4') or None,
                object_start_date_4=form.data.get('object_start_date_4') or None,
                object_end_date_4=form.data.get('object_end_date_4') or None,
                object_comment_4=form.data.get('object_comment_4') or None,

                object_type_5=form.data.get('object_type_5') or None,
                object_working_hour_5=form.data.get('object_working_hour_5') or None,
                object_hourly_wage_5=form.data.get('object_hourly_wage_5') or None,
                object_monthly_income_5=form.data.get('object_monthly_income_5') or None,
                object_start_date_5=form.data.get('object_start_date_5') or None,
                object_end_date_5=form.data.get('object_end_date_5') or None,
                object_comment_5=form.data.get('object_comment_5') or None,

                object_type_6=form.data.get('object_type_6') or None,
                object_working_hour_6=form.data.get('object_working_hour_6') or None,
                object_hourly_wage_6=form.data.get('object_hourly_wage_6') or None,
                object_monthly_income_6=form.data.get('object_monthly_income_6') or None,
                object_start_date_6=form.data.get('object_start_date_6') or None,
                object_end_date_6=form.data.get('object_end_date_6') or None,
                object_comment_6=form.data.get('object_comment_6') or None,

                object_type_7=form.data.get('object_type_7') or None,
                object_working_hour_7=form.data.get('object_working_hour_7') or None,
                object_hourly_wage_7=form.data.get('object_hourly_wage_7') or None,
                object_monthly_income_7=form.data.get('object_monthly_income_7') or None,
                object_start_date_7=form.data.get('object_start_date_7') or None,
                object_end_date_7=form.data.get('object_end_date_7') or None,
                object_comment_7=form.data.get('object_comment_7') or None,

                object_type_8=form.data.get('object_type_8') or None,
                object_working_hour_8=form.data.get('object_working_hour_8') or None,
                object_hourly_wage_8=form.data.get('object_hourly_wage_8') or None,
                object_monthly_income_8=form.data.get('object_monthly_income_8') or None,
                object_start_date_8=form.data.get('object_start_date_8') or None,
                object_end_date_8=form.data.get('object_end_date_8') or None,
                object_comment_8=form.data.get('object_comment_8') or None,

                object_type_9=form.data.get('object_type_9') or None,
                object_working_hour_9=form.data.get('object_working_hour_9') or None,
                object_hourly_wage_9=form.data.get('object_hourly_wage_9') or None,
                object_monthly_income_9=form.data.get('object_monthly_income_9') or None,
                object_start_date_9=form.data.get('object_start_date_9') or None,
                object_end_date_9=form.data.get('object_end_date_9') or None,
                object_comment_9=form.data.get('object_comment_9') or None,

                object_type_10=form.data.get('object_type_10') or None,
                object_working_hour_10=form.data.get('object_working_hour_10') or None,
                object_hourly_wage_10=form.data.get('object_hourly_wage_10') or None,
                object_monthly_income_10=form.data.get('object_monthly_income_10') or None,
                object_start_date_10=form.data.get('object_start_date_10') or None,
                object_end_date_10=form.data.get('object_end_date_10') or None,
                object_comment_10=form.data.get('object_comment_10') or None,
            )
            return redirect('/interviewList')
        except ObjectDoesNotExist:
            return redirect('/interviewNew/' + interview_id)
    else:
        try:
            interview = Interview.objects.get(interview_id=interview_id)
            form = InterviewForm(instance=interview)
            return render(request, 'interview_update.html', {'form': form})
        except ObjectDoesNotExist:
            return redirect('/interviewNew/' + interview_id)
    return redirect('/interviewList')
def interview_delete(request, interview_id):
    obj = Interview.objects.get(interview_id=interview_id)
    obj.delete()
    return redirect('/interviewList')
def interview_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rise_project_interviews.csv"'

    writer = csv.writer(response)
    writer.writerow(['interview_id', 'subject_id', 'researcher', 'interview_type', 'interview_date', 'financial_supporter_type',
                   'household_adult', 'household_child', 'financial_familiy_adult', 'financial_familiy_child', 'move_date', 'housing_comments',
                   'conception_date', 'tri1_date', 'tri2_date', 'tri3_date', 'birth_date', 'scan_date', 'event_comments',
                   'object_type_1', 'object_working_hour_1', 'object_hourly_wage_1', 'object_monthly_income_1', 'object_start_date_1', 'object_end_date_1', 'object_comment_1',
                   'object_type_2', 'object_working_hour_2', 'object_hourly_wage_2', 'object_monthly_income_2', 'object_start_date_2', 'object_end_date_2', 'object_comment_2',
                   'object_type_3', 'object_working_hour_3', 'object_hourly_wage_3', 'object_monthly_income_3', 'object_start_date_3', 'object_end_date_3', 'object_comment_3',
                   'object_type_4', 'object_working_hour_4', 'object_hourly_wage_4', 'object_monthly_income_4', 'object_start_date_4', 'object_end_date_4', 'object_comment_4',
                   'object_type_5', 'object_working_hour_5', 'object_hourly_wage_5', 'object_monthly_income_5', 'object_start_date_5', 'object_end_date_5', 'object_comment_5',
                   'object_type_6', 'object_working_hour_6', 'object_hourly_wage_6', 'object_monthly_income_6', 'object_start_date_6', 'object_end_date_6', 'object_comment_6',
                   'object_type_7', 'object_working_hour_7', 'object_hourly_wage_7', 'object_monthly_income_7', 'object_start_date_7', 'object_end_date_7', 'object_comment_7',
                   'object_type_8', 'object_working_hour_8', 'object_hourly_wage_8', 'object_monthly_income_8', 'object_start_date_8', 'object_end_date_8', 'object_comment_8',
                   'object_type_9', 'object_working_hour_9', 'object_hourly_wage_9', 'object_monthly_income_9', 'object_start_date_9', 'object_end_date_9', 'object_comment_9',
                   'object_type_10', 'object_working_hour_10', 'object_hourly_wage_10', 'object_monthly_income_10', 'object_start_date_10', 'object_end_date_10', 'object_comment_10'])

    queryset = Interview.objects.all()
    for row in queryset:
        writer.writerow([
            row.interview_id, row.subject_id, row.researcher, row.interview_type, row.interview_date, row.financial_supporter_type,
            row.household_adult, row.household_child, row.financial_familiy_adult, row.financial_familiy_child, row.move_date, row.housing_comments,
            row.conception_date, row.tri1_date, row.tri2_date, row.tri3_date, row.birth_date, row.scan_date, row.event_comments,
            row.object_type_1, row.object_working_hour_1, row.object_hourly_wage_1, row.object_monthly_income_1,
            row.object_start_date_1, row.object_end_date_1, row.object_comment_1,
            row.object_type_2, row.object_working_hour_2, row.object_hourly_wage_2, row.object_monthly_income_2,
            row.object_start_date_2, row.object_end_date_2, row.object_comment_2,
            row.object_type_3, row.object_working_hour_3, row.object_hourly_wage_3, row.object_monthly_income_3,
            row.object_start_date_3, row.object_end_date_3, row.object_comment_3,
            row.object_type_4, row.object_working_hour_4, row.object_hourly_wage_4, row.object_monthly_income_4,
            row.object_start_date_4, row.object_end_date_4, row.object_comment_4,
            row.object_type_5, row.object_working_hour_5, row.object_hourly_wage_5, row.object_monthly_income_5,
            row.object_start_date_5, row.object_end_date_5, row.object_comment_5,
            row.object_type_6, row.object_working_hour_6, row.object_hourly_wage_6, row.object_monthly_income_6,
            row.object_start_date_6, row.object_end_date_6, row.object_comment_6,
            row.object_type_7, row.object_working_hour_7, row.object_hourly_wage_7, row.object_monthly_income_7,
            row.object_start_date_7, row.object_end_date_7, row.object_comment_7,
            row.object_type_8, row.object_working_hour_8, row.object_hourly_wage_8, row.object_monthly_income_8,
            row.object_start_date_8, row.object_end_date_8, row.object_comment_8,
            row.object_type_9, row.object_working_hour_9, row.object_hourly_wage_9, row.object_monthly_income_9,
            row.object_start_date_9, row.object_end_date_9, row.object_comment_9,
            row.object_type_10, row.object_working_hour_10, row.object_hourly_wage_10, row.object_monthly_income_10,
            row.object_start_date_10, row.object_end_date_10, row.object_comment_10
            ])

    return response
def interview_upload(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            header = next(csv_data) # header

            for row in csv_data:
                interview_id = row[0]
                subject_id = row[1]
                researcher = row[2]
                interview_type = row[3]
                interview_date = row[4]
                financial_supporter_type = row[5]
                household_adult = row[6]
                household_child = row[7]
                financial_familiy_adult = row[8]
                financial_familiy_child = row[9]
                housing_comments = row[10]
                move_date = row[11]
                conception_date = row[12]
                tri1_date = row[13]
                tri2_date = row[14]
                tri3_date = row[15]
                birth_date = row[16]
                scan_date = row[17]
                event_comments = row[18]
                object_type_1 = row[19]
                object_working_hour_1 = row[20]
                object_hourly_wage_1 = row[21]
                object_monthly_income_1 = row[22]
                object_start_date_1 = row[23]
                object_end_date_1 = row[24]
                object_comment_1 = row[25]
                object_type_2 = row[26]
                object_working_hour_2 = row[27]
                object_hourly_wage_2 = row[28]
                object_monthly_income_2 = row[29]
                object_start_date_2 = row[30]
                object_end_date_2 = row[31]
                object_comment_2 = row[32]
                object_type_3 = row[33]
                object_working_hour_3 = row[34]
                object_hourly_wage_3 = row[35]
                object_monthly_income_3 = row[36]
                object_start_date_3 = row[37]
                object_end_date_3 = row[38]
                object_comment_3 = row[39]
                object_type_4 = row[40]
                object_working_hour_4 = row[41]
                object_hourly_wage_4 = row[42]
                object_monthly_income_4 = row[43]
                object_start_date_4 = row[44]
                object_end_date_4 = row[45]
                object_comment_4 = row[46]
                object_type_5 = row[47]
                object_working_hour_5 = row[48]
                object_hourly_wage_5 = row[49]
                object_monthly_income_5 = row[50]
                object_start_date_5 = row[51]
                object_end_date_5 = row[52]
                object_comment_5 = row[53]
                object_type_6 = row[54]
                object_working_hour_6 = row[55]
                object_hourly_wage_6 = row[56]
                object_monthly_income_6 = row[57]
                object_start_date_6 = row[58]
                object_end_date_6 = row[59]
                object_comment_6 = row[60]
                object_type_7 = row[61]
                object_working_hour_7 = row[62]
                object_hourly_wage_7 = row[63]
                object_monthly_income_7 = row[64]
                object_start_date_7 = row[65]
                object_end_date_7 = row[66]
                object_comment_7 = row[67]
                object_type_8 = row[68]
                object_working_hour_8 = row[69]
                object_hourly_wage_8 = row[70]
                object_monthly_income_8 = row[71]
                object_start_date_8 = row[72]
                object_end_date_8 = row[73]
                object_comment_8 = row[74]
                object_type_9 = row[75]
                object_working_hour_9 = row[76]
                object_hourly_wage_9 = row[77]
                object_monthly_income_9 = row[78]
                object_start_date_9 = row[79]
                object_end_date_9 = row[80]
                object_comment_9 = row[81]
                object_type_10 = row[82]
                object_working_hour_10 = row[83]
                object_hourly_wage_10 = row[84]
                object_monthly_income_10 = row[85]
                object_start_date_10 = row[86]
                object_end_date_10 = row[87]
                object_comment_10 = row[88]
                try:
                    interview = Interview.objects.get(interview_id=interview_id)
                    pass
                except ObjectDoesNotExist:
                    Interview.objects.create(
                        interview_id=interview_id,
                        subject_id=subject_id or None,
                        researcher=researcher or None,
                        interview_type=interview_type or None,
                        interview_date=interview_date or None,
                        financial_supporter_type=financial_supporter_type or None,
                        household_adult=household_adult or None,
                        household_child=household_child or None,
                        financial_familiy_adult=financial_familiy_adult or None,
                        financial_familiy_child=financial_familiy_child or None,
                        housing_comments=housing_comments or None,
                        move_date=move_date or None,
                        conception_date=conception_date or None,
                        tri1_date=tri1_date or None,
                        tri2_date=tri2_date or None,
                        tri3_date=tri3_date or None,
                        birth_date=birth_date or None,
                        scan_date=scan_date or None,
                        event_comments=event_comments or None,
                        object_type_1=object_type_1 or None,
                        object_working_hour_1=object_working_hour_1 or None,
                        object_hourly_wage_1=object_hourly_wage_1 or None,
                        object_monthly_income_1=object_monthly_income_1 or None,
                        object_start_date_1=object_start_date_1 or None,
                        object_end_date_1=object_end_date_1 or None,
                        object_comment_1=object_comment_1 or None,
                        object_type_2=object_type_2 or None,
                        object_working_hour_2=object_working_hour_2 or None,
                        object_hourly_wage_2=object_hourly_wage_2 or None,
                        object_monthly_income_2=object_monthly_income_2 or None,
                        object_start_date_2=object_start_date_2 or None,
                        object_end_date_2=object_end_date_2 or None,
                        object_comment_2=object_comment_2 or None,
                        object_type_3=object_type_3 or None,
                        object_working_hour_3=object_working_hour_3 or None,
                        object_hourly_wage_3=object_hourly_wage_3 or None,
                        object_monthly_income_3=object_monthly_income_3 or None,
                        object_start_date_3=object_start_date_3 or None,
                        object_end_date_3=object_end_date_3 or None,
                        object_comment_3=object_comment_3 or None,
                        object_type_4=object_type_4 or None,
                        object_working_hour_4=object_working_hour_4 or None,
                        object_hourly_wage_4=object_hourly_wage_4 or None,
                        object_monthly_income_4=object_monthly_income_4 or None,
                        object_start_date_4=object_start_date_4 or None,
                        object_end_date_4=object_end_date_4 or None,
                        object_comment_4=object_comment_4 or None,
                        object_type_5=object_type_5 or None,
                        object_working_hour_5=object_working_hour_5 or None,
                        object_hourly_wage_5=object_hourly_wage_5 or None,
                        object_monthly_income_5=object_monthly_income_5 or None,
                        object_start_date_5=object_start_date_5 or None,
                        object_end_date_5=object_end_date_5 or None,
                        object_comment_5=object_comment_5 or None,
                        object_type_6=object_type_6 or None,
                        object_working_hour_6=object_working_hour_6 or None,
                        object_hourly_wage_6=object_hourly_wage_6 or None,
                        object_monthly_income_6=object_monthly_income_6 or None,
                        object_start_date_6=object_start_date_6 or None,
                        object_end_date_6=object_end_date_6 or None,
                        object_comment_6=object_comment_6 or None,
                        object_type_7=object_type_7 or None,
                        object_working_hour_7=object_working_hour_7 or None,
                        object_hourly_wage_7=object_hourly_wage_7 or None,
                        object_monthly_income_7=object_monthly_income_7 or None,
                        object_start_date_7=object_start_date_7 or None,
                        object_end_date_7=object_end_date_7 or None,
                        object_comment_7=object_comment_7 or None,
                        object_type_8=object_type_8 or None,
                        object_working_hour_8=object_working_hour_8 or None,
                        object_hourly_wage_8=object_hourly_wage_8 or None,
                        object_monthly_income_8=object_monthly_income_8 or None,
                        object_start_date_8=object_start_date_8 or None,
                        object_end_date_8=object_end_date_8 or None,
                        object_comment_8=object_comment_8 or None,
                        object_type_9=object_type_9 or None,
                        object_working_hour_9=object_working_hour_9 or None,
                        object_hourly_wage_9=object_hourly_wage_9 or None,
                        object_monthly_income_9=object_monthly_income_9 or None,
                        object_start_date_9=object_start_date_9 or None,
                        object_end_date_9=object_end_date_9 or None,
                        object_comment_9=object_comment_9 or None,
                        object_type_10=object_type_10 or None,
                        object_working_hour_10=object_working_hour_10 or None,
                        object_hourly_wage_10=object_hourly_wage_10 or None,
                        object_monthly_income_10=object_monthly_income_10 or None,
                        object_start_date_10=object_start_date_10 or None,
                        object_end_date_10=object_end_date_10 or None,
                        object_comment_10=object_comment_10 or None,
                    )
            return redirect('/interviewList')
    else:
        form = CSVUploadForm()

    return render(request, 'interview_upload.html', {'form': form})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})
def subject_new(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('subject_id')
            if id is not None and Subject.objects.filter(subject_id=id).exists():
                form.add_error('subject_id', 'Subject ID already exists.')
            else:
                Subject.objects.create(
                    subject_id=form.cleaned_data.get('subject_id'),
                    researcher=form.cleaned_data.get('researcher'),
                    pv1=form.cleaned_data.get('subject_id')+'_5126',
                    pv2=form.cleaned_data.get('subject_id')+'_5120',
                    pv3=form.cleaned_data.get('subject_id')+'_5109',
                    pn1=form.cleaned_data.get('subject_id')+'_5081',
                    pn4=form.cleaned_data.get('subject_id')+'_5018'
                )
                return redirect('/home')
    else:
        form = SubjectForm()
    return render(request, 'subject_new.html', {'form': form})
def subject_update(request, subject_id):
    subject = Subject.objects.get(subject_id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.clean_researcher_field():
            Subject.objects.filter(subject_id=subject_id).update(researcher=form.data.get('researcher'), )
            return redirect('/home')
    else:
        form = SubjectForm(instance=subject)
        return render(request, 'subject_update.html', {'form': form})
    return redirect('/home')
def subject_delete(request, subject_id):
    obj = Subject.objects.get(subject_id=subject_id)
    obj.delete()
    return redirect('/home')
def subject_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rise_project_subjects.csv"'

    writer = csv.writer(response)
    writer.writerow(['subject_id', 'researcher', 'pv1', 'pv2', 'pv3', 'pn1', 'pn4'])

    queryset = Subject.objects.all()
    for row in queryset:
        writer.writerow([row.subject_id, row.researcher, row.pv1, row.pv2, row.pv3, row.pn1, row.pn4])

    return response
def subject_upload(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            header = next(csv_data) # header

            for row in csv_data:
                subject_id = row[0]
                researcher = row[1]
                pv1 = row[2]
                pv2 = row[3]
                pv3 = row[4]
                pn1 = row[5]
                pn4 = row[6]
                try:
                    subject = Subject.objects.get(subject_id=subject_id)
                    pass
                except ObjectDoesNotExist:
                    Subject.objects.create(
                        subject_id=subject_id,
                        researcher=researcher,
                        pv1=subject_id+'_5126',
                        pv2=subject_id+'_5120',
                        pv3=subject_id+'_5109',
                        pn1=subject_id+'_5081',
                        pn4=subject_id+'_5018'
                    )
            return redirect('/home')
    else:
        form = CSVUploadForm()

    return render(request, 'subject_upload.html', {'form': form})
def subject_statics(request, subject_id=None):

    birth_date = get_birth_date(subject_id)
    conception_date = get_conception_date(subject_id)

    if birth_date is None and conception_date is not None:
        birth_date = add_months_to_date(conception_date, 9)
    if birth_date is not None and conception_date is None:
        conception_date = add_months_to_date(birth_date, -9)

    tri1_date = get_tri1_date(subject_id)
    tri2_date = get_tri2_date(subject_id)
    tri3_date = get_tri3_date(subject_id)

    if tri1_date is None:
        tri1_date = conception_date
    if tri2_date is None:
        tri2_date = add_months_to_date(tri1_date, 3)
    if tri3_date is None:
        tri3_date = add_months_to_date(tri2_date, 3)

    pv1_interview_date = get_interview_type_date(subject_id, 'pv1')
    pv2_interview_date = get_interview_type_date(subject_id, 'pv2')
    pv3_interview_date = get_interview_type_date(subject_id, 'pv3')
    pn1_interview_date = get_interview_type_date(subject_id, 'pn1')
    pn4_interview_date = get_interview_type_date(subject_id, 'pn4')

    scan_date = get_scan_date(subject_id)
    move_date = get_move_date(subject_id=subject_id)

    interviews = Interview.objects.filter(subject_id=subject_id)

    statics = []
    pre_conception_date = None

    for interview in interviews:
        # Start/End date setting.
        if interview.interview_type == 'pv1':
            work_start = add_months_to_date(birth_date, -12).date()
            pre_conception_date = work_start
            work_end = pv1_interview_date
        elif interview.interview_type == 'pv2':
            work_start = pv1_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pv2_interview_date
        elif interview.interview_type == 'pv3':
            work_start = pv2_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pv3_interview_date
        elif interview.interview_type == 'pn1':
            work_start = pv3_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pn1_interview_date
        elif interview.interview_type == 'pn4':
            work_start = pn1_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pn4_interview_date

        current_date = work_start
        while current_date <= work_end:
            event = ""
            moc_work_end = 0
            foc_work_end = 0
            moc_work_start = 0
            foc_work_start = 0
            year = current_date.year
            month = current_date.month
            moc_income = calculate_monthly_income(subject_id, year, month)['moc_income']
            foc_income = calculate_monthly_income(subject_id, year, month)['foc_income']
            monthly_income = moc_income + foc_income
            moc_work_end = calculate_monthly_income(subject_id, year, month)['moc_work_end']
            foc_work_end = calculate_monthly_income(subject_id, year, month)['foc_work_end']
            moc_work_start = calculate_monthly_income(subject_id, year, month)['moc_work_start']
            foc_work_start = calculate_monthly_income(subject_id, year, month)['foc_work_start']

            yearly_income = monthly_income * 12

            f_adult = interview.financial_familiy_adult
            h_adult = interview.household_adult
            if f_adult is None:
                f_adult = 0
            if h_adult is None:
                h_adult = 0
            adult = max(f_adult, h_adult)

            f_kid = interview.financial_familiy_child
            h_kid = interview.household_child
            if f_kid is None:
                f_kid = 0
            if h_kid is None:
                h_kid = 0
            kid = max(f_kid, h_kid)

            pline = Poverty.objects.get(year=year, familysize=adult+kid, adult=adult, kid=kid).pline
            inr = yearly_income / pline

            poverty_yn = 0
            if inr < 2:
                poverty_yn = 1

            # event check
            if birth_date is not None:
                if year == birth_date.year and month == birth_date.month:
                    event += "(Birth) (Tri3_end) "
            if conception_date is not None:
                if year == conception_date.year and month == conception_date.month:
                    event += "(Conception) "
            if tri1_date is not None:
                if year == tri1_date.year and month == tri1_date.month:
                    event += "(Tri1 Start) "
            if tri2_date is not None:
                if year == tri2_date.year and month == tri2_date.month:
                    event += "(Tri1 End) (Tri2 Start) "
            if tri3_date is not None:
                if year == tri3_date.year and month == tri3_date.month:
                    event += "(Tri2 End) (Tri3 Start) "
            if scan_date is not None:
                if year == scan_date.year and month == scan_date.month:
                    event += "(Scan) "
            if pv1_interview_date is not None:
                if year == pv1_interview_date.year and month == pv1_interview_date.month:
                    event += "(PV1) "
            if pv2_interview_date is not None:
                if year == pv2_interview_date.year and month == pv2_interview_date.month:
                    event += "(PV2) "
            if pv3_interview_date is not None:
                if year == pv3_interview_date.year and month == pv3_interview_date.month:
                    event += "(PV3) "
            if pn1_interview_date is not None:
                if year == pn1_interview_date.year and month == pn1_interview_date.month:
                    event += "(PN1) "
            if pn4_interview_date is not None:
                if year == pn4_interview_date.year and month == pn4_interview_date.month:
                    event += "(PN4) "
            move_yn = 0
            if move_date is not None:
                if year == move_date.year and month == move_date.month:
                    event += "(Move) "
                    move_yn = 1

            statics.append({'subject_id': subject_id, 'year': year, 'month': month, 'pline': pline, 'yearly_income': yearly_income, 'monthly_income': monthly_income, 'adult': adult, 'kid': kid, 'inr': inr, 'poverty_yn': poverty_yn, 'move_yn': move_yn, 'event': event, 'moc_work_end': moc_work_end, 'foc_work_end': foc_work_end, 'moc_work_start': moc_work_start, 'foc_work_start': foc_work_start})

            # move to next month.
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

    events = []
    events.append(calculate_events(pre_conception_date, conception_date, statics, "PRE_CONCEPTION-CONCEPTION"))
    events.append(calculate_events(conception_date, pv1_interview_date, statics, "CONCEPTION-PV1"))
    events.append(calculate_events(pv1_interview_date, pv2_interview_date, statics, "PV1-PV2"))
    events.append(calculate_events(pv2_interview_date, pv3_interview_date, statics, "PV2-PV3"))
    events.append(calculate_events(pv3_interview_date, pn1_interview_date, statics, "PV3-PN1"))
    events.append(calculate_events(pn1_interview_date, pn4_interview_date, statics, "PN1-PN4"))
    events.append(calculate_events(conception_date, tri2_date, statics, "1st TRIMESTER(Conception-Tri1End)"))
    events.append(calculate_events(tri2_date, tri3_date, statics, "2nd TRIMESTER(Tri2Start-Tri2End)"))
    events.append(calculate_events(tri3_date, birth_date, statics, "3rd TRIMESTER(Tri3Start-Tri3End)"))
    events.append(calculate_events(birth_date, scan_date, statics, "SCAN Postnatal(Birth-Scan)"))
    events.append(calculate_events(birth_date, pn1_interview_date, statics, "PN1 Postnatal(Birth-PN1)"))
    events.append(calculate_events(pn1_interview_date, pn4_interview_date, statics, "PN4 Postnatal(PN1-PN4)"))
    events.append(calculate_events(conception_date, birth_date, statics, "AVG PRENATAL(Conception-Birth)"))
    events.append(calculate_events(birth_date, pn4_interview_date, statics, "AVG POSTNATAL(Birth-PN4)"))
    events.append(calculate_events(pre_conception_date, birth_date, statics, "12-MONTH AVG(1 year pre - due date)"))

    return render(request, 'subject_statics.html', {'statics': statics, 'events': events, 'subject_id': subject_id})
def subject_statics_download(request, subject_id=None):

    csv_data1 = io.StringIO()
    writer1 = csv.writer(csv_data1)
    writer1.writerow(['Subject', 'Year', 'Month', 'Poverty', 'Income(Y)', 'Income(M)', 'Adults', 'Kids', 'INR', 'Poverty', 'Move', 'Event'])

    csv_data2 = io.StringIO()
    writer2 = csv.writer(csv_data2)
    writer2.writerow(['Subject', 'EVENT', 'INR', 'Income', 'Duration_Poverty', 'Move', '(M) Work Changed', '(F) Work Changed'])

    birth_date = get_birth_date(subject_id)
    conception_date = get_conception_date(subject_id)

    if birth_date is None and conception_date is not None:
        birth_date = add_months_to_date(conception_date, 9)
    if birth_date is not None and conception_date is None:
        conception_date = add_months_to_date(birth_date, -9)

    tri1_date = get_tri1_date(subject_id)
    tri2_date = get_tri2_date(subject_id)
    tri3_date = get_tri3_date(subject_id)

    if tri1_date is None:
        tri1_date = conception_date
    if tri2_date is None:
        tri2_date = add_months_to_date(tri1_date, 3)
    if tri3_date is None:
        tri3_date = add_months_to_date(tri2_date, 3)

    pv1_interview_date = get_interview_type_date(subject_id, 'pv1')
    pv2_interview_date = get_interview_type_date(subject_id, 'pv2')
    pv3_interview_date = get_interview_type_date(subject_id, 'pv3')
    pn1_interview_date = get_interview_type_date(subject_id, 'pn1')
    pn4_interview_date = get_interview_type_date(subject_id, 'pn4')

    scan_date = get_scan_date(subject_id)
    move_date = get_move_date(subject_id=subject_id)

    interviews = Interview.objects.filter(subject_id=subject_id)

    statics = []
    pre_conception_date = None

    for interview in interviews:
        # Start/End date setting.
        if interview.interview_type == 'pv1':
            work_start = add_months_to_date(birth_date, -12).date()
            pre_conception_date = work_start
            work_end = pv1_interview_date
        elif interview.interview_type == 'pv2':
            work_start = pv1_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pv2_interview_date
        elif interview.interview_type == 'pv3':
            work_start = pv2_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pv3_interview_date
        elif interview.interview_type == 'pn1':
            work_start = pv3_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pn1_interview_date
        elif interview.interview_type == 'pn4':
            work_start = pn1_interview_date
            work_start = work_start.replace(day=1)
            work_start = add_months_to_date(work_start, 1).date()
            work_end = pn4_interview_date

        current_date = work_start
        while current_date <= work_end:
            event = ""
            moc_work_end = 0
            foc_work_end = 0
            moc_work_start = 0
            foc_work_start = 0
            year = current_date.year
            month = current_date.month
            moc_income = calculate_monthly_income(subject_id, year, month)['moc_income']
            foc_income = calculate_monthly_income(subject_id, year, month)['foc_income']
            monthly_income = moc_income + foc_income
            moc_work_end = calculate_monthly_income(subject_id, year, month)['moc_work_end']
            foc_work_end = calculate_monthly_income(subject_id, year, month)['foc_work_end']
            moc_work_start = calculate_monthly_income(subject_id, year, month)['moc_work_start']
            foc_work_start = calculate_monthly_income(subject_id, year, month)['foc_work_start']

            yearly_income = monthly_income * 12

            f_adult = interview.financial_familiy_adult
            h_adult = interview.household_adult
            if f_adult is None:
                f_adult = 0
            if h_adult is None:
                h_adult = 0
            adult = max(f_adult, h_adult)

            f_kid = interview.financial_familiy_child
            h_kid = interview.household_child
            if f_kid is None:
                f_kid = 0
            if h_kid is None:
                h_kid = 0
            kid = max(f_kid, h_kid)

            pline = Poverty.objects.get(year=year, familysize=adult+kid, adult=adult, kid=kid).pline
            inr = yearly_income / pline

            poverty_yn = 0
            if inr < 2:
                poverty_yn = 1

            # event check
            if birth_date is not None:
                if year == birth_date.year and month == birth_date.month:
                    event += "(Birth) (Tri3_end) "
            if conception_date is not None:
                if year == conception_date.year and month == conception_date.month:
                    event += "(Conception) "
            if tri1_date is not None:
                if year == tri1_date.year and month == tri1_date.month:
                    event += "(Tri1 Start) "
            if tri2_date is not None:
                if year == tri2_date.year and month == tri2_date.month:
                    event += "(Tri1 End) (Tri2 Start) "
            if tri3_date is not None:
                if year == tri3_date.year and month == tri3_date.month:
                    event += "(Tri2 End) (Tri3 Start) "
            if scan_date is not None:
                if year == scan_date.year and month == scan_date.month:
                    event += "(Scan) "
            if pv1_interview_date is not None:
                if year == pv1_interview_date.year and month == pv1_interview_date.month:
                    event += "(PV1) "
            if pv2_interview_date is not None:
                if year == pv2_interview_date.year and month == pv2_interview_date.month:
                    event += "(PV2) "
            if pv3_interview_date is not None:
                if year == pv3_interview_date.year and month == pv3_interview_date.month:
                    event += "(PV3) "
            if pn1_interview_date is not None:
                if year == pn1_interview_date.year and month == pn1_interview_date.month:
                    event += "(PN1) "
            if pn4_interview_date is not None:
                if year == pn4_interview_date.year and month == pn4_interview_date.month:
                    event += "(PN4) "
            move_yn = 0
            if move_date is not None:
                if year == move_date.year and month == move_date.month:
                    event += "(Move) "
                    move_yn = 1

            writer1.writerow([subject_id, year, month, pline, yearly_income, monthly_income, adult, kid, inr, poverty_yn, move_yn, event])

            statics.append({'subject_id': subject_id, 'year': year, 'month': month, 'pline': pline, 'yearly_income': yearly_income, 'monthly_income': monthly_income, 'adult': adult, 'kid': kid, 'inr': inr, 'poverty_yn': poverty_yn, 'move_yn': move_yn, 'event': event, 'moc_work_end': moc_work_end, 'foc_work_end': foc_work_end, 'moc_work_start': moc_work_start, 'foc_work_start': foc_work_start})

            # move to next month.
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

    events = []
    events.append(calculate_events(pre_conception_date, conception_date, statics, "PRE_CONCEPTION-CONCEPTION"))
    events.append(calculate_events(conception_date, pv1_interview_date, statics, "CONCEPTION-PV1"))
    events.append(calculate_events(pv1_interview_date, pv2_interview_date, statics, "PV1-PV2"))
    events.append(calculate_events(pv2_interview_date, pv3_interview_date, statics, "PV2-PV3"))
    events.append(calculate_events(pv3_interview_date, pn1_interview_date, statics, "PV3-PN1"))
    events.append(calculate_events(pn1_interview_date, pn4_interview_date, statics, "PN1-PN4"))
    events.append(calculate_events(conception_date, tri2_date, statics, "1st TRIMESTER(Conception-Tri1End)"))
    events.append(calculate_events(tri2_date, tri3_date, statics, "2nd TRIMESTER(Tri2Start-Tri2End)"))
    events.append(calculate_events(tri3_date, birth_date, statics, "3rd TRIMESTER(Tri3Start-Tri3End)"))
    events.append(calculate_events(birth_date, scan_date, statics, "SCAN Postnatal(Birth-Scan)"))
    events.append(calculate_events(birth_date, pn1_interview_date, statics, "PN1 Postnatal(Birth-PN1)"))
    events.append(calculate_events(pn1_interview_date, pn4_interview_date, statics, "PN4 Postnatal(PN1-PN4)"))
    events.append(calculate_events(conception_date, birth_date, statics, "AVG PRENATAL(Conception-Birth)"))
    events.append(calculate_events(birth_date, pn4_interview_date, statics, "AVG POSTNATAL(Birth-PN4)"))
    events.append(calculate_events(pre_conception_date, birth_date, statics, "12-MONTH AVG(1 year pre - due date)"))

    for event in events:
        print(event)
        writer2.writerow([subject_id, event['tag'], event['inr'], event['income'], event['duration_poverty'], event['tot_move_cnt'], event['moc_work_end_cnt'], event['foc_work_end_cnt'] ])#, month, pline, yearly_income, monthly_income, adult, kid, inr, poverty_yn, move_yn,event])


    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        zipf.writestr(f'rise_project_statics_{subject_id}.csv', csv_data1.getvalue())
        zipf.writestr(f'rise_project_events_{subject_id}.csv', csv_data2.getvalue())

    # ZIP 파일을 HttpResponse에 담아서 반환
    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="rise_project_statics_and_events_{subject_id}.zip"'

    return response

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

## Functions
def get_conception_date(subject_id):
    conception_date=None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.conception_date is not None:
            conception_date = interview.conception_date

    return conception_date
def get_birth_date(subject_id):
    birth_date=None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.birth_date is not None:
            birth_date = interview.birth_date

    return birth_date
def get_scan_date(subject_id):
    scan_date=None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.scan_date is not None:
            scan_date = interview.scan_date

    return scan_date
def get_interview_type_date(subject_id, interview_type):
    interview_date = None
    try:
        interview = Interview.objects.get(subject_id=subject_id, interview_type=interview_type)
        interview_date = interview.interview_date
    except ObjectDoesNotExist:
        pass

    return interview_date
def get_tri1_date(subject_id):
    tri1_date = None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.tri1_date is not None:
            tri1_date = interview.tri1_date

    if tri1_date is None:
        conception_date = get_conception_date(subject_id)
        if conception_date is None:
            tri1_date = None
        else:
            days_to_add = 91*0
            tri1_date = conception_date + timedelta(days=days_to_add)

    return tri1_date
def get_tri2_date(subject_id):
    tri2_date = None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.tri2_date is not None:
            tri2_date = interview.tri2_date

    if tri2_date is None:
        conception_date = get_conception_date(subject_id)
        if conception_date is None:
            tri2_date = None
        else:
            days_to_add = 91*1
            tri2_date = conception_date + timedelta(days=days_to_add)

    return tri2_date
def get_tri3_date(subject_id):
    tri3_date = None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.tri3_date is not None:
            tri3_date = interview.tri3_date

    if tri3_date is None:
        conception_date = get_conception_date(subject_id)
        birth_date = get_birth_date(subject_id)
        if conception_date is None and birth_date is None:
            tri3_date = None
        else:
            if birth_date is not None:
                tri3_date = birth_date
            elif conception_date is not None:
                days_to_add = 91*2
                tri3_date = conception_date + timedelta(days=days_to_add)
    return tri3_date
def get_move_date(subject_id):
    move_date = None
    interviews = Interview.objects.filter(subject_id=subject_id)

    for interview in interviews:
        if interview.move_date is not None:
            move_date = interview.move_date

    return move_date
def calculate_monthly_income(subject_id, year=None, month=None):

    moc_income = 0
    foc_income = 0
    etc_income = 0
    gov_income = 0
    tot_income = 0
    moc_work_end = 0
    foc_work_end = 0
    moc_work_start = 0
    foc_work_start = 0

    interviews = Interview.objects.filter(subject_id=subject_id)
    for interview in interviews:
        for i in range(1, 11):
            income = 0

            field_type = f'object_type_{i}'
            field_start = f'object_start_date_{i}'
            field_end = f'object_end_date_{i}'
            field_hour = f'object_working_hour_{i}'
            field_wage = f'object_hourly_wage_{i}'
            field_monthly = f'object_monthly_income_{i}'

            if hasattr(interview, field_type) and getattr(interview, field_type) is not None\
                    and hasattr(interview, field_start) and getattr(interview, field_start) is not None\
                    and hasattr(interview, field_end) and getattr(interview, field_end) is not None\
                    and year is not None\
                    and month is not None:

                income_start = getattr(interview, field_start)
                income_end = getattr(interview, field_end)

                base_start_day = date(year, month, 1)
                total_days = calendar.monthrange(year, month)[1]

                if total_days is None:
                    total_days = 30
                base_end_day = date(year, month, total_days)

                if is_date_in_range(income_start, income_end, year, month):
                    max_start_date = max(base_start_day, income_start)
                    min_end_date = min(base_end_day, income_end)

                    worked_day = (min_end_date - max_start_date).days + 1
                    if worked_day < 0:
                        worked_day = 0

                    # 이제 실제 일한 날짜를 계산해야 해
                    # 기준 월을 받아서 헤당 월의 시작일과 종료일 그리고 총 일수 계산
                    # 여기에서 워킹 시작일과 종료일 계산해서 실제 일한 일수 계산
                    # 총 일수 대비 계산일 수로 monthly_income 계산

                    if hasattr(interview, field_monthly) and getattr(interview, field_monthly) is not None:
                        income_monthly = getattr(interview, field_monthly, 0)
                        if income_monthly is not None and total_days > 0:
                            income = (income_monthly / total_days) * worked_day
                    else:
                        income_hour = getattr(interview, field_hour, 0)
                        income_wage = getattr(interview, field_wage, 0)
                        income = ((income_hour * income_wage) / 7) * worked_day

                    # 날짜 별에 따른 주급/월급 계산하기

                    if getattr(interview, field_type) == 'moc':
                        moc_income += income
                        if year == income_end.year and month == income_end.month:
                            moc_work_end += 1
                        if year == income_start.year and month == income_start.month:
                            moc_work_start += 1
                    elif getattr(interview, field_type) == 'foc':
                        foc_income += income
                        if year == income_end.year and month == income_end.month:
                            foc_work_end += 1
                        if year == income_start.year and month == income_start.month:
                            foc_work_start += 1
                    elif getattr(interview, field_type) == 'etc':
                        etc_income += income
                    elif getattr(interview, field_type) == 'gov':
                        gov_income += income

    tot_income = moc_income + foc_income + etc_income + gov_income

    return {'moc_income': moc_income, 'foc_income': foc_income, 'etc_income': etc_income, 'gov_income': gov_income, 'tot_income': tot_income, 'moc_work_end': moc_work_end, 'foc_work_end': foc_work_end, 'moc_work_start': moc_work_start, 'foc_work_start': foc_work_start}
def is_date_in_range(start_date, end_date, year, month):
    input_date = date(year, month, 1)
    start_date_obj = date(start_date.year, start_date.month, 1)
    end_date_obj = date(end_date.year, end_date.month, end_date.day)

    return start_date_obj <= input_date <= end_date_obj
def add_months_to_date(date, months):
    new_date = None
    if date is not None:
        year = date.year + (date.month + months - 1) // 12
        month = (date.month + months - 1) % 12 + 1
        day = date.day
        new_date = datetime(year, month, day)
    return new_date
def calculate_events(work_start, work_end, statics, tag):

    tot_inr = 0
    tot_move_cnt = 0
    duration_poverty = 0
    moc_work_end_cnt = 0
    foc_work_end_cnt = 0
    tot_income = 0
    avg_inr = 0
    avg_income = 0

    if work_start is None or work_end is None :
        return {'tag': tag, 'inr': avg_inr, 'income': avg_income, 'duration_poverty': duration_poverty,
                'tot_move_cnt': tot_move_cnt, 'moc_work_end_cnt': moc_work_end_cnt,
                'foc_work_end_cnt': foc_work_end_cnt}

    if work_start.day <= 15:
        current_date = work_start.replace(day=15)
    else:
        if work_start.month == 12:
            current_date = work_start.replace(year=work_start.year + 1, month=1, day=15)
        else:
            current_date = work_start.replace(month=work_start.month + 1, day=15)

    if work_end.day < 15:
        if work_end.month == 1:
            work_end = work_end.replace(year=work_end.year - 1, month=12, day=15)
        else:
            work_end = work_end.replace(month=work_end.month - 1, day=15)

    cal_month_cnt = 0
    diff_month_cnt = (work_end.year - current_date.year)*12 + (work_end.month - current_date.month) + 1

    while current_date <= work_end:
        for data in statics:
            if data['year'] == current_date.year and data['month'] == current_date.month:
                moc_work_end_cnt += data['moc_work_end']
                moc_work_end_cnt += data['moc_work_start']
                foc_work_end_cnt += data['foc_work_end']
                foc_work_end_cnt += data['foc_work_start']
                duration_poverty += data['poverty_yn']
                tot_inr += data['inr']
                tot_move_cnt += data['move_yn']
                tot_income += data['yearly_income']
                cal_month_cnt += 1
        # move to next month.
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)

    if cal_month_cnt == diff_month_cnt:
        if cal_month_cnt > 0:
            avg_inr = tot_inr / cal_month_cnt
            avg_income = tot_income / cal_month_cnt
    else:
        tot_move_cnt = 0
        duration_poverty = 0
        moc_work_end_cnt = 0
        foc_work_end_cnt = 0
        avg_inr = 0
        avg_income = 0

    return {'tag': tag, 'inr': avg_inr, 'income': avg_income, 'duration_poverty': duration_poverty, 'tot_move_cnt': tot_move_cnt, 'moc_work_end_cnt': moc_work_end_cnt, 'foc_work_end_cnt': foc_work_end_cnt}