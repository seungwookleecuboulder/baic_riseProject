from django.db import models

class Subject(models.Model):
    subject_id = models.CharField(max_length=20, primary_key=True)
    researcher = models.CharField(max_length=20)
    pv1 = models.CharField(max_length=20)
    pv2 = models.CharField(max_length=20)
    pv3 = models.CharField(max_length=20)
    pn1 = models.CharField(max_length=20)
    pn4 = models.CharField(max_length=20)

    class Meta:
        app_label = 'rise'

    def __str__(self):
        return self.subject_id


class Poverty(models.Model):
    year = models.IntegerField()
    familysize = models.IntegerField()
    old = models.IntegerField()
    adult = models.IntegerField()
    kid = models.IntegerField()
    pline = models.FloatField()

    class Meta:
        unique_together = ('year', 'old', 'adult', 'kid')

    def __str__(self):
        return f"Poverty data for year {self.year}"


class Interview(models.Model):

    interview_id = models.CharField(max_length=20, primary_key=True)
    subject_id = models.CharField(max_length=20)
    researcher = models.CharField(max_length=20)
    interview_type = models.CharField(max_length=20)
    interview_date = models.DateField()
    financial_supporter_type = models.CharField(max_length=20)
    household_adult = models.IntegerField(null=True)
    household_child = models.IntegerField(null=True)
    financial_familiy_adult = models.IntegerField(null=True)
    financial_familiy_child = models.IntegerField(null=True)
    housing_comments = models.TextField(null=True)
    move_date = models.DateField(null=True)
    conception_date = models.DateField(null=True)
    tri1_date = models.DateField(null=True)
    tri2_date = models.DateField(null=True)
    tri3_date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    scan_date = models.DateField(null=True)
    event_comments = models.TextField(null=True)

    # Define object type fields (up to 10 objects)
    object_type_1 = models.CharField(max_length=20, null=True)
    object_working_hour_1 = models.IntegerField(null=True)
    object_hourly_wage_1 = models.IntegerField(null=True)
    object_monthly_income_1 = models.IntegerField(null=True)
    object_start_date_1 = models.DateField(null=True)
    object_end_date_1 = models.DateField(null=True)
    object_comment_1 = models.TextField(null=True)

    object_type_2 = models.CharField(max_length=20, null=True)
    object_working_hour_2 = models.IntegerField(null=True)
    object_hourly_wage_2 = models.IntegerField(null=True)
    object_monthly_income_2 = models.IntegerField(null=True)
    object_start_date_2 = models.DateField(null=True)
    object_end_date_2 = models.DateField(null=True)
    object_comment_2 = models.TextField(null=True)

    object_type_3 = models.CharField(max_length=20, null=True)
    object_working_hour_3 = models.IntegerField(null=True)
    object_hourly_wage_3 = models.IntegerField(null=True)
    object_monthly_income_3 = models.IntegerField(null=True)
    object_start_date_3 = models.DateField(null=True)
    object_end_date_3 = models.DateField(null=True)
    object_comment_3 = models.TextField(null=True)

    object_type_4 = models.CharField(max_length=20, null=True)
    object_working_hour_4 = models.IntegerField(null=True)
    object_hourly_wage_4 = models.IntegerField(null=True)
    object_monthly_income_4 = models.IntegerField(null=True)
    object_start_date_4 = models.DateField(null=True)
    object_end_date_4 = models.DateField(null=True)
    object_comment_4 = models.TextField(null=True)

    object_type_5 = models.CharField(max_length=20, null=True)
    object_working_hour_5 = models.IntegerField(null=True)
    object_hourly_wage_5 = models.IntegerField(null=True)
    object_monthly_income_5 = models.IntegerField(null=True)
    object_start_date_5 = models.DateField(null=True)
    object_end_date_5 = models.DateField(null=True)
    object_comment_5 = models.TextField(null=True)

    object_type_6 = models.CharField(max_length=20, null=True)
    object_working_hour_6 = models.IntegerField(null=True)
    object_hourly_wage_6 = models.IntegerField(null=True)
    object_monthly_income_6 = models.IntegerField(null=True)
    object_start_date_6 = models.DateField(null=True)
    object_end_date_6 = models.DateField(null=True)
    object_comment_6 = models.TextField(null=True)

    object_type_7 = models.CharField(max_length=20, null=True)
    object_working_hour_7 = models.IntegerField(null=True)
    object_hourly_wage_7 = models.IntegerField(null=True)
    object_monthly_income_7 = models.IntegerField(null=True)
    object_start_date_7 = models.DateField(null=True)
    object_end_date_7 = models.DateField(null=True)
    object_comment_7 = models.TextField(null=True)

    object_type_8 = models.CharField(max_length=20, null=True)
    object_working_hour_8 = models.IntegerField(null=True)
    object_hourly_wage_8 = models.IntegerField(null=True)
    object_monthly_income_8 = models.IntegerField(null=True)
    object_start_date_8 = models.DateField(null=True)
    object_end_date_8 = models.DateField(null=True)
    object_comment_8 = models.TextField(null=True)

    object_type_9 = models.CharField(max_length=20, null=True)
    object_working_hour_9 = models.IntegerField(null=True)
    object_hourly_wage_9 = models.IntegerField(null=True)
    object_monthly_income_9 = models.IntegerField(null=True)
    object_start_date_9 = models.DateField(null=True)
    object_end_date_9 = models.DateField(null=True)
    object_comment_9 = models.TextField(null=True)

    object_type_10 = models.CharField(max_length=20, null=True)
    object_working_hour_10 = models.IntegerField(null=True)
    object_hourly_wage_10 = models.IntegerField(null=True)
    object_monthly_income_10 = models.IntegerField(null=True)
    object_start_date_10 = models.DateField(null=True)
    object_end_date_10 = models.DateField(null=True)
    object_comment_10 = models.TextField(null=True)

    def __str__(self):
        return f"Interview data for interview {self.interview_id}"
