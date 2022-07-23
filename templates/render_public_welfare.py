from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/public_welfare.j2')

def type_check (param):
    if pd.isna(param):
        return 2
    else:
        return int(float(param))

def render_public_welfare(sample_df, idx):
    record = {}
    # record['name'] = sample_df.loc[df_indices[2], 'Name Telugu']

    record['ACS_status'] = type_check(sample_df.loc[idx, 'Agricultural Credit Societies (Status A(1)/NA(2))'])
    record['if_no_dist_ACS'] = sample_df.loc[idx, '(If Agricultural Credit Societies not available within the ' + 
    'village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for '+
    '5-10 Kms and c for 10+ kms ). ']

    record['PDS_status'] = type_check(sample_df.loc[idx, 'Public Distribution System (PDS) Shop (Status A(1)/NA(2))'])
    record['if_no_dist_PDS'] = sample_df.loc[idx, '(If Public Distribution System (PDS) Shop not available within the ' + 
    'village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for '+
    '5-10 Kms and c for 10+ kms ). ']

    record['SHG_status'] = type_check(sample_df.loc[idx, 'Self - Help Group (SHG) (Status A(1)/NA(2))'])
    record['if_no_dist_SHG'] = sample_df.loc[idx, '(If Self - Help Group (SHG) not available within the ' + 
    'village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for '+
    '5-10 Kms and c for 10+ kms ). ']

    record['ASHA_status'] = type_check(sample_df.loc[idx, 'ASHA (Status A(1)/NA(2))'])
    record['if_no_dist_ASHA'] = sample_df.loc[idx, '(If ASHA not available within the ' + 
    'village, the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for '+
    '5-10 Kms and c for 10+ kms ). ']

    return template.render(record)


# print(render_public_welfare(1))