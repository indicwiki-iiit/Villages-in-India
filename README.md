# Generating Wikipedia Articles on 6,00,000+ Indian Villages in Telugu (Ongoing)

## Data Gathering
The data consists of 479 different attributes corresponding to
Indian Villages.  
Basic information w.r.t villages like the sub district, district, state it belongs to along with their codes and demographics is taken from Census India (2011).  
https://censusindia.gov.in/census.website/data/census-tables  

Village amenities information is taken from below:  
https://tn.data.gov.in/catalog/village-amenities-census-2011  

Data from both these sources has been merged (JOIN) based on ["State Code", "Sub District Code", "District Code", "Village Code"] values that are commonly found using pandas library in python.

```
# left join

mega_data = pd.merge(left = <main_data>, right = <add_data>, 
                   left_on = ['State', 'District', 'Subdistt', 'Town/Village'],
                   right_on = ['State Code', 'District Code', 'Sub District Code', 'Village Code'],
                   how = "left")
```
Duplicate rows and additional columns that are same in both sources have been dropped.

## Geocoding
There are two APIs that can be used to fetch geocodes of the villages.  
* ArcGIS Location Service  
https://developers.arcgis.com/documentation/mapping-apis-and-services/search/geocoding/  
Code for the same is available to ```./geocodes``` directory.

* Microsoft Azure Maps

## Finding Elevation

## Transliteration

## Translation

## Templating in Jinja2

## Rendering Templates

## Generating XML Dump

