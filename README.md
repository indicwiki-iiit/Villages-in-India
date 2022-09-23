# Generating Wikipedia Articles on 6,00,000+ Indian Villages in Telugu

## 1. Data Gathering 📊
The data consists of 479 different attributes corresponding to
Indian Villages.  
Basic information w.r.t villages like the sub district, district, state it belongs to along with their codes and demographics is taken from Census India (2011).  
https://censusindia.gov.in/census.website/data/census-tables  

Village amenities information is taken from below:  
https://tn.data.gov.in/catalog/village-amenities-census-2011  

Data from both these sources has been merged (JOIN) based on ["State Code", "Sub District Code", "District Code", "Village Code"] values that are commonly found using pandas library in python.

```
# left join

mega_data = pd.merge(left = <main_data>, right = <amenities_data>, 
                   left_on = ['State', 'District', 'Subdistt', 'Town/Village'],
                   right_on = ['State Code', 'District Code', 'Sub District Code', 'Village Code'],
                   how = "left")
```
Duplicate rows and additional columns that are same in both sources have been dropped.  

* **NOTE :** The resultant data was very unclean. We have cleaned it manually and programmatically using concepts like regular expressions, etc..   

## 2. Geocoding 📍
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
Code for the same is available in ```./elevation``` directory.

* ### Open-elevation 
https://open-elevation.com/  
This API is a bit slower compared to the above mentioned one.  

## 4. Transliteration 
There are two options that can be used for transliteration.
* ### Google-transliteration-api  
https://pypi.org/project/google-transliteration-api/  
It is slower than Deeptranslit and does not support batches but with this trade-off comes a better accuracy than Deeptranslit. It powers the Google Input Tools.
```
pip install google-transliteration-api
```

* ### Deeptranslit  
https://pypi.org/project/deeptranslit/  
Deeptranslit is very fast and supports batches of data. It performs better for hindi transliterations than telugu. One can rely on it when the amount of data is huge but the number of unique words is low so that when manual check is done to verify the correctness of the library's transliterations, it won't be a hassle.  
```
pip install --upgrade deeptranslit

pip install tensorflow==1.15

pip install keras==2.2.4

pip install 'h5py==2.10.0' --force-reinstall
```
Find the code for both methods in ```./transliteration``` directory.

## 5. Translation
The translator we made use of is Microsoft Azure Cognitive Services Translator. It has a 2M character limit per API key.
https://portal.azure.com/#create/Microsoft.CognitiveServicesTextTranslation  

The code is in ```./translation``` directory.

## 6. Templating in Jinja2 🏯
Based on the article structure, we can create intelligent articles with jinja2 templates which upon rendering, give the article as we desire. The below code snipped shows how we can load the template.  
https://jinja.palletsprojects.com/en/3.1.x/

```
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('./')
env = Environment(loader = file_loader)
template = env.get_template('./templates/<template>')
```
All the templates are present in ```./templates``` directory.

## 7. Rendering Templates 🚀
While rendering the template, we pass the data required for the template as arguments to the render method. We can either pass data as multiple arguments as key value pairs or create a dictionary and pass as a single argument.

```
template.render(<data_to_be_passed_to_the_template>)
```

## 8. Generating XML Dump 
The output of the template is written to an XML file under ```<text></text>``` tags. To get an idea of how the XML file structure should be, open any wikipedia article, go to
ప్రత్యేక పేజీలు (Special pages) -> పేజీ పనిముట్లు (Page tools; at the bottom of the page) -> ఎగుమతి పేజీలు (Export pages).  

Few points to be noted while generating XML dump:  
* To get to know your username and userid, export a wikipedia page where you made the latest edit
* For choosing page id, take a large number (we have taken 1500000) so that it doesn't overlap and overwrite an arleady existing page

## 9. Sample Article Link 📄
https://tewiki.iiit.ac.in/index.php?title=%E0%B0%85%E0%B0%B0%E0%B1%8D%E0%B0%97%E0%B1%8B%E0%B0%B5%E0%B0%BE%E0%B0%B2%E0%B1%8D_(%E0%B0%B9%E0%B1%8B%E0%B0%B7%E0%B0%BF%E0%B0%AF%E0%B0%BE%E0%B0%B0%E0%B1%8D%E0%B0%AA%E0%B1%82%E0%B0%B0%E0%B1%8D,_%E0%B0%AA%E0%B0%82%E0%B0%9C%E0%B0%BE%E0%B0%AC%E0%B1%8D)

