from bs4 import BeautifulSoup
import requests
import pytz
import os
from datetime import datetime
import json

#Arrays to store the name,image,and price data
Gname = []
Gimage =[]
Gprice =[]
Glink =[]
#Making the start of the webscarping with BeatifuleSoup
def getdata(url): 
    r = requests.get(url) 
    return r.text 
website_url = 'https://www.gundamplanet.com/catalogsearch/result/index/show_in/293/mst_stock/2/?mst_stock=2&q=gundam'
html_text = getdata(website_url)
soup = BeautifulSoup(html_text, 'lxml')

#Making a funcation to Write a file, and get the name, image, and price
def GundamLookOut():
    data=[]
    #Get the date
    Myzone = pytz.timezone("US/Central") 
    DateForMe = datetime.now(Myzone)
    Date = DateForMe.now().strftime("%Y-%m-%d %S")
    
      
    #Make the GundamList.txt in subfolder 
    folder_path = 'Gundam-Look-Out'
    filepath_json = os.path.join(folder_path, "Gundamlist.json")
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    #Opne the txt file 
    GundamList = open(filepath_json, 'w', encoding='utf-8')
    
    with open(filepath_json, "w") as outfile:
        outfile.write(f'"Date": "{Date}",\n')
        
    data = {
    "website": website_url,
    "Date": Date,
    "items": []
    }
    
    #Gets the name of the Gundam Modle
    for Gunum in soup.find_all('a', class_='product-item-link'):
                name = Gunum.string
                if name not in Gname:
                    Gname.append(name)
                    
    #Gets the image of the Gundam Modle
    for Gunage in soup.find_all('div', class_='product-item-info'):
        leftlabel = Gunage.find('div', class_='leftlabel')
        if leftlabel:
            image_url = leftlabel.find_next('img', class_='product-image-photo')['src']
            Gimage.append(image_url)
            for a_tag in Gunage.find_all('a'):
                link = Gunage
                link_url = a_tag['href']
                if link_url != "javascript:void(0);" :
                    if "#reviews" not in link_url:
                        if link_url not in Glink:
                            Glink.append(link_url)
                            
           
    #Gets the price of the Gundam Modle
    for Gunice in soup.find_all('span', class_ ='price'):
                Gprice.append(Gunice.text)
    
    #Writes in the txt file the data it collected            
    for image,name,price,link in zip(Gimage,Gname,Gprice,Glink):
        name = name.replace("\n", "").strip()
        item = {
            "image": image,
            "name": name,
            "price": price,
            'link': link
        }
        data["items"].append(item)
        json_data = json.dumps(data,indent=4)
        with open(filepath_json, "w") as outfile:
            outfile.write(json_data)

    GundamList.close()
    
#Runs the function
GundamLookOut()



