from jinja2 import Environment, FileSystemLoader
import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/governance.j2')

def type_check (param):
    if pd.isna(param):
        return 2
    else:
        return int(float(param))

def NACheck (param):
    if pd.isna(param):
        return 'nan'
    else:
        return param


def render_governance(sample_df, idx):
    record = {}
    record['name'] = sample_df.loc[idx, 'Name Telugu']
    record['CD_block'] = NACheck(sample_df.loc[idx, 'CD Block Name Telugu'])
    # record['CD_block_code'] = int(sample_df.loc[idx, 'CD Block Code'])
    record['gram_panchayat'] = NACheck(sample_df.loc[idx, 'Gram Panchayat Name Telugu'])
    # record['gram_panchayat_code'] = int(sample_df.loc[idx, 'Gram Panchayat Code'])
    record['subdist_HQ'] = NACheck(sample_df.loc[idx, 'Sub District Head Quarter (Name) Telugu'])
    record['subdist_HQ_dist'] = sample_df.loc[idx, 'Sub District Head Quarter (Distance in km)']
    record['district_HQ'] = NACheck(sample_df.loc[idx, 'District Head Quarter (Name) Telugu'])
    record['district_HQ_dist'] = sample_df.loc[idx, 'District Head Quarter (Distance in km)']
    record['statutory_town'] = NACheck(sample_df.loc[idx, 'Nearest Statutory Town (Name) Telugu'])
    record['statutory_town_dist'] = sample_df.loc[idx, 'Nearest Statutory Town (Distance in km)']
    record['polling_station_status'] = type_check(sample_df.loc[idx, 'Assembly Polling Station (Status A(1)/NA(2))'])

    # print(sample_df.loc[idx, 'Name'])

    record['if_no_dist_PS'] = sample_df.loc[idx, '(If Assembly Polling Station not available within the village, '+
    'the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and c for 10+ kms ). ']



    return template.render(record)


# print(render_governance(1))