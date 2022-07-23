from jinja2 import Environment, FileSystemLoader
# import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

def capcase_state_eng (state):
    if state == 'JAMMU & KASHMIR':
        state = 'JAMMU and KASHMIR'
    return " ".join( [ word[0] + word[1:].lower() for word in state.split(" ") ] )

# if pin1 and pin2 both nan return pin1
# if pin1 is nan and pin2 is !nan return pin1
# if pin1 is !nan and pin2 is nan return pin2
# if pin1 = pin2 return pin1
# if pin1 != pin2 and pin1 != nan and pin2 != nan return pin2
# sample_df.loc[ idx, 'Pincode' ] = np.nan
# sample_df.loc[ idx, 'PIN Code' ] = 344025

def decide_pincode (pin1, pin2):
    if pin1 == pin2 and str(pin1) != 'nan' and str(pin2) != 'nan':
        return int(pin1)
    elif str(pin1) == 'nan' and str(pin2) != 'nan':
        pin2 = float(pin2)
        return int(pin2)
    elif str(pin1) != 'nan' and str(pin2) == 'nan':
        return int(pin1)
    elif pin1 != pin2 and str(pin1) != 'nan' and str(pin2) != 'nan':
        pin2 = float(pin2)
        return int(pin2)
    else: # both pin1 and pin2 are null
        return pin1


file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/infobox.j2')

def render_infobox(sample_df, idx):

    record = {}
    record['name'] = sample_df.loc[idx, 'Name Telugu']
    record['state_eng'] = capcase_state_eng ( sample_df.loc[idx, 'State Name'] )
    record['latitude'] = sample_df.loc[idx, 'Latitude']
    record['longitude'] = sample_df.loc[idx, 'Longitude']
    record['state_tel'] = sample_df.loc[idx, 'State Name Telugu']
    record['district'] = sample_df.loc[idx, 'District Name Telugu']
    record['subdistrict'] = sample_df.loc[idx, 'Sub District Name Telugu']
    record['total_area'] = sample_df.loc[idx, 'Total Geographical Area (in Hectares)']
    record['elevation'] = sample_df.loc[idx, 'Elevation']
    record['total_population'] = sample_df.loc[idx, 'TOT_P']
    record['pincode'] = decide_pincode ( sample_df.loc[idx, 'Pincode'], sample_df.loc[idx, 'PIN Code'] )
    # print( record['pincode'] )
    return template.render(record)

# print(render_info())
# op = render_infobox(1)
# print(op)
# with open("output.txt", "w", encoding = "utf-8") as f:
#     f.write(op)


