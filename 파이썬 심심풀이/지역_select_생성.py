import requests
from bs4 import BeautifulSoup as bs


req = requests.get('https://m.search.naver.com/search.naver?where=m&query=%EC%A0%84%EA%B5%AD+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&x_trv=Ml8wMF8wXw%3D%3D&sm=mtb_trv')
html = req.text
soup = bs(html, 'html.parser')

divs = soup.findAll('div' , {"class" : "map_marker"})

a= "충남"

for div in divs:
    
    links = div.find_all('a', {'href':True})
   
    for link in links:

        linkname = link.findAll('span' , {'class' : 'spot'})
        
        for yo in linkname:
            name_only = yo.text
                        
            if name_only == a:

                req2 = requests.get("https://m.search.naver.com"+link['href'])
                html2 = req2.text

                soup2 =bs(html2,'html.parser')

                attractions =soup2.findAll('span' , {'class' : 'spot'})

                namelist=[]
                for at in attractions:
                    name_only = at.text
                    namelist.append(name_only)
                
                namelist.sort()
                for i in namelist:
                    b="<option value="+'"'+i+'"'+">"+i+"</option>"
                    print(b)



    
