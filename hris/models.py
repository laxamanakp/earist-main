from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.



class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,unique=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="Default_pfp.jpg", null=True, blank=True)
    employee_id = models.CharField(max_length=20,unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    employment_status = models.CharField(max_length=100, null=True, blank=True)
    name_ext = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    gsis_no = models.CharField(max_length=20, blank=True, null=True)
    pagibig_no = models.CharField(max_length=20, blank=True, null=True)
    philhealth_no = models.CharField(max_length=20, blank=True, null=True)
    sss_no = models.CharField(max_length=20, blank=True, null=True)
    tin_no = models.CharField(max_length=20, blank=True, null=True)
    agency_em = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    residential_house_no = models.CharField(max_length=10, blank=True, null=True)
    residential_street = models.CharField(max_length=100, blank=True, null=True)
    residential_subd = models.CharField(max_length=100, blank=True, null=True)
    residential_brgy = models.CharField(max_length=100, blank=True, null=True)
    residential_city = models.CharField(max_length=100, blank=True, null=True)
    residential_province = models.CharField(max_length=100, blank=True, null=True)
    residential_zipcode = models.CharField(max_length=10, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=10, blank=True, null=True)
    permanent_street = models.CharField(max_length=100, blank=True, null=True)
    permanent_subd = models.CharField(max_length=100, blank=True, null=True)
    permanent_brgy = models.CharField(max_length=100, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_province = models.CharField(max_length=100, blank=True, null=True)
    permanent_zipcode = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name_ext = models.CharField(max_length=10, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_employer = models.CharField(max_length=100, blank=True, null=True)
    spouse_business_address = models.CharField(max_length=200, blank=True, null=True)
    spouse_telephone = models.CharField(max_length=20, blank=True, null=True)
    elementary_education = models.CharField(max_length=200, blank=True, null=True)
    secondary_education = models.CharField(max_length=200, blank=True, null=True)
    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)
    father_name_ext = models.CharField(max_length=10, blank=True, null=True)
    mother_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    organization_name_1 = models.CharField(max_length=150, blank=True, null=True)     #For PDS3 VI row 1
    organization_address_1 = models.CharField(max_length=100, blank=True, null=True)
    from_date_1 = models.DateField(blank=True, null=True)
    to_date_1 = models.DateField(blank=True, null=True)
    number_of_hours_1 = models.PositiveIntegerField(default=0)
    position_nature_of_work_1 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_2 = models.CharField(max_length=150, blank=True, null=True )    #For PDS3 VI row 2
    organization_address_2 = models.CharField(max_length=100, blank=True, null=True)
    from_date_2 = models.DateField(blank=True, null=True)
    to_date_2 = models.DateField(blank=True, null=True)
    number_of_hours_2 = models.PositiveIntegerField(default=0)
    position_nature_of_work_2 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_3 = models.CharField(max_length=150, blank=True, null=True )    #For PDS3 VI row 3
    organization_address_3 = models.CharField(max_length=100, blank=True, null=True)
    from_date_3 = models.DateField(blank=True, null=True)
    to_date_3 = models.DateField(blank=True, null=True)
    number_of_hours_3 = models.PositiveIntegerField(default=0)
    position_nature_of_work_3 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_4 = models.CharField(max_length=150, blank=True, null=True )    #For PDS3 VI row 4
    organization_address_4 = models.CharField(max_length=100, blank=True, null=True)
    from_date_4 = models.DateField(blank=True, null=True)
    to_date_4 = models.DateField(blank=True, null=True)
    number_of_hours_4 = models.PositiveIntegerField(default=0)
    position_nature_of_work_4 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_5 = models.CharField(max_length=150, blank=True, null=True )    #For PDS3 VI row 5
    organization_address_5 = models.CharField(max_length=100, blank=True, null=True)
    from_date_5 = models.DateField(blank=True, null=True)
    to_date_5 = models.DateField(blank=True, null=True)
    number_of_hours_5 = models.PositiveIntegerField(default=0)
    position_nature_of_work_5 = models.CharField(max_length=150, blank=True, null=True)
    organization_name_6 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VI row 6
    organization_address_6 = models.CharField(max_length=100, blank=True, null=True)
    from_date_6 = models.DateField(blank=True, null=True)
    to_date_6 = models.DateField(blank=True, null=True)
    number_of_hours_6 = models.PositiveIntegerField(default=0)
    position_nature_of_work_6 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VI row 7
    organization_name_7 = models.CharField(max_length=150, blank=True, null=True)
    organization_address_7 = models.CharField(max_length=100, blank=True, null=True)
    from_date_7 = models.DateField(blank=True, null=True)
    to_date_7 = models.DateField(blank=True, null=True)
    number_of_hours_7 = models.PositiveIntegerField(default=0)
    position_nature_of_work_7 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_1 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 1
    from_date_A1 = models.DateField(blank=True, null=True)
    to_date_A1 = models.DateField(blank=True, null=True)
    number_of_hours_A1 = models.PositiveIntegerField(default=0)
    type_of_ld_1 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_1 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_2 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 2
    from_date_A2 = models.DateField(blank=True, null=True)
    to_date_A2 = models.DateField(blank=True, null=True)
    number_of_hours_A2 = models.PositiveIntegerField(default=0)
    type_of_ld_2 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_2 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_3 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 3
    from_date_A3 = models.DateField(blank=True, null=True)
    to_date_A3 = models.DateField(blank=True, null=True)
    number_of_hours_A3 = models.PositiveIntegerField(default=0)
    type_of_ld_3 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_3 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_4 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 4
    from_date_A4 = models.DateField(blank=True, null=True)
    to_date_A4 = models.DateField(blank=True, null=True)
    number_of_hours_A4 = models.PositiveIntegerField(default=0)
    type_of_ld_4 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_4 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_5 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 5
    from_date_A5 = models.DateField(blank=True, null=True)
    to_date_A5 = models.DateField(blank=True, null=True)
    number_of_hours_A5 = models.PositiveIntegerField(default=0)
    type_of_ld_5 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_5 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_6 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 6
    from_date_A6 = models.DateField(blank=True, null=True)
    to_date_A6 = models.DateField(blank=True, null=True)
    number_of_hours_A6 = models.PositiveIntegerField(default=0)
    type_of_ld_6 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_6 = models.CharField(max_length=150, blank=True, null=True)
    title_of_program_7 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VII row 7
    from_date_A7 = models.DateField(blank=True, null=True)
    to_date_A7 = models.DateField(blank=True, null=True)
    number_of_hours_A7 = models.PositiveIntegerField(default=0)
    type_of_ld_7 = models.CharField(max_length=150, blank=True, null=True)
    conducted_by_7 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_1 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 1
    special_skills_1 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_1 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_2 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 2
    special_skills_2 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_2 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_3 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 3
    special_skills_3 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_3 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_4 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 4
    special_skills_4 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_4 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_5 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 5
    special_skills_5 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_5 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_6 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 6
    special_skills_6 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_6 = models.CharField(max_length=150, blank=True, null=True)
    non_academic_distinctions_7 = models.CharField(max_length=150, blank=True, null=True)    #For PDS3 VIII row 7
    special_skills_7 = models.CharField(max_length=150, blank=True, null=True)
    membership_association_7 = models.CharField(max_length=150, blank=True, null=True)
    
    ref_name_1 = models.CharField(max_length=100, blank=True, null=True)                            #For PDS4 REFERENCES
    ref_adress1 = models.CharField(max_length=100, blank=True, null=True)
    fer_num_1 = models.CharField(max_length=20, blank=True, null=True)
    ref_name_2 = models.CharField(max_length=100, blank=True, null=True)
    ref_adress_2 = models.CharField(max_length=100, blank=True, null=True)
    fer_num_2 = models.CharField(max_length=20, blank=True, null=True)
    ref_name_3 = models.CharField(max_length=100, blank=True, null=True)
    ref_adress_3 = models.CharField(max_length=100, blank=True, null=True)
    fer_num_3 = models.CharField(max_length=20, blank=True, null=True)
    gov_s_id = models.CharField(max_length=50, blank=True, null=True)
    ids_num = models.CharField(max_length=20, blank=True, null=True)
    date_place_i = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.surname}"


class OfficialTime(models.Model):
    employee_id = models.CharField(max_length=20)
    day = models.CharField(max_length = 10)
    semester_id = models.CharField(max_length = 10, null= True, blank = True)
    official_office_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_office_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_out = models.TimeField(default='00:00:00', null=True, blank=True)


class AttendanceRecord(models.Model):
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_out = models.TimeField(default='00:00:00', null=True, blank=True)
    time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_out = models.TimeField(default='00:00:00', null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.date}" if self.date else self.employee_id


class EditLogs(models.Model):
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)