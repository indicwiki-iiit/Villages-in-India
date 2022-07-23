from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test2.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)
# sample_df.loc[df_indices[2], 'Elevation'] = np.nan

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/introduction.j2')

def render_intro(sample_df, idx):
    record = {}
    record['name_tel'] = sample_df.loc[idx, 'Name Telugu']
    record['name_eng'] = sample_df.loc[idx, 'Name']
    record['name_hin'] = sample_df.loc[idx, 'Name Hindi']

    record['subdistrict_tel'] = sample_df.loc[idx, 'Sub District Name Telugu']
    record['subdistrict_eng'] = sample_df.loc[idx, 'Sub District Name']
    record['subdistrict_hin'] = sample_df.loc[idx, 'Sub District Name Hindi']

    record['district_tel'] = sample_df.loc[idx, 'District Name Telugu']
    record['district_eng'] = sample_df.loc[idx, 'District Name']
    record['district_hin'] = sample_df.loc[idx, 'District Name Hindi']

    record['state_tel'] = sample_df.loc[idx, 'State Name Telugu']
    record['state_eng'] = sample_df.loc[idx, 'State Name']
    record['state_hin'] = sample_df.loc[idx, 'State Name Hindi']

    return template.render(record)


# print(render_intro(1))