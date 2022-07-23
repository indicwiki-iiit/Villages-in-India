from jinja2 import Environment, FileSystemLoader
import pickle
import pandas as pd
import numpy as np

# with open('test1.pkl', 'rb') as f:
#     sample_df = pickle.load(f)

# df_indices = list(sample_df.index)

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/demographics.j2')

# general = []
# main_workers = []
# marginal_workers = []

def fill_my_lst (field, total, men, women, type, sample_df, idx,  general, main_workers, marginal_workers):
    record = {}
    record['field'] = field
    record['total'] = int(sample_df.loc[idx, total])
    record['men'] = int(sample_df.loc[idx, men])
    record['women'] = int(sample_df.loc[idx, women])
    if type == 'general':
        general.append(record)
    elif type == 'main_workers':
        main_workers.append(record)
    elif type == 'marginal_workers':
        marginal_workers.append(record)

def render_demographics(sample_df, idx):
    general = []
    main_workers = []
    marginal_workers = []

    ginfo = ['TOT_P', 'TOT_M', 'TOT_F', 'P_06', 'M_06', 'F_06', 'P_SC', 'M_SC', 'F_SC', 'P_ST', 'M_ST', 'F_ST', 
             'P_LIT', 'M_LIT', 'F_LIT', 'MAINWORK_P', 'MAINWORK_M', 'MAINWORK_F', 'MARGWORK_P', 'MARGWORK_M', 'MARGWORK_F']

    maininfo = ['MAIN_CL_P', 'MAIN_CL_M', 'MAIN_CL_F', 'MAIN_AL_P', 'MAIN_AL_M', 'MAIN_AL_F', 'MAIN_HH_P',
                'MAIN_HH_M', 'MAIN_HH_F', 'MAIN_OT_P', 'MAIN_OT_M', 'MAIN_OT_F']

    marginfo = ['MARG_CL_P', 'MARG_CL_M', 'MARG_CL_F', 'MARG_AL_P', 'MARG_AL_M', 'MARG_AL_F', 'MARG_HH_P',
                'MARG_HH_M', 'MARG_HH_F', 'MARG_OT_P', 'MARG_OT_M', 'MARG_OT_F']

    fields = ['జనాభా లెక్క', '0-6 ఏళ్ళ వయసు వారు', 'షెడ్యూల్డ్ కులాలు', 'షెడ్యూల్డ్ తెగలు', 'అక్షరాస్యులు', 'ప్రధాన కార్మికులు', 'ఉపాంత కార్మికులు',
              'సాగు చేసేవారు', 'వ్యవసాయ కూలీలు', 'గృహ పరిశ్రమ కార్మికులు', 'ఇతరులు', 
              'సాగు చేసేవారు', 'వ్యవసాయ కూలీలు', 'గృహ పరిశ్రమ కార్మికులు', 'ఇతరులు' ]

    
    i = 0
    j = 0
    while ( i < len(ginfo) ):
        fill_my_lst( fields[j], ginfo[i], ginfo[i + 1], ginfo[i + 2], 'general', sample_df, idx, general, main_workers, marginal_workers )
        i += 3
        j += 1
    
    i = 0
    while ( i < len(maininfo) ):
        fill_my_lst( fields[j], maininfo[i], maininfo[i + 1], maininfo[i + 2], 'main_workers', sample_df, idx, general, main_workers, marginal_workers )
        i += 3
        j += 1

    i = 0
    while ( i < len(marginfo) ):
        fill_my_lst( fields[j], marginfo[i], marginfo[i + 1], marginfo[i + 2], 'marginal_workers', sample_df, idx, general, main_workers, marginal_workers )
        i += 3
        j += 1


    return template.render(general = general, main_workers = main_workers, marginal_workers = marginal_workers)


# print(render_demographics(1))