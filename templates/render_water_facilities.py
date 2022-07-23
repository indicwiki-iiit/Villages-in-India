from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/water_facilities.j2')

# full_year = []
# only_summer = []
def type_check (param):
    if pd.isna(param):
        return 2
    else:
        return int(float(param))

def fill_my_lst (water_status, fy, os, facility, sample_df, idx, full_year, only_summer):
    if type_check(sample_df.loc[idx, water_status]) == 1:
        # record = {}
        if type_check(sample_df.loc[idx, fy]) == 1:
            full_year.append(facility)
        elif type_check(sample_df.loc[idx, os]) == 1:
            only_summer.append(facility)


def render_water_facilities(sample_df, idx):
    full_year = []
    only_summer = []
    water_status = ['Tap Water-Treated (Status A(1)/NA(2))', 'Tap Water Untreated (Status A(1)/NA(2))',
                    'Covered Well (Status A(1)/NA(2))', 'Uncovered Well (Status A(1)/NA(2))',
                    'Hand Pump (Status A(1)/NA(2))', 'Tube Wells/Borehole (Status A(1)/NA(2))',
                    'Spring (Status A(1)/NA(2))', 'River/Canal (Status A(1)/NA(2))',
                    'Tank/Pond/Lake (Status A(1)/NA(2))'
                   ]

    facility = ['రక్షిత పంపు నీళ్లు', 'సాధారణ పంపు నీళ్లు',
                'కప్పిన బావి నీరు', 'కప్పని బావి నీరు',
                'చేతి పంపు నీరు', 'గొట్టపు బావి/బోరు బావి నీరు',
                'ఊట నీరు', 'నది/కాలువ నీరు',
                'ట్యాంక్/చెరువు నీరు'
               ]
    
    for i in range(len(water_status)):
        fy = water_status[i].replace("(Status A(1)/NA(2))", "Functioning All round the year (Status A(1)/NA(2))")
        os = water_status[i].replace("(Status A(1)/NA(2))", "Functioning in Summer months (April-September) (Status A(1)/NA(2))")
        fill_my_lst(water_status[i], fy, os, facility[i], sample_df, idx, full_year, only_summer)
   
    return template.render(full_year = full_year, only_summer = only_summer)

# print(render_water_facilities(1))