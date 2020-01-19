import requests
from bs4 import BeautifulSoup as bs


req = requests.get('https://m.search.naver.com/search.naver?where=m&query=%EC%A0%84%EA%B5%AD+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&x_trv=Ml8wMF8wXw%3D%3D&sm=mtb_trv')
html = req.text
soup = bs(html, 'html.parser')

divs = soup.findAll('div' , {"class" : "map_marker"})

a= "서울"
# django에서 get으로 받는값



for div in divs:
    
    links = div.find_all('a', {'href':True})
    # [<a class="circle providence" href="/search.naver?where=m&amp;query=%EC%9A%B8%EC%82%B0+%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&amp;x_trv=Ml8xMF8wXw%3D%3D&amp;sm=mtb_trv" onclick="return goOtherCR(this, 'a=trv.mapclick&amp;r=&amp;i=&amp;u='+urlencode(urlexpand(this.href)));"> <span class="center"> 
    # <span class="spot">울산</span> <span class="num">305</span> </span> </a>]
    
    for link in links:

        linkname = link.findAll('span' , {'class' : 'spot'})
        # [<span class="spot">울산</span>]
        for yo in linkname:
            name_only = yo.text
            # 울산
            
            if name_only == a:

                
                req2 = requests.get("https://m.search.naver.com"+link['href'])
                html2 = req2.text

                soup2 =bs(html2,'html.parser')

                attraction_img = soup2.find_all('img' , {'class' : 'bg_nimg'})
                for at_img in attraction_img:
                    print(at_img.get('src'))

                # attractions =soup2.findAll('div' , {'class' : 'info'})
                # for attraction in attractions:
                #     at = attraction.find_all('strong' ,{'class' : 'tit'})
                    
                    
                #     for hi in at:
                #         hello = hi.text
                #         print(hello)

