#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
import math
import numpy as np


# In[2]:


# sample_data = pd.read_pickle('./test_main.pkl')

# sample_data


# In[3]:

def cleaning (sample_data):
    for i in sample_data.columns.values:
        if sample_data[i].dtype == 'object':
            sample_data[i] = sample_data[i].astype('string')
            sample_data[i].mask(sample_data[i].str.lower().str.strip() == 'n.a.', np.nan, inplace = True)


# In[4]:
def type_check (param):
    if pd.isna(param):
        return 2
    else:
        return int(float(param))

# sample_data['Power Supply For Domestic Use Summer (April-Sept.) per day (in Hours)'] = sample_data['Power Supply For Domestic Use Summer (April-Sept.) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For Domestic Use Winter (Oct-March) per day (in Hours)'] = sample_data['Power Supply For Domestic Use Winter (Oct-March) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For Agriculture Use Summer (April-Sept.) per day (in Hours)'] = sample_data['Power Supply For Agriculture Use Summer (April-Sept.) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For Agriculture Use Winter (Oct-March)per day (in Hours)'] = sample_data['Power Supply For Agriculture Use Winter (Oct-March)per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For Commercial Use Summer (April-Sept.) per day (in Hours)'] = sample_data['Power Supply For Commercial Use Summer (April-Sept.) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For Commercial Use Winter (Oct-March) per day (in Hours)'] = sample_data['Power Supply For Commercial Use Winter (Oct-March) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For All Users Summer (April-Sept.) per day (in Hours)'] = sample_data['Power Supply For All Users Summer (April-Sept.) per day (in Hours)'].fillna(0).astype(int)
# sample_data['Power Supply For All Users Winter (Oct-March) per day (in Hours)'] = sample_data['Power Supply For All Users Winter (Oct-March) per day (in Hours)'].fillna(0).astype(int)


# In[5]:


# sample_data['Pincode'] = sample_data['Pincode'].astype(int)
# def decide_pincode (pin1, pin2):
#     if pin1 == pin2 and str(pin1) != 'nan' and str(pin2) != 'nan':
#         return int(pin1)
#     elif str(pin1) == 'nan' and str(pin2) != 'nan':
#         pin2 = float(pin2)
#         return int(pin2)
#     elif str(pin1) != 'nan' and str(pin2) == 'nan':
#         return str(int(pin1)) + "-ii"
#     elif pin1 != pin2 and str(pin1) != 'nan' and str(pin2) != 'nan':
#         pin2 = float(pin2)
#         return int(pin2)
#     else: # both pin1 and pin2 are null
#         return pin1
def decide_pincode (pin):
    if pd.isna(pin):
        return 'nan'
    else:
        return int(float(pin))
# In[41]:


env = Environment(
    loader = FileSystemLoader("./"),
    autoescape = select_autoescape()
)


# In[42]:


village_education_array = ['Nearest Village/Town Name (Pre-Primary School (Nursery/LKG/UKG) Telugu',
                          'Nearest Village/Town Name (Primary School) Telugu',
                          'Nearest Village/Town Name (Middle School) Telugu',
                          'Nearest Village/Town Name (Secondary School) Telugu',
                          'Nearest Village/Town Name (Senior Secondary School) Telugu',
                          'Nearest Village/Town Name (Arts and Science Degree College) Telugu',
                          'Nearest Village/Town Name (Engineering College) Telugu',
                          'Nearest Village/Town Name (Medicine College) Telugu',
                          'Nearest Village/Town Name (Management Institute) Telugu',
                          'Nearest Village/Town Name (Polytechnic) Telugu',
                          'Nearest Village/Town Name (Vocational Training School/ITI) Telugu',
                          'Nearest Village/Town Name (Private Non Formal Training Centre) Telugu',
                          'Nearest Village/Town Name (Private School For Disabled) Telugu']

facility_status_array = ['Nearest Facility Status (Pre-Primary School (Nursery/LKG/UKG) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Primary School) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Middle School) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Secondary School)(Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Senior Secondary School) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Arts and Science Degree College) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Engineering College) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Medicine College) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Management Institute) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Polytechnic) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Vocational Training School/ITI) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Private Non Formal Training Centre) (Govt(1)/Private(2)) ',
                         'Nearest Facility Status (Private School For Disabled) (Govt(1)/Private(2)) ']

distance_education_array = ['(If Pre-Primary School (Nursery/LKG/UKG not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Primary School not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Middle School not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Secondary School not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Senior Secondary School not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Arts and Science Degree College not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Engineering College not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Medicine College not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Management Institute not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Polytechnic not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Vocational Training School/ITI not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Private Non Formal Training Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                           '(If Private School For Disabled not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

translated_education_array = ['పూర్వ ప్రాథమిక పాఠశాలలు',
                              'ప్రాథమిక పాఠశాలలు',
                              'మధ్య పాఠశాలలు',
                              'మాధ్యమిక పాఠశాలలు',
                              'సీనియర్ సెకండరీ పాఠశాలలు',
                              'ఆర్ట్స్ అండ్ సైన్స్ డిగ్రీ కళాశాలలు',
                              'ఇంజనీరింగ్ కళాశాలలు',
                              'వైద్య కళాశాలలు',
                              'మానేజ్మెంట్ ఇన్స్టిట్యూట్లు',
                              'పాలిటెక్నిక్ కళాశాలలు',
                              'వృత్తి శిక్షణ పాఠశాలలు/ఐ.టి.ఐ',
                              'అనియత శిక్షణా కేంద్రాలు',
                              'వికలాంగుల కోసం పాఠశాలలు']


# In[79]:


def get_educational_centres(info_df, i):
    education = {}
    
    for index in range(len(distance_education_array)):
        distance_var = info_df.loc[i, (distance_education_array[index])]
        village_name = info_df.loc[i, (village_education_array[index])]

        if not pd.isna(distance_var) and not pd.isna(village_name):
            distance_var = distance_var.strip().lower()
            village_name = village_name.strip().lower()

            if distance_var not in education:
                education[distance_var] = {}

            current_scope = education[distance_var]

            if village_name not in current_scope:
                current_scope[village_name] = []

            govt_or_private = type_check(info_df.loc[i, (facility_status_array[index])])

            # print(type(govt_or_private))

            if govt_or_private > 1:
                current_scope[village_name].append(f'ప్రైవేట్ {translated_education_array[index]}')
            else:
                current_scope[village_name].append(f'ప్రభుత్వ {translated_education_array[index]}')

    if 'a' in education:
        education['ఊరినుండి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నవి'] = education.pop('a')

    if 'b' in education:
        education['ఊరినుండి 5-10 కి.మీ. సమీపం లో ఉన్నవి'] = education.pop('b')

    if 'c' in education:
        education['ఊరినుండి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నవి'] = education.pop('c')
    
    return education


# In[44]:


distance_health_array = ['(If Community Health Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Primary Health Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Primary Health Sub Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Maternity And Child Welfare Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If TB Clinic not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Hospital Allopathic not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Hospital Alternative Medicine not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Dispensary not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Veterinary Hospital not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Mobile Health Clinic not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Family Welfare Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

health_centres_array = ['Community Health Centre (Numbers)',
                        'Primary Health Centre (Numbers)',
                        'Primary Health Sub Centre (Numbers)',
                        'Maternity And Child Welfare Centre (Numbers)',
                        'TB Clinic (Numbers)',
                        'Hospital Allopathic (Numbers)',
                        'Hospital Alternative Medicine (Numbers)',
                        'Dispensary (Numbers)',
                        'Veterinary Hospital (Numbers)',
                        'Mobile Health Clinic (Numbers)',
                        'Family Welfare Centre (Numbers)']

translated_health_array = ['సామాజిక ఆరోగ్య కేంద్రాలు',
                          'ప్రాథమిక ఆరోగ్య కేంద్రాలు',
                          'ప్రాథమిక ఆరోగ్య ఉప కేంద్రాలు',
                          'ప్రసూతి, శిశు సంక్షేమ కేంద్రాలు',
                          'టిబి క్లినిక్లు',
                          'అల్లోపతి ఆసుపత్రులు',
                          'ఇతర ఆసుపత్రులు',
                          'డిస్పెన్సరీలు',
                          'వెర్టర్నరీ ఆసుపత్రులు',
                          'మొబైల్ హెల్త్ క్లినిక్లు',
                          'కుటుంబ సంక్షేమ కేంద్రాలు']


# In[45]:


def get_medical_centres(info_df, i):
    medical = {}
    
    for index in range(len(distance_health_array)):
        distance_var = info_df.loc[i, (distance_health_array[index])]
        centre_number = info_df.loc[i, (health_centres_array[index])]

        if not pd.isna(distance_var):
            distance_var = distance_var.strip().lower()

            if distance_var not in medical:
                medical[distance_var] = []
            
            medical[distance_var].append(translated_health_array[index])

    if 'a' in medical:
        medical['ఊరినుండి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నవి'] = medical.pop('a')

    if 'b' in medical:
        medical['ఊరినుండి 5-10 కి.మీ. సమీపం లో ఉన్నవి'] = medical.pop('b')

    if 'c' in medical:
        medical['ఊరినుండి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నవి'] = medical.pop('c')
    
    return medical


# In[82]:


def get_drainge_release_method(info_df, i):
    if type_check(info_df.loc[i, ('Whether Drain water is discharged directly into water bodies or to sewar plant (For Water Bodies-1/Sewar Plants-2)')]) > 1:
        return 'నీటి వనరులలోకి'
    return 'సీవార్ ప్లాంట్లోకి'


# In[83]:


def get_driange_scheme(info_df, i):
    drainage_system = False
    return_str = 'ఈ గ్రామానికి'
    
    if type_check(info_df.loc[i, (' Open Drainage (Status A(1)/NA(2))')]) < 2:
        drainage_system = True
        return_str += ' ఓపెన్ డ్రైనేజీ'
    
    if type_check(info_df.loc[i, ('Closed Drainage (Status A(1)/NA(2))')]) < 2:
        if drainage_system:
            return_str += ' మరియు క్లోజ్డ్ డ్రైనేజీ'
        else:
            drainage_system = True
            return_str += ' క్లోజ్డ్ డ్రైనేజీ'
    
    if drainage_system:
        return return_str+' ఉన్నది'
    return ''


# In[84]:


def get_post_office_status(info_df, k):
    if type_check(info_df.loc[k, ('Post Office (Status A(1)/NA(2))')]) > 1:
        return 'తపాలా కార్యాలయము లేదు'
    return 'తపాలా కార్యాలయుము తయారైనది'


# In[85]:


def get_landline_status(info_df, k, dcom):
    if type_check(info_df.loc[k, ('Telephone (landlines) (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Telephone (landlines) not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return
        if distance_var == 'c':
            dcom['t'].append('ల్యాండ్లైన్ టెలిఫోన్ సౌకార్యం')
        elif distance_var == 'b':
            dcom['ft'].append('ల్యాండ్లైన్ టెలిఫోన్ సౌకార్యం')
        elif distance_var == 'a':
            dcom['f'].append('ల్యాండ్లైన్ టెలిఫోన్ సౌకార్యం')

    elif type_check(info_df.loc[k, ('Telephone (landlines) (Status A(1)/NA(2))')]) == 1:
        dcom['z'].append('ల్యాండ్లైన్ టెలిఫోన్ సౌకార్యం')



# In[86]:


# def get_public_call_status(info_df, k, dcom):
#     if type_check(info_df.loc[k, ('Public Call Office /Mobile (PCO) (Status A(1)/NA(2))')]) > 1:
#         distance_var = info_df.loc[k, ('(If Public Call Office /Mobile (PCO) not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
#         if pd.isna(distance_var):
#             return 'పబ్లిక్ కాల్ కార్యాలయం లేదు'
        
#         elif distance_var == 'c':
#             return 'పబ్లిక్ కాల్ కార్యాలయం గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉంది'
#         elif distance_var == 'b':
#             return 'పబ్లిక్ కాల్ కార్యాలయం గ్రామానికి 5-10 కి.మీ. సమీపం లో ఉంది'
#         return 'పబ్లిక్ కాల్ కార్యాలయం గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నవి'
    
#     return 'పబ్లిక్ కాల్ కార్యాలయం ఉంది'


# In[87]:


def get_mobile_coverage_status(info_df, k, dcom):
    if type_check(info_df.loc[k, ('Mobile Phone Coverage (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Mobile Phone Coverage not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return
        if distance_var == 'c':
            dcom['t'].append('మొబైల్ ఫోను కవరేజి')
        elif distance_var == 'b':
            dcom['ft'].append('మొబైల్ ఫోను కవరేజి')
        elif distance_var == 'a':
            dcom['f'].append('మొబైల్ ఫోను కవరేజి')

    elif type_check(info_df.loc[k, ('Mobile Phone Coverage (Status A(1)/NA(2))')]) == 1:
        dcom['z'].append('మొబైల్ ఫోను కవరేజి')


# In[108]:


def get_internet_cafe_status(info_df, k, dcom):
    if type_check(info_df.loc[k, ('Internet Cafes / Common Service Centre (CSC) (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Internet Cafes / Common Service Centre (CSC) not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]

        if pd.isna(distance_var):
            return
        if distance_var == 'c':
            dcom['t'].append('ఇంటర్నెట్')
        elif distance_var == 'b':
            dcom['ft'].append('ఇంటర్నెట్')
        elif distance_var == 'a':
            dcom['f'].append('ఇంటర్నెట్')

    elif type_check(info_df.loc[k, ('Internet Cafes / Common Service Centre (CSC) (Status A(1)/NA(2))')]) == 1:
        dcom['z'].append('ఇంటర్నెట్')     


# In[88]:


def get_private_courier_status(info_df, k, dcom):
    if type_check(info_df.loc[k, ('Private Courier Facility (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Private Courier Facility not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return
        if distance_var == 'c':
            dcom['t'].append('ప్రైవేటు కొరియర్')
        elif distance_var == 'b':
            dcom['ft'].append('ప్రైవేటు కొరియర్')
        elif distance_var == 'a':
            dcom['f'].append('ప్రైవేటు కొరియర్')

    elif type_check(info_df.loc[k, ('Private Courier Facility (Status A(1)/NA(2))')]) == 1:
        dcom['z'].append('ప్రైవేటు కొరియర్')


# In[106]:

def get_communication (info_df, k):
    dcom = {}
    dcom['z'] = []
    dcom['f'] = []
    dcom['ft'] = []
    dcom['t'] = []
    get_private_courier_status(info_df, k, dcom)
    get_internet_cafe_status(info_df, k, dcom)
    get_mobile_coverage_status(info_df, k, dcom)
    get_landline_status(info_df, k, dcom)
    return dcom



def get_railway_service_status(info_df, k):
    if type_check(info_df.loc[k, ('Railway Station (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Railway Station not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return 'గ్రామంలో రైల్వే రవాణా సౌకర్యం లేదు'
        
        elif distance_var == 'c':
            return 'రైల్వే రవాణా సౌకర్యం ఈ ఊరికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉంది'
        elif distance_var == 'b':
            return 'రైల్వే రవాణా సౌకర్యం ఈ ఊరికి 5-10 కి.మీ. సమీపం లో ఉంది'
        return 'రైల్వే రవాణా సౌకర్యం ఈ ఊరికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నవి'
    
    return 'గ్రామంలో రైల్వే రవాణా సౌకర్యం ఉంది'
 


# In[89]:


def get_bus_service_status(info_df, k):
    if type_check(info_df.loc[k, ('Public Bus Service (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Public Bus Service not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return 'గ్రామంలో బస్సు రవాణా సౌకర్యం లేదు'
        
        elif distance_var == 'c':
            return 'బస్సు రవాణా సౌకర్యం ఈ ఊరికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉంది'
        elif distance_var == 'b':
            return 'బస్సు రవాణా సౌకర్యం ఈ ఊరికి 5-10 కి.మీ. సమీపం లో ఉంది'
        return 'బస్సు రవాణా సౌకర్యం ఈ ఊరికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నవి'
    
    return 'గ్రామంలో బస్సు రవాణా సౌకర్యం ఉంది'


# In[90]:


def get_atm_status(info_df, k):
    if type_check(info_df.loc[k, ('ATM (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('Nearest Facility Distance (in Km) ')]
        
        if pd.isna(distance_var):
            return 'గ్రామంలో ATMలు లేవు'
        
        elif distance_var == 'c':
            return 'ATMలు 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నాయి'
        elif distance_var == 'b':
            return 'ATMలు 5-10 కి.మీ. సమీపం లో ఉన్నాయి'
        return 'ATMలు 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నాయి'
    
    return 'గ్రామంలో ATMలు ఉన్నాయి'


# In[91]:


def get_banks_status(info_df, k):
    return_str = ''
    commercial_bank = True
    
    if type_check(info_df.loc[k, ('Commercial Bank (Status A(1)/NA(2))')]) > 1:
        # global return_str
        distance_var = info_df.loc[k, ('(If Commercial Bank not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return_str = 'గ్రామంలో వాణిజ్య బ్యాంకులు లేవు'
            commercial_bank = False
        
        elif distance_var == 'c':
            return_str = 'వాణిజ్య బ్యాంకులు గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నాయి'
        elif distance_var == 'b':
            return_str = 'వాణిజ్య బ్యాంకులు గ్రామానికి 5-10 కి.మీ. సమీపం లో ఉన్నాయి'
        else:
            return_str = 'వాణిజ్య బ్యాంకులు గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నాయి'
    else:
        retrun_str = 'గ్రామంలో వాణిజ్య బ్యాంకులు ఉన్నాయి'
    
    if commercial_bank:
        return_str += ', '
    
    if type_check(info_df.loc[k, ('Cooperative Bank (Status A(1)/NA(2))')]) > 1:
        distance_var = info_df.loc[k, ('(If Cooperative Bank not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ')]
        
        if pd.isna(distance_var):
            return_str += 'సహకార బ్యాంకులు లేవు'
        
        elif distance_var == 'c':
            return_str += 'సహకార బ్యాంకులు గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నాయి'
        elif distance_var == 'b':
            return_str += 'సహకార బ్యాంకులు గ్రామానికి 5-10 కి.మీ. సమీపం లో ఉన్నాయి'
        else:
            return_str += 'సహకార బ్యాంకులు గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నాయి'
    else:
        return_str += 'గ్రామంలో సహకార బ్యాంకులు ఉన్నాయి'
    
    return return_str


# In[92]:


def get_domestic_power_status(info_df, i):
    power_var = type_check(info_df.loc[i, ('Power Supply For Domestic Use (Status A(1)/NA(2))')])
    
    if pd.notna(power_var):
        if power_var < 2:
            return 'ఉన్నది'
    return 'లేదు'


# In[93]:


def get_agriculture_power_status(info_df, i):
    power_var = type_check(info_df.loc[i, ('Power Supply For Agriculture Use (Status A(1)/NA(2))')])
    
    if pd.notna(power_var):
        if power_var < 2:
            return 'ఉన్నది'
    return 'లేదు'


# In[94]:


def get_commercial_power_status(info_df, i):
    power_var = type_check(info_df.loc[i, ('Power Supply For Commercial Use (Status A(1)/NA(2))')])
    
    if pd.notna(power_var):
        if power_var < 2:
            return 'ఉన్నది'
    return 'లేదు'


# In[95]:


def get_all_users_power_status(info_df, i):
    power_var = type_check(info_df.loc[i, ('Power Supply For All Users (Status A(1)/NA(2))')])
    
    if pd.notna(power_var):
        if power_var < 2:
            return 'ఉన్నది'
    return 'లేదు'


# In[97]:


def get_first_agricultural_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Agricultural Commodities (First) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_second_agricultural_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Agricultural Commodities (Second) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_third_agricultural_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Agricultural Commodities (Third) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'


# In[98]:


def get_first_manufacturers_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Manufacturers Commodities (First) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_second_manufacturers_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Manufacturers Commodities (Second) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_third_manufacturers_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Manufacturers Commodities (Third) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'


# In[99]:


def get_first_handicrafts_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Handicrafts Commodities (First) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_second_handicrafts_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Handicrafts Commodities (Second) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'

def get_third_handicrafts_commodity(info_df, i):
    commodity_var = info_df.loc[i, ('Handicrafts Commodities (Third) Telugu')]
    if pd.notna(commodity_var):
        return commodity_var
    return '-'


# In[100]:


entertainet_status_array = ['Sports Field (Status A(1)/NA(2))',
                           'Sports Club/Recreation Centre (Status A(1)/NA(2))',
                           'Cinema/Video Hall (Status A(1)/NA(2))',
                           'Public Library (Status A(1)/NA(2))',
                           'Public Reading Room (Status A(1)/NA(2))']
                        #    'Daily Newspaper Supply (Status A(1)/NA(2))']

entertainment_distance_array = ['(If Sports Field not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If Sports Club/Recreation Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If Cinema/Video Hall not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If Public Library not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If Public Reading Room not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If Daily Newspaper Supply not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

entertainment_translated_array = ['క్రీడా మైదానాలు',
                                 'క్రీడా మైదానాలు/వినోద కేంద్రాలు',
                                 'సినిమా/వీడియో హాళ్లు',
                                 'ప్రజా గ్రంథాలయాలు',
                                 'ప్రజా పఠన గదులు']
                                #  'రోజువారీ వార్తాపత్రిక సరఫరా']


# In[101]:


def get_entertainment_status(info_df, i):
    in_village = []
    outside = {}
    return_str = ''
    
    for index in range(len(entertainet_status_array)):
        
        if type_check(info_df.loc[i, (entertainet_status_array[index])]) > 1:
            distance_var = info_df.loc[i, (entertainment_distance_array[index])]

            if pd.notna(distance_var):
                if distance_var == 'a':
                    if 'a' not in outside:
                        outside['a'] = []
                    outside['a'].append(entertainment_translated_array[index])
                elif distance_var == 'b':
                    if 'b' not in outside:
                        outside['b'] = []
                    outside['b'].append(entertainment_translated_array[index])
                elif distance_var == 'c':
                    if 'c' not in outside:
                        outside['c'] = []
                    outside['c'].append(entertainment_translated_array[index])
        else:
            in_village.append(entertainment_translated_array[index])
    
    if len(in_village) > 0:
        return_str = '*' + 'గ్రామంలో ' + ', '.join(in_village) + ' ఉన్నాయి.\n'
    
    if len(outside) > 0:
        if 'a' in outside:
            return_str += '*' + ', '.join(outside['a']) + ' గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో ఉన్నాయి.\n'
        if  'b' in outside:
            return_str += '*' + ', '.join(outside['b']) + ' గ్రామానికి 5-10 కి.మీ. సమీపం లో ఉన్నాయి.\n'
        if 'c' in outside:
            return_str += '*' + ', '.join(outside['c']) + ' గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో ఉన్నాయి.\n'
    
    return return_str[:-1] if return_str[-1:] == '\n' else return_str


# In[67]:


other_details_array = ['Birth and Death Registration Office (Status A(1)/NA(2))',
                      'National Highway (Status A(1)/NA(2))']

other_details_distance_array = ['(If Birth and Death Registration Office not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                               '(If National Highway not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

other_details_translated_array = ['జనన మరియు మరణ నమోదు కార్యాలయం',
                                 'జాతీయ రహదారి']


# In[102]:


def get_other_details(info_df, i):
    return_dict = {}
    return_str = ''
    for index in range(len(other_details_array)):
        
        if type_check(info_df.loc[i, other_details_array[index]]) > 1:
            distance_var = info_df.loc[i, (other_details_distance_array[index])]
            
            if pd.notna(distance_var):
                if distance_var == 'a':
                    if 'a' not in return_dict:
                        return_dict['a'] = []
                    return_dict['a'].append(other_details_translated_array[index])
                elif distance_var == 'b':
                    if 'b' not in return_dict:
                        return_dict['b'] = []
                    return_dict['b'].append(other_details_translated_array[index])
                elif distance_var == 'c':
                    if 'c' not in return_dict:
                        return_dict['c'] = []
                    return_dict['c'].append(other_details_translated_array[index])
        else:
            if 'inside' not in return_dict:
                return_dict['inside'] = []
            return_dict['inside'].append(other_details_translated_array[index])
    
    if 'inside' in return_dict:
        return_str += '*గ్రామంలో ' + ', '.join(return_dict['inside'])
        return_str += ' ఉంది.\n' if len(return_dict['inside']) == 1 else ' ఉన్నాయి.\n'
    
    if 'a' in return_dict:
        return_str += '*' + ', '.join(return_dict['a']) + ' గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో'
        return_str += ' ఉంది.\n' if len(return_dict['a']) == 1 else ' ఉన్నాయి.\n'
        
    if  'b' in return_dict:
        return_str += '*' + ', '.join(return_dict['b']) + ' గ్రామానికి 5-10 కి.మీ. సమీపం లో'
        return_str += ' ఉంది.\n' if len(return_dict['b']) == 1 else ' ఉన్నాయి.\n'
            
    if 'c' in return_dict:
        return_str += '*' + ', '.join(return_dict['c']) + ' గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో'
        return_str += ' ఉంది.\n' if len(return_dict['c']) == 1 else ' ఉన్నాయి.\n'
    
    return return_str[:-1] if return_str[-1:] == '\n' else return_str


# In[69]:


nutrition_centres_array = ['Nutritional Centres-ICDS (Status A(1)/NA(2))',
                          'Nutritional Centres-Anganwadi Centre (Status A(1)/NA(2))']

nutrition_distance_array = ['(If Nutritional Centres-ICDS not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                            '(If Nutritional Centres-Anganwadi Centre not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

nutrition_translated_array = ['పోషకాహార కేంద్రాలు - ఐసిడిఎస్(సమగ్ర పిల్లల అభివృద్ధి సేవలు)',
                             'పోషకాహార కేంద్రాలు - అంగన్వాడి కేంద్రాలు']


# In[103]:


def get_nutritional_status(info_df, i):
    return_dict = {}
    return_str = ''
    
    for index in range(len(nutrition_centres_array)):
        
        if type_check(info_df.loc[i, nutrition_centres_array[index]]) > 1:
            distance_var = info_df.loc[i, (nutrition_distance_array[index])]
            
            if pd.notna(distance_var):
                if distance_var == 'a':
                    if 'a' not in return_dict:
                        return_dict['a'] = []
                    return_dict['a'].append(nutrition_translated_array[index])
                elif distance_var == 'b':
                    if 'b' not in return_dict:
                        return_dict['b'] = []
                    return_dict['b'].append(nutrition_translated_array[index])
                elif distance_var == 'c':
                    if 'c' not in return_dict:
                        return_dict['c'] = []
                    return_dict['c'].append(nutrition_translated_array[index])
        else:
            if 'inside' not in return_dict:
                return_dict['inside'] = []
            return_dict['inside'].append(nutrition_translated_array[index])
    
    if 'inside' in return_dict:
        return_str += '*గ్రామంలో ' + ', '.join(return_dict['inside']) + ' ఉన్నాయి.\n'
    
    if 'a' in return_dict:
        return_str += '*' + ', '.join(return_dict['a']) + ' గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో' + ' ఉన్నాయి.\n'
        
    if  'b' in return_dict:
        return_str += '*' + ', '.join(return_dict['b']) + ' గ్రామానికి 5-10 కి.మీ. సమీపం లో' + ' ఉన్నాయి.\n'
            
    if 'c' in return_dict:
        return_str += '*' + ', '.join(return_dict['c']) + ' గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో' + ' ఉన్నాయి.\n'
    
    return return_str[:-1] if return_str[-1:] == '\n' else return_str


# In[71]:


market_array = ['Public Distribution System (PDS) Shop (Status A(1)/NA(2))',
               'Mandis/Regular Market (Status A(1)/NA(2))',
               'Weekly Haat (Status A(1)/NA(2))',
               'Agricultural Marketing Society (Status A(1)/NA(2))']

market_distance_array = ['(If Public Distribution System (PDS) Shop not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Mandis/Regular Market not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Weekly Haat not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ',
                        '(If Agricultural Marketing Society not available within the village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']

market_translated_array = ['ప్రజా పంపిణీ వ్యవస్థ (పిడిఎస్) దుకాణాలు',
                          'మండీలు/సాధారణ మార్కెట్లు',
                          'వారంవారీ మార్కెట్లు',
                          'వ్యవసాయ మార్కెటింగ్ సంఘాలు']


# In[104]:


def get_markets_status(info_df, i):
    return_dict = {}
    return_str = ''
    
    for index in range(len(market_array)):
        
        if type_check(info_df.loc[i, market_array[index]]) > 1:
            distance_var = info_df.loc[i, (market_distance_array[index])]
            
            if pd.notna(distance_var):
                if distance_var == 'a':
                    if 'a' not in return_dict:
                        return_dict['a'] = []
                    return_dict['a'].append(market_translated_array[index])
                elif distance_var == 'b':
                    if 'b' not in return_dict:
                        return_dict['b'] = []
                    return_dict['b'].append(market_translated_array[index])
                elif distance_var == 'c':
                    if 'c' not in return_dict:
                        return_dict['c'] = []
                    return_dict['c'].append(market_translated_array[index])
        else:
            if 'inside' not in return_dict:
                return_dict['inside'] = []
            return_dict['inside'].append(market_translated_array[index])
    
    if 'inside' in return_dict:
        return_str += '*గ్రామంలో ' + ', '.join(return_dict['inside']) + ' ఉన్నాయి.\n'
    
    if 'a' in return_dict:
        return_str += '*' + ', '.join(return_dict['a']) + ' గ్రామానికి 5 కి.మీ. కంటే తక్కువ సమీపంలో' + ' ఉన్నాయి.\n'
        
    if  'b' in return_dict:
        return_str += '*' + ', '.join(return_dict['b']) + ' గ్రామానికి 5-10 కి.మీ. సమీపం లో' + ' ఉన్నాయి.\n'
            
    if 'c' in return_dict:
        return_str += '*' + ', '.join(return_dict['c']) + ' గ్రామానికి 10 కి.మీ. కంటే ఎక్కువ దూరంలో లో' + ' ఉన్నాయి.\n'
    
    return return_str[:-1] if return_str[-1:] == '\n' else return_str


# In[73]:

def check_power (param):
    # print(type(param))
    if pd.isna(param):
        return 0.0
    else:
        return param
# k = 91738
# In[109]:

def get_wikitext (sample_data, k, template):
    cleaning(sample_data)
    template = env.get_template("./templates/" + template)
    output = template.render(village_name = sample_data.loc[k, ('Name Telugu')],
                            educational_centres = get_educational_centres(sample_data, k),
                            medical_centres = get_medical_centres(sample_data, k),
                            drainage_release_method = get_drainge_release_method(sample_data, k),
                            drainage_method = get_driange_scheme(sample_data, k),
                            # post_office_status = get_post_office_status(sample_data, k),

                            # pincode = sample_data.loc[k, ('Pincode')],
                            pincode = decide_pincode(sample_data.loc[k, ('Pincode')]),
                            comm = get_communication(sample_data, k),

                            # landline_status = get_landline_status(sample_data, k),
                            # public_call_status = get_public_call_status(sample_data, k),
                            # mobile_coverage = get_mobile_coverage_status(sample_data, k),
                            # internet_cafes = get_internet_cafe_status(sample_data, k),
                            # private_courier = get_private_courier_status(sample_data, k),
                            bus_service = get_bus_service_status(sample_data, k),
                            railway_service = get_railway_service_status(sample_data, k),
                            markets = get_markets_status(sample_data, k),
                            atm = get_atm_status(sample_data, k),
                            banks = get_banks_status(sample_data, k),
                            total_area = sample_data.loc[k, ('Total Geographical Area (in Hectares)')],
                            forest_area = sample_data.loc[k, ('Forest Area (in Hectares)')],
                            non_agricultural_land = sample_data.loc[k, ('Area under Non-Agricultural Uses (in Hectares)')],
                            uncultivable_land = sample_data.loc[k, ('Barren & Un-cultivable Land Area (in Hectares)')],
                            grazing_land = sample_data.loc[k, ('Permanent Pastures and Other Grazing Land Area (in Hectares)')],
                            unirrigated_land = sample_data.loc[k, ('Total Unirrigated Land Area (in Hectares)')],
                            sown_area = sample_data.loc[k, ('Net Area Sown (in Hectares)')],
                            canals_area = sample_data.loc[k, ('Canals Area (in Hectares)')],
                            tree_land = sample_data.loc[k, ('Land Under Miscellaneous Tree Crops etc. Area (in Hectares)')],
                            cultivate_waste_land = sample_data.loc[k, ('Culturable Waste Land Area (in Hectares)')],
                            domestic_power_status = get_domestic_power_status(sample_data, k),

                            domestic_summer_power_usage = check_power(sample_data.loc[k, ('Power Supply For Domestic Use Summer (April-Sept.) per day (in Hours)')]),
                            domestic_winter_power_usage = check_power(sample_data.loc[k, ('Power Supply For Domestic Use Winter (Oct.-March) per day (in Hours)')]),
                            agriculture_power_status = get_agriculture_power_status(sample_data, k),

                            agriculture_summer_power_usage = check_power(sample_data.loc[k, ('Power Supply For Agriculture Use Summer (April-Sept.) per day (in Hours)')]),
                            agriculture_winter_power_usage = check_power(sample_data.loc[k, ('Power Supply For Agriculture Use Winter (Oct.-March)per day (in Hours)')]),
                            commercial_power_status = get_commercial_power_status(sample_data, k),

                            commercial_summer_power_usage = check_power(sample_data.loc[k, ('Power Supply For Commercial Use Summer (April-Sept.) per day (in Hours)')]),
                            commercial_winter_power_usage = check_power(sample_data.loc[k, ('Power Supply For Commercial Use Winter (Oct.-March) per day (in Hours)')]),
                            all_users_power_status = get_all_users_power_status(sample_data, k),

                            all_users_summer_power_usage = check_power(sample_data.loc[k, ('Power Supply For All Users Summer (April-Sept.) per day (in Hours)')]),
                            all_users_winter_power_usage = check_power(sample_data.loc[k, ('Power Supply For All Users Winter (Oct.-March) per day (in Hours)')]),

                            first_agricultural_commodity = get_first_agricultural_commodity(sample_data, k),
                            second_agricultural_commodity = get_second_agricultural_commodity(sample_data, k),
                            third_agricultural_commodity = get_third_agricultural_commodity(sample_data, k),
                            first_manufacturers_commodity = get_first_manufacturers_commodity(sample_data, k),
                            second_manufacturers_commodity = get_second_manufacturers_commodity(sample_data, k),
                            third_manufacturers_commodity = get_third_manufacturers_commodity(sample_data, k),
                            first_handicrafts_commodity = get_first_handicrafts_commodity(sample_data, k),
                            second_handicrafts_commodity = get_second_handicrafts_commodity(sample_data, k),
                            third_handicrafts_commodity = get_third_handicrafts_commodity(sample_data, k),
                            entertainment = get_entertainment_status(sample_data, k),
                            other_details = get_other_details(sample_data, k),
                            nutritional_centers = get_nutritional_status(sample_data, k),
                            state_tel = sample_data.loc[k, 'State Name Telugu'],
                            district_tel = sample_data.loc[k, 'District Name Telugu']
                            )
    return output

# print(get_wikitext(sample_data, 91738))


# In[ ]:


# var = sample_data.loc[1149, ('Manufacturers Commodities (Second) Telugu')]
# pd.isna(var)


# In[ ]:




