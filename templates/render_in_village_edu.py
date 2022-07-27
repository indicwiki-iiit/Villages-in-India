from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/in_village_education.j2')

# my_lst = []

def type_check (param):
    if pd.isna(param):
        return 2
    else:
        return int(float(param))

def num_check (param):
    if pd.isna(param):
        return 0
    else:
        return int(param)


def fill_my_lst (edu_status, edu_level, numbers, sample_df, idx, my_lst):
    if type_check(sample_df.loc[idx, edu_status]) == 1:
        record = {}
        record['edu_level'] = edu_level
        record['numbers'] = num_check(sample_df.loc[idx, numbers])
        my_lst.append(record)

def render_in_village_edu(sample_df, idx):
    my_lst = []
    edu_statuses = [ 'Govt Pre-Primary School (Nursery/LKG/UKG) (Status A(1)/NA(2))', 'Private Pre-Primary School (Nursery/LKG/UKG) (Status A(1)/NA(2))',
                     'Govt Primary School (Status A(1)/NA(2))', 'Private Primary School (Status A(1)/NA(2))',
                     'Govt Middle School (Status A(1)/NA(2))', 'Private Middle School (Status A(1)/NA(2))',
                     'Govt Secondary School (Status A(1)/NA(2))', 'Private Secondary School (Status A(1)/NA(2))',
                     'Govt Senior Secondary School (Status A(1)/NA(2))', 'Private Senior Secondary School (Status A(1)/NA(2))',
                     'Govt Arts and Science Degree College (Status A(1)/NA(2))', 'Private Arts and Science Degree College (Status A(1)/NA(2))',
                     'Govt Engineering College (Status A(1)/NA(2))','Private Engineering College (Status A(1)/NA(2))',
                     'Govt Medicine College (Status A(1)/NA(2))', 'Private Medicine College (Status A(1)/NA(2))',
                     'Govt Management Institute (Status A(1)/NA(2))', 'Private Management Institute (Status A(1)/NA(2))',
                     'Govt Polytechnic (Status A(1)/NA(2))', 'Private Polytechnic (Status A(1)/NA(2))',
                     'Govt Vocational Training School/ITI (Status A(1)/NA(2))', 'Private Vocational Training School/ITI (Status A(1)/NA(2))',
                     'Government Non Formal Training Centre (Status A(1)/NA(2))', 'Private Non Formal Training Centre (Status A(1)/NA(2))',
                     'Government School For Disabled (Status A(1)/NA(2))', 'Private School For Disabled ( Status A(1)/NA(2))',
                     'Government Others (Status A(1)/NA(2))', 'Private Others (Status A(1)/NA(2))'
                   ]

    edu_levels = [ "ప్రభుత్వ పూర్వ ప్రాథమిక పాఠశాల", "ప్రైవేట్ పూర్వ ప్రాథమిక పాఠశాల",
                   "ప్రభుత్వ ప్రాథమిక పాఠశాల", "ప్రైవేట్ ప్రాథమిక పాఠశాల",
                   "ప్రభుత్వ మధ్య పాఠశాల", "ప్రైవేట్ మధ్య పాఠశాల",
                   "ప్రభుత్వ మాధ్యమిక పాఠశాల", "ప్రైవేట్ మాధ్యమిక పాఠశాల",
                   "ప్రభుత్వ సీనియర్ సెకండరీ పాఠశాల", "ప్రైవేట్ సీనియర్ సెకండరీ పాఠశాల",
                   "ప్రభుత్వ ఆర్ట్స్ మరియు సైన్స్ డిగ్రీ కళాశాల", "ప్రైవేట్ ఆర్ట్స్ మరియు సైన్స్ డిగ్రీ కళాశాల",
                   "ప్రభుత్వ ఇంజనీరింగ్ కళాశాల", "ప్రైవేట్ ఇంజనీరింగ్ కళాశాల",
                   "ప్రభుత్వ వైద్య కళాశాల", "ప్రైవేట్ వైద్య కళాశాల",
                   "ప్రభుత్వ నిర్వహణ సంస్థ", "ప్రైవేట్ నిర్వహణ సంస్థ",
                   "ప్రభుత్వ పాలిటెక్నిక్ కళాశాల", "ప్రైవేట్ పాలిటెక్నిక్ కళాశాల",
                   "ప్రభుత్వ వృత్తివిద్యా శిక్షున", "ప్రైవేట్ వృత్తివిద్యా శిక్షున",
                   "ప్రభుత్వ అనియత శిక్షున", "ప్రైవేట్ అనియత శిక్షున",
                   "ప్రభుత్వ వికలాంగుల కోసం పాఠశాల", "ప్రైవేట్ వికలాంగుల కోసం పాఠశాల",
                   "ప్రభుత్వ ఇతర విద్యా సంస్థ", "ప్రైవేట్ ఇతర విద్యా సంస్థ"

                 ]
    
    for i in range(len(edu_statuses)):
        edu_number = edu_statuses[i].replace("(Status A(1)/NA(2))", "(Numbers)")
        fill_my_lst(edu_statuses[i], edu_levels[i], edu_number, sample_df, idx, my_lst)


    return template.render(name = sample_df.loc[idx, 'Name Telugu'], my_lst = my_lst)


# print(render_in_village_edu(1))