# from jinja2 import Environment, FileSystemLoader
import pickle
from genXML import tewiki, write_to_page
from render_test_2 import get_wikitext
# import pandas as pd
# import numpy as np
# import sys
# sys.path.append('./templates')
from templates.render_infobox import render_infobox
from templates.render_intro import render_intro
from templates.render_village_info import render_village_info
from templates.render_governance import render_governance
from templates.render_public_welfare import render_public_welfare
from templates.render_in_village_edu import render_in_village_edu
from templates.render_in_village_hcare import render_in_village_hcare
from templates.render_in_village_trport import render_in_village_tport
from templates.render_paths import render_paths
from templates.render_water_facilities import render_water_facilities
from templates.render_demographics import render_demographics

with open('./major1.pkl', 'rb') as f:
    sample_df = pickle.load(f)

df_indices = list(sample_df.index)

current_page_id = 1500000

with open("village_test.xml", 'a', encoding = "utf-8") as fobj:
    fobj.write(tewiki + "\n")

    for idx in df_indices:
        infobox = render_infobox(sample_df, idx)
        intro = render_intro(sample_df, idx)
        village_info = render_village_info(sample_df, idx)
        governance = render_governance(sample_df, idx)
        public_welfare = render_public_welfare(sample_df, idx)

        in_village_edu = render_in_village_edu(sample_df, idx)
        out_village_edu = get_wikitext(sample_df, idx, "out_village_edu.j2")

        in_village_hcare = render_in_village_hcare(sample_df, idx)
        out_village_hcare = get_wikitext(sample_df, idx, "out_village_hcare.j2")

        in_village_tport = render_in_village_tport(sample_df, idx)
        paths = render_paths(sample_df, idx)
        water_facilities = render_water_facilities(sample_df, idx)
        demographics = render_demographics(sample_df, idx)
        
        part_2 = get_wikitext(sample_df, idx, 's9s_2.j2')

        title = sample_df.loc[idx, 'Name Telugu'] + " (" + sample_df.loc[idx, 'District Name Telugu'] + ", " + sample_df.loc[idx, 'State Name Telugu'] + ")"
        content = infobox + intro + village_info + governance + public_welfare + in_village_edu + out_village_edu + in_village_hcare + out_village_hcare + in_village_tport + paths + water_facilities + demographics + part_2 
        # content = part_2
        write_to_page(current_page_id, title, content, fobj)
        
        current_page_id += 1
        # with open("output.txt", "w", encoding = "utf-8") as f:
        #     f.write(content)
    fobj.write('</mediawiki>')

    # break

