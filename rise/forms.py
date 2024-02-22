from django import forms
from .models import Subject, Interview

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_id', 'researcher', 'pv1', 'pv2', 'pv3', 'pn1', 'pn4']
    def clean_researcher_field(self):
        researcher_field_value = self.data.get('researcher')
        if len(researcher_field_value) <= 20 and researcher_field_value is not None:
            return True
        else:
            return False

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV File')

class InterviewForm(forms.ModelForm):
    financial_family_adult = forms.IntegerField(required=True)
    financial_family_child = forms.IntegerField(required=True)
    household_adult = forms.IntegerField(required=True)
    household_child = forms.IntegerField(required=True)

    financial_family_changes_date_1 = forms.DateField(required=False)
    financial_family_changes_adult_1 = forms.IntegerField(required=False)
    financial_family_changes_child_1 = forms.IntegerField(required=False)
    financial_family_changes_date_2 = forms.DateField(required=False)
    financial_family_changes_adult_2 = forms.IntegerField(required=False)
    financial_family_changes_child_2 = forms.IntegerField(required=False)
    financial_family_changes_date_3 = forms.DateField(required=False)
    financial_family_changes_adult_3 = forms.IntegerField(required=False)
    financial_family_changes_child_3 = forms.IntegerField(required=False)
    financial_family_changes_date_4 = forms.DateField(required=False)
    financial_family_changes_adult_4 = forms.IntegerField(required=False)
    financial_family_changes_child_4 = forms.IntegerField(required=False)
    financial_family_changes_date_5 = forms.DateField(required=False)
    financial_family_changes_adult_5 = forms.IntegerField(required=False)
    financial_family_changes_child_5 = forms.IntegerField(required=False)

    household_member_changes_date_1 = forms.DateField(required=False)
    household_member_changes_comments_1 = forms.CharField(widget=forms.Textarea, required=False)
    household_member_changes_date_2 = forms.DateField(required=False)
    household_member_changes_comments_2 = forms.CharField(widget=forms.Textarea, required=False)
    household_member_changes_date_3 = forms.DateField(required=False)
    household_member_changes_comments_3 = forms.CharField(widget=forms.Textarea, required=False)
    household_member_changes_date_4 = forms.DateField(required=False)
    household_member_changes_comments_4 = forms.CharField(widget=forms.Textarea, required=False)
    household_member_changes_date_5 = forms.DateField(required=False)
    household_member_changes_comments_5 = forms.CharField(widget=forms.Textarea, required=False)

    move_date_1 = forms.DateField(required=False)
    housing_comments_1 = forms.CharField(widget=forms.Textarea, required=False)
    move_date_2 = forms.DateField(required=False)
    housing_comments_2 = forms.CharField(widget=forms.Textarea, required=False)
    move_date_3 = forms.DateField(required=False)
    housing_comments_3 = forms.CharField(widget=forms.Textarea, required=False)
    move_date_4 = forms.DateField(required=False)
    housing_comments_4 = forms.CharField(widget=forms.Textarea, required=False)
    move_date_5 = forms.DateField(required=False)
    housing_comments_5 = forms.CharField(widget=forms.Textarea, required=False)

    conception_date = forms.DateField(required=False)

    tri1_date = forms.DateField(required=False)
    tri2_date = forms.DateField(required=False)
    tri3_date = forms.DateField(required=False)
    birth_date = forms.DateField(required=False)
    scan_date = forms.DateField(required=False)
    event_comments = forms.CharField(widget=forms.Textarea, required=False)

    pn1_q1 = forms.IntegerField(required=False)
    pn1_q2 = forms.IntegerField(required=False)
    pn1_q3 = forms.IntegerField(required=False)
    pn1_q4 = forms.IntegerField(required=False)
    pn1_q5 = forms.CharField(widget=forms.Textarea, required=False)
    pn1_q6 = forms.CharField(widget=forms.Textarea, required=False)

    # Define object type fields (up to 10 objects)
    object_type_1 = forms.CharField(max_length=20, required=False)
    object_working_hour_1 = forms.IntegerField(required=False)
    object_hourly_wage_1 = forms.FloatField(required=False)
    object_monthly_income_1 = forms.FloatField(required=False)
    object_start_date_1 = forms.DateField(required=False)
    object_end_date_1 = forms.DateField(required=False)
    object_comment_1 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_2 = forms.CharField(max_length=20, required=False)
    object_working_hour_2 = forms.IntegerField(required=False)
    object_hourly_wage_2 = forms.FloatField(required=False)
    object_monthly_income_2 = forms.FloatField(required=False)
    object_start_date_2 = forms.DateField(required=False)
    object_end_date_2 = forms.DateField(required=False)
    object_comment_2 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_3 = forms.CharField(max_length=20, required=False)
    object_working_hour_3 = forms.IntegerField(required=False)
    object_hourly_wage_3 = forms.FloatField(required=False)
    object_monthly_income_3 = forms.FloatField(required=False)
    object_start_date_3 = forms.DateField(required=False)
    object_end_date_3 = forms.DateField(required=False)
    object_comment_3 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_4 = forms.CharField(max_length=20, required=False)
    object_working_hour_4 = forms.IntegerField(required=False)
    object_hourly_wage_4 = forms.FloatField(required=False)
    object_monthly_income_4 = forms.FloatField(required=False)
    object_start_date_4 = forms.DateField(required=False)
    object_end_date_4 = forms.DateField(required=False)
    object_comment_4 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_5 = forms.CharField(max_length=20, required=False)
    object_working_hour_5 = forms.IntegerField(required=False)
    object_hourly_wage_5 = forms.FloatField(required=False)
    object_monthly_income_5 = forms.FloatField(required=False)
    object_start_date_5 = forms.DateField(required=False)
    object_end_date_5 = forms.DateField(required=False)
    object_comment_5 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_6 = forms.CharField(max_length=20, required=False)
    object_working_hour_6 = forms.IntegerField(required=False)
    object_hourly_wage_6 = forms.FloatField(required=False)
    object_monthly_income_6 = forms.FloatField(required=False)
    object_start_date_6 = forms.DateField(required=False)
    object_end_date_6 = forms.DateField(required=False)
    object_comment_6 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_7 = forms.CharField(max_length=20, required=False)
    object_working_hour_7 = forms.IntegerField(required=False)
    object_hourly_wage_7 = forms.FloatField(required=False)
    object_monthly_income_7 = forms.FloatField(required=False)
    object_start_date_7 = forms.DateField(required=False)
    object_end_date_7 = forms.DateField(required=False)
    object_comment_7 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_8 = forms.CharField(max_length=20, required=False)
    object_working_hour_8 = forms.IntegerField(required=False)
    object_hourly_wage_8 = forms.FloatField(required=False)
    object_monthly_income_8 = forms.FloatField(required=False)
    object_start_date_8 = forms.DateField(required=False)
    object_end_date_8 = forms.DateField(required=False)
    object_comment_8 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_9 = forms.CharField(max_length=20, required=False)
    object_working_hour_9 = forms.IntegerField(required=False)
    object_hourly_wage_9 = forms.FloatField(required=False)
    object_monthly_income_9 = forms.FloatField(required=False)
    object_start_date_9 = forms.DateField(required=False)
    object_end_date_9 = forms.DateField(required=False)
    object_comment_9 = forms.CharField(widget=forms.Textarea, required=False)

    object_type_10 = forms.CharField(max_length=20, required=False)
    object_working_hour_10 = forms.IntegerField(required=False)
    object_hourly_wage_10 = forms.FloatField(required=False)
    object_monthly_income_10 = forms.FloatField(required=False)
    object_start_date_10 = forms.DateField(required=False)
    object_end_date_10 = forms.DateField(required=False)
    object_comment_10 = forms.CharField(widget=forms.Textarea, required=False)


    class Meta:
        model = Interview
        fields = [ 'interview_id', 'subject_id', 'researcher', 'interview_type', 'interview_date', 'partner_support_status',
                   'household_adult', 'household_child', 'financial_family_adult', 'financial_family_child',
                   'financial_family_changes_date_1', 'financial_family_changes_adult_1', 'financial_family_changes_child_1',
                   'financial_family_changes_date_2', 'financial_family_changes_adult_2', 'financial_family_changes_child_2',
                   'financial_family_changes_date_3', 'financial_family_changes_adult_3', 'financial_family_changes_child_3',
                   'financial_family_changes_date_4', 'financial_family_changes_adult_4', 'financial_family_changes_child_4',
                   'financial_family_changes_date_5', 'financial_family_changes_adult_5', 'financial_family_changes_child_5',
                   'household_member_changes_date_1', 'household_member_changes_comments_1',
                   'household_member_changes_date_2', 'household_member_changes_comments_2',
                   'household_member_changes_date_3', 'household_member_changes_comments_3',
                   'household_member_changes_date_4', 'household_member_changes_comments_4',
                   'household_member_changes_date_5', 'household_member_changes_comments_5',
                   'move_date_1', 'housing_comments_1',
                   'move_date_2', 'housing_comments_2',
                   'move_date_3', 'housing_comments_3',
                   'move_date_4', 'housing_comments_4',
                   'move_date_5', 'housing_comments_5',
                   'conception_date', 'tri1_date', 'tri2_date', 'tri3_date', 'birth_date', 'scan_date', 'event_comments',
                   'pn1_q1', 'pn1_q2', 'pn1_q3', 'pn1_q4', 'pn1_q5', 'pn1_q6',
                   'object_type_1', 'object_working_hour_1', 'object_hourly_wage_1', 'object_monthly_income_1', 'object_start_date_1', 'object_end_date_1', 'object_comment_1',
                   'object_type_2', 'object_working_hour_2', 'object_hourly_wage_2', 'object_monthly_income_2', 'object_start_date_2', 'object_end_date_2', 'object_comment_2',
                   'object_type_3', 'object_working_hour_3', 'object_hourly_wage_3', 'object_monthly_income_3', 'object_start_date_3', 'object_end_date_3', 'object_comment_3',
                   'object_type_4', 'object_working_hour_4', 'object_hourly_wage_4', 'object_monthly_income_4', 'object_start_date_4', 'object_end_date_4', 'object_comment_4',
                   'object_type_5', 'object_working_hour_5', 'object_hourly_wage_5', 'object_monthly_income_5', 'object_start_date_5', 'object_end_date_5', 'object_comment_5',
                   'object_type_6', 'object_working_hour_6', 'object_hourly_wage_6', 'object_monthly_income_6', 'object_start_date_6', 'object_end_date_6', 'object_comment_6',
                   'object_type_7', 'object_working_hour_7', 'object_hourly_wage_7', 'object_monthly_income_7', 'object_start_date_7', 'object_end_date_7', 'object_comment_7',
                   'object_type_8', 'object_working_hour_8', 'object_hourly_wage_8', 'object_monthly_income_8', 'object_start_date_8', 'object_end_date_8', 'object_comment_8',
                   'object_type_9', 'object_working_hour_9', 'object_hourly_wage_9', 'object_monthly_income_9', 'object_start_date_9', 'object_end_date_9', 'object_comment_9',
                   'object_type_10', 'object_working_hour_10', 'object_hourly_wage_10', 'object_monthly_income_10', 'object_start_date_10', 'object_end_date_10', 'object_comment_10']