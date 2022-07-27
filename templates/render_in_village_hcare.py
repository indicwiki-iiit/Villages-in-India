from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/in_village_healthcare.j2')

# basic = []
# non_govt = []
def type_check (param):
    if pd.isna(param):
        return 0
    else:
        return int(float(param))

def fill_my_lst (numbers, n_doctors, n_paramedical_staff, facility, type, sample_df, idx, basic, non_govt):
    if type_check(sample_df.loc[idx, numbers]) > 0:
        if type == 'basic':
            record = {}
            record['facility'] = facility
            record['numbers'] = type_check(sample_df.loc[idx, numbers])
            record['n_doctors'] = type_check(sample_df.loc[idx, n_doctors])
            record['n_paramedical_staff'] = type_check(sample_df.loc[idx, n_paramedical_staff])
            basic.append(record)
        elif type == 'non_govt':
            record = {}
            record['facility'] = facility
            record['numbers'] = type_check(sample_df.loc[idx, numbers])
            non_govt.append(record)


def render_in_village_hcare(sample_df, idx):
    basic = []
    non_govt = []
    health_statuses = ['Community Health Centre (Numbers)', 'Primary Health Centre (Numbers)',
                       'Primary Health Sub Centre (Numbers)', 'Maternity And Child Welfare Centre (Numbers)',
                       'TB Clinic (Numbers)', 'Hospital Allopathic (Numbers)', 'Dispensary (Numbers)', 
                       'Veterinary Hospital (Numbers)', 'Mobile Health Clinic (Numbers)', 
                       'Family Welfare Centre (Numbers)'
                      ]
    additional = ['Non Government Medical facilities Out Patient (Numbers)',
                  'Non Government Medical facilities In And Out Patient (Numbers)',
                  'Non Government Medical facilities Charitable (Numbers)',
                  'Non Government Medical facilities Medical Practitioner with MBBS Degree (Numbers) ',
                  'Non Government Medical facilities Traditional Practitioner and Faith Healer (Numbers) ',
                  'Non Government Medical facilities Medicine Shop (Numbers) '
                 ]
                 
    health_facilities = ['సామాజిక ఆరోగ్య కేంద్రం', 'ప్రాథమిక ఆరోగ్య కేంద్రం', 'ప్రాథమిక ఆరోగ్య ఉప కేంద్రం',
                         'ప్రసూతి, శిశు సంక్షేమ కేంద్రం', 'TB క్లినిక్', 'అల్లోపతి ఆసుపత్రి', 'డిస్పెన్సరీ', 'వెర్టర్నరీ ఆసుపత్రి',
                         'మొబైల్ క్లినిక్', 'కుటుంబ సంక్షేమ కేంద్రం', 'ఔట్ పేషెంట్ సౌకర్యం', 'ఇన్ మరియు ఔట్ పేషెంట్ సౌకర్యం',
                         'ఛారిటబుల్ ఆసుపత్రి', 'MBBS డిగ్రీతో మెడికల్ ప్రాక్టీషనర్', 'హీలింగ్ క్లినిక్',
                         'మందుల దుకాణం'
                        ]
    
    i = 0
    j = 0
    while ( i < len(health_statuses) ):
        n_doctors = health_statuses[i].replace("(Numbers)", "Doctors Total Strength (Numbers)")
        if health_statuses[i] == 'TB Clinic (Numbers)':
            n_paramedical_staff = health_statuses[i].replace("(Numbers)", "Para Medical Para Medical Staff Total Strength (Numbers)")
        else:
            n_paramedical_staff = health_statuses[i].replace("(Numbers)", "Para Medical Staff Total Strength (Numbers)")
        fill_my_lst( health_statuses[i], n_doctors, n_paramedical_staff, health_facilities[j], 'basic', sample_df, idx, basic, non_govt )
        i += 1
        j += 1

    i = 0
    while ( i < len(additional) ):
        fill_my_lst( additional[i], 0, 0, health_facilities[j], 'non_govt', sample_df, idx, basic, non_govt )
        i += 1
        j += 1


    return template.render( basic = basic, non_govt = non_govt )


# print(render_in_village_hcare(1))