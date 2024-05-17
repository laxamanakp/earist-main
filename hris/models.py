from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.



class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, unique=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="Default_pfp.jpg", null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True)  # Employee ID
    surname = models.CharField(max_length=100, null=True, blank=True)  # Surname
    first_name = models.CharField(max_length=100, null=True, blank=True)  # First Name
    middle_name = models.CharField(max_length=100, null=True, blank=True)  # Middle Name
    email = models.EmailField(blank=True, null=True)  # Email Address
    employment_status = models.CharField(max_length=100, null=True, blank=True)  # Employment Status
    name_ext = models.CharField(max_length=10, blank=True, null=True)  # Name Extension
    date_of_birth = models.DateField(blank=True, null=True)  # Date of Birth
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)  # Place of Birth
    sex = models.CharField(max_length=10, blank=True, null=True)  # Sex
    civil_status = models.CharField(max_length=20, blank=True, null=True)  # Civil Status
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Height (m)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Weight (kg)
    blood_type = models.CharField(max_length=10, blank=True, null=True)  # Blood Type
    gsis_no = models.CharField(max_length=20, blank=True, null=True)  # GSIS Number
    pagibig_no = models.CharField(max_length=20, blank=True, null=True)  # Pag-IBIG Number
    philhealth_no = models.CharField(max_length=20, blank=True, null=True)  # PhilHealth Number
    sss_no = models.CharField(max_length=20, blank=True, null=True)  # SSS Number
    tin_no = models.CharField(max_length=20, blank=True, null=True)  # TIN Number
    agency_em = models.CharField(max_length=100, blank=True, null=True)  # Agency Employment
    citizenship = models.CharField(max_length=50, blank=True, null=True)  # Citizenship
    residential_house_no = models.CharField(max_length=10, blank=True, null=True)  # Residential House No.
    residential_street = models.CharField(max_length=100, blank=True, null=True)  # Residential Street
    residential_subd = models.CharField(max_length=100, blank=True, null=True)  # Residential Subdivision
    residential_brgy = models.CharField(max_length=100, blank=True, null=True)  # Residential Barangay
    residential_city = models.CharField(max_length=100, blank=True, null=True)  # Residential City
    residential_province = models.CharField(max_length=100, blank=True, null=True)  # Residential Province
    residential_zipcode = models.CharField(max_length=10, blank=True, null=True)  # Residential Zip Code
    permanent_house_no = models.CharField(max_length=10, blank=True, null=True)  # Permanent House No.
    permanent_street = models.CharField(max_length=100, blank=True, null=True)  # Permanent Street
    permanent_subd = models.CharField(max_length=100, blank=True, null=True)  # Permanent Subdivision
    permanent_brgy = models.CharField(max_length=100, blank=True, null=True)  # Permanent Barangay
    permanent_city = models.CharField(max_length=100, blank=True, null=True)  # Permanent City
    permanent_province = models.CharField(max_length=100, blank=True, null=True)  # Permanent Province
    permanent_zipcode = models.CharField(max_length=10, blank=True, null=True)  # Permanent Zip Code
    telephone = models.CharField(max_length=20, blank=True, null=True)  # Telephone Number
    mobile_number = models.CharField(max_length=20, blank=True, null=True)  # Mobile Number
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)  # Spouse Surname
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)  # Spouse First Name
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)  # Spouse Middle Name
    spouse_name_ext = models.CharField(max_length=10, blank=True, null=True)  # Spouse Name Extension
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)  # Spouse Occupation
    spouse_employer = models.CharField(max_length=100, blank=True, null=True)  # Spouse Employer
    spouse_business_address = models.CharField(max_length=200, blank=True, null=True)  # Spouse Business Address
    spouse_telephone = models.CharField(max_length=20, blank=True, null=True)  # Spouse Telephone Number
    elementary_education = models.CharField(max_length=200, blank=True, null=True)  # Elementary Education
    secondary_education = models.CharField(max_length=200, blank=True, null=True)  # Secondary Education
    vocational_or_trade_course = models.CharField(max_length=200, blank=True, null=True)  # Vocational/Trade Course
    college_education = models.CharField(max_length=200, blank=True, null=True)  # College Education
    graduate_studies = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies
    elementary_basic_education = models.CharField(max_length=200, blank=True, null=True)  # Elementary Education Basic
    secondary_basic_education = models.CharField(max_length=200, blank=True, null=True)  # Secondary Education Basic
    vocational_basic_education = models.CharField(max_length=200, blank=True, null=True)  # Vocational/Trade Course Basic
    college_basic_education = models.CharField(max_length=200, blank=True, null=True)  # College Education Basic
    graduate_studies_basic_education = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies Basic
    elementary_graduate_from = models.CharField(max_length=200, blank=True, null=True)  # Elementary From
    elementary_graduate_to = models.CharField(max_length=200, blank=True, null=True)  # Elementary to
    secondary_graduate_from = models.CharField(max_length=200, blank=True, null=True)  # Secondary From
    secondary_graduate_to = models.CharField(max_length=200, blank=True, null=True)  # Secondary to
    vocational_graduate_from = models.CharField(max_length=200, blank=True, null=True)  # Vocational From
    vocational_graduate_to = models.CharField(max_length=200, blank=True, null=True)  # Vocational to
    college_graduate_from = models.CharField(max_length=200, blank=True, null=True)  # College From
    college_graduate_to = models.CharField(max_length=200, blank=True, null=True)  # College to
    graduate_graduate_from = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies From
    graduate_studies_graduate_to = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies to
    elementary_highest_level_earned = models.CharField(max_length=200, blank=True, null=True)  # Elementary Highest Level
    secondary_highest_level_earned = models.CharField(max_length=200, blank=True, null=True)  # Secondary Highest Level
    vocational_highest_level_earned = models.CharField(max_length=200, blank=True, null=True)  # Vocational Highest Level
    college_highest_level_earned = models.CharField(max_length=200, blank=True, null=True)  # College Highest Level
    graduate_studies_highest_level_earned = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies Highest Level
    elementary_year_graduated = models.CharField(max_length=200, blank=True, null=True)  # Elementary Highest Year Graduated
    secondary_year_graduated = models.CharField(max_length=200, blank=True, null=True)  # Secondary Highest Year Graduated
    vocational_year_graduated = models.CharField(max_length=200, blank=True, null=True)  # Vocational Highest Year Graduated
    college_year_graduated = models.CharField(max_length=200, blank=True, null=True)  # College Highest Year Graduated
    graduate_studies_year_graduated = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies Year Graduated
    elementary_honors = models.CharField(max_length=200, blank=True, null=True)  # Elementary Highest Honors
    secondary_honors = models.CharField(max_length=200, blank=True, null=True)  # Secondary Highest Honors
    vocational_honors = models.CharField(max_length=200, blank=True, null=True)  # Vocational Highest Honors
    college_honors = models.CharField(max_length=200, blank=True, null=True)  # College Highest Honors
    graduate_studies_honors = models.CharField(max_length=200, blank=True, null=True)  # Graduate Studies Honors
    father_surname = models.CharField(max_length=100, blank=True, null=True)  # Father's Surname
    father_first_name = models.CharField(max_length=100, blank=True, null=True)  # Father's First Name
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)  # Father's Middle Name
    father_name_ext = models.CharField(max_length=10, blank=True, null=True)  # Father's Name Extension
    mother_surname = models.CharField(max_length=100, blank=True, null=True)  # Mother's Surname
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)  # Mother's First Name
    mother_middle_name = models.CharField(max_length=100, blank=True, null=True)  # Mother's Middle Name
    child_name = models.CharField(max_length=100, blank=True, null=True)  # Children's Full Name
    child_birth = models.DateField(blank=True, null=True)  # Children's Date of Birth
    child_name_2 = models.CharField(max_length=100, blank=True, null=True)  # 2nd Children's Full Name
    child_birth_2 = models.DateField(blank=True, null=True)  # Children's Date of Birth
    child_name_3 = models.CharField(max_length=100, blank=True, null=True)  # 3rd Children's Full Name
    child_birth_3 = models.DateField(blank=True, null=True)  # Children's Date of Birth
    child_name_4 = models.CharField(max_length=100, blank=True, null=True)  # 4th Children's Full Name
    child_birth_4 = models.DateField(blank=True, null=True)  # Children's Date of Birth
    child_name_5 = models.CharField(max_length=100, blank=True, null=True)  # 5th Children's Full Name
    child_birth_5 = models.DateField(blank=True, null=True)  # Children's Date of Birth
    date_created = models.DateTimeField(auto_now_add=True, null=True)  # Date Created

    #pds2 Civil Service Eligibility
    credentials = models.CharField(max_length=100, blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True, null=True)
    exam_date = models.DateField(null=True, blank=True)
    exam_location = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=20, blank=True, null=True)
    license_date = models.DateField(null=True, blank=True)

    credentials2 = models.CharField(max_length=100, blank=True, null=True)
    rating2 = models.CharField(max_length=5, blank=True, null=True)
    exam_date2 = models.DateField(null=True, blank=True)
    exam_location2 = models.CharField(max_length=100, blank=True, null=True)
    license_number2 = models.CharField(max_length=20, blank=True, null=True)
    license_date2 = models.DateField(null=True, blank=True)

    credentials3 = models.CharField(max_length=100, blank=True, null=True)
    rating3 = models.CharField(max_length=5, blank=True, null=True)
    exam_date3 = models.DateField(null=True, blank=True)
    exam_location3 = models.CharField(max_length=100, blank=True, null=True)
    license_number3 = models.CharField(max_length=20, blank=True, null=True)
    license_date3 = models.DateField(null=True, blank=True)

    credentials4 = models.CharField(max_length=100, blank=True, null=True)
    rating4 = models.CharField(max_length=5, blank=True, null=True)
    exam_date4 = models.DateField(null=True, blank=True)
    exam_location4 = models.CharField(max_length=100, blank=True, null=True)
    license_number4 = models.CharField(max_length=20, blank=True, null=True)
    license_date4 = models.DateField(null=True, blank=True)

    credentials5 = models.CharField(max_length=100, blank=True, null=True)
    rating5 = models.CharField(max_length=5, blank=True, null=True)
    exam_date5 = models.DateField(null=True, blank=True)
    exam_location5 = models.CharField(max_length=100, blank=True, null=True)
    license_number5 = models.CharField(max_length=20, blank=True, null=True)
    license_date5 = models.DateField(null=True, blank=True)

    credentials6 = models.CharField(max_length=100, blank=True, null=True)
    rating6 = models.CharField(max_length=5, blank=True, null=True)
    exam_date6 = models.DateField(null=True, blank=True)
    exam_location6 = models.CharField(max_length=100, blank=True, null=True)
    license_number6 = models.CharField(max_length=20, blank=True, null=True)
    license_date6 = models.DateField(null=True, blank=True)

    credentials7 = models.CharField(max_length=100, blank=True, null=True)
    rating7 = models.CharField(max_length=5, blank=True, null=True)
    exam_date7 = models.DateField(null=True, blank=True)
    exam_location7 = models.CharField(max_length=100, blank=True, null=True)
    license_number7 = models.CharField(max_length=20, blank=True, null=True)
    license_date7 = models.DateField(null=True, blank=True)

    #pds2 Work Experience

    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    workplace_name = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade = models.CharField(max_length=20, blank=True, null=True)
    step = models.CharField(max_length=20, blank=True, null=True)
    status_appointment = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N = models.CharField(max_length=1, blank=True, null=True)

    date_from2 = models.DateField(null=True, blank=True)
    date_to2 = models.DateField(null=True, blank=True)
    position2 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name2 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary2 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade2 = models.CharField(max_length=20, blank=True, null=True)
    step2 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment2 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N2 = models.CharField(max_length=1, blank=True, null=True)

    date_from3 = models.DateField(null=True, blank=True)
    date_to3 = models.DateField(null=True, blank=True)
    position3 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name3 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary3 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade3 = models.CharField(max_length=20, blank=True, null=True)
    step3 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment3 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N3 = models.CharField(max_length=1, blank=True, null=True)

    date_from4 = models.DateField(null=True, blank=True)
    date_to4 = models.DateField(null=True, blank=True)
    position4 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name4 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary4 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade4 = models.CharField(max_length=20, blank=True, null=True)
    step4 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment4 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N4 = models.CharField(max_length=1, blank=True, null=True)

    date_from5 = models.DateField(null=True, blank=True)
    date_to5 = models.DateField(null=True, blank=True)
    position5 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name5 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary5 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade5 = models.CharField(max_length=20, blank=True, null=True)
    step5 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment5 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N5 = models.CharField(max_length=1, blank=True, null=True)

    date_from6 = models.DateField(null=True, blank=True)
    date_to6 = models.DateField(null=True, blank=True)
    position6 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name6 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary6 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade6 = models.CharField(max_length=20, blank=True, null=True)
    step6 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment6 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N6 = models.CharField(max_length=1, blank=True, null=True)

    date_from7 = models.DateField(null=True, blank=True)
    date_to7 = models.DateField(null=True, blank=True)
    position7 = models.CharField(max_length=100, blank=True, null=True)
    workplace_name7 = models.CharField(max_length=100, blank=True, null=True)
    monthly_salary7 = models.CharField(max_length=20, blank=True, null=True)
    salary_paygrade7 = models.CharField(max_length=20, blank=True, null=True)
    step7 = models.CharField(max_length=20, blank=True, null=True)
    status_appointment7 = models.CharField(max_length=100, blank=True, null=True)
    government_service_Y_or_N7 = models.CharField(max_length=1, blank=True, null=True)

    signature = models.ImageField(null=True, blank=True)
    date_filled = models.DateField(null=True, blank=True)


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