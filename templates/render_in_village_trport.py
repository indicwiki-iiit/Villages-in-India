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

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/in_village_transport.j2')

def render_in_village_tport(sample_df, idx):
    record = {}
    record['public_bus'] = type_check(sample_df.loc[idx, 'Public Bus Service (Status A(1)/NA(2))'])
    record['private_bus'] = type_check(sample_df.loc[idx, 'Private Bus Service (Status A(1)/NA(2))'])
    record['railway'] = type_check(sample_df.loc[idx, 'Railway Station (Status A(1)/NA(2))'])
    record['auto'] = type_check(sample_df.loc[idx, 'Auto/Modified Autos (Status A(1)/NA(2))'])
    record['taxi'] = type_check(sample_df.loc[idx, 'Taxi (Status A(1)/NA(2))'])
    record['vans'] = type_check(sample_df.loc[idx, 'Vans (Status A(1)/NA(2))'])
    record['tractors'] = type_check(sample_df.loc[idx, 'Tractors (Status A(1)/NA(2))'])
    record['cpr_manual'] = type_check(sample_df.loc[idx, 'Cycle-pulled Rickshaws  (manual driven) (Status A(1)/NA(2))'])
    record['cpr_machine'] = type_check(sample_df.loc[idx, 'Cycle-pulled Rickshaws (machine driven) (Status A(1)/NA(2))'])
    record['carts'] = type_check(sample_df.loc[idx, 'Carts Driven by Animals (Status A(1)/NA(2))'])
    record['waterways'] = type_check(sample_df.loc[idx, 'Sea/River/Ferry Service (Status A(1)/NA(2))'])


    return template.render(record)


# print(render_in_village_tport(1))