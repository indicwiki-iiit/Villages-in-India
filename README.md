# Generating Wikipedia Articles on 6,00,000+ Indian Villages in Telugu (Ongoing)

## 1. Data Gathering
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

## 2. Geocoding
There are two APIs that can be used to fetch geocodes of the villages.  
* ### ArcGIS Location Service  
https://developers.arcgis.com/documentation/mapping-apis-and-services/search/geocoding/  
Code for the same is available in ```./geocodes``` directory.

* ### Microsoft Azure Maps  
There may be more than one result and the result with the highest match confidence score should be chosen as the geocode for a given location.

## 3. Finding Elevation  
This can be done with either:  
* ### Elevation-api  
https://elevation-api.io/  
30 requests can be made per second (when making use of an API key) with a maximum batch size of 10 for a GET request.

* ### Open-elevation 
https://open-elevation.com/  
This API is a bit slower compared to the above mentioned one.

## 4. Transliteration

## 5. Translation

## 6. Templating in Jinja2

## 7. Rendering Templates

## 8. Generating XML Dump

## 9. Sample Article Link

