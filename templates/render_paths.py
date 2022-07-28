from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)
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

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/paths.j2')

def render_paths(sample_df, idx):
    record = {}
    record['nat_highway_s'] = type_check(sample_df.loc[idx, 'National Highway (Status A(1)/NA(2))'])
    record['if_no_dist_nat_highway'] = NACheck(sample_df.loc[idx, '(If National Highway not available within the village, '+ 
    'the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and ' +
    'c for 10+ kms ). '])

    record['state_highway_s'] = type_check(sample_df.loc[idx, 'State Highway (Status A(1)/NA(2))'])
    record['if_no_dist_state_highway'] = NACheck(sample_df.loc[idx, '(If State Highway not available within the village, '+ 
    'the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and ' +
    'c for 10+ kms ). '])

    record['major_dist_road_s'] = type_check(sample_df.loc[idx, 'Major District Road (Status A(1)/NA(2))'])
    record['if_no_dist_major_road'] = NACheck(sample_df.loc[idx, '(If Major District Road not available within the village, '+ 
    'the distance range code of nearest place where facility is available is given viz; a for < 5 Kms, b for 5-10 Kms and ' +
    'c for 10+ kms ). '])

    record['black_top_road_s'] = type_check(sample_df.loc[idx, 'Black Topped (pucca) Road (Status A(1)/NA(2))'])
    record['gravel_road_s'] = type_check(sample_df.loc[idx, 'Gravel (kuchha) Roads (Status A(1)/NA(2))'])


    return template.render(record)


# print(render_paths(1))