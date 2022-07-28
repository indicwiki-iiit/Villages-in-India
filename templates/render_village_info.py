from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/village_info.j2')

def check_dist (dist):
    if pd.isna(dist):
        return 'nan'
    else:
        return dist

def render_village_info(sample_df, idx):
    record = {}
    record['name'] = sample_df.loc[idx, 'Name Telugu']
    record['village_code'] = sample_df.loc[idx, 'Town/Village']
    record['total_population'] = sample_df.loc[idx, 'TOT_P']
    record['total_households'] = sample_df.loc[idx, 'No_HH']
    record['nearest_town'] = sample_df.loc[idx, 'Nearest Town Name Telugu']
    record['nearest_town_dist'] = check_dist(sample_df.loc[idx, 'Nearest Town Distance from Village (in Km.)'])
    record['latitude'] = sample_df.loc[idx, 'Latitude']
    record['longitude'] = sample_df.loc[idx, 'Longitude']
    record['elevation'] = sample_df.loc[idx, 'Elevation']
    record['total_area'] = sample_df.loc[idx, 'Total Geographical Area (in Hectares)']

    return template.render(record)