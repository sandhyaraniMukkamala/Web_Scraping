from webbrowser import Chrome

from bs4 import BeautifulSoup as soup
from urllib.request import Request
from urllib.request import urlopen

#save the url
url = 'https://www.flipkart.com/search?q=iphone&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
req = Request(url, headers={'User-Agent': 'Chrome/67.0'})

#open the url
open_url = urlopen(req)
#get the html of the page
page_html = open_url.read()
#end the connection
open_url.close()
#parse the html
page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class:", "_3O0U0u"})
#print(len(containers))

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div", {"class:", "col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings = container.findAll("div", {"class:", "niH0FQ"})
#print(ratings[0].text)

filename = "iphone_data.csv"
f = open(filename,"w")

column_names = "Iphone_Type,Price,Rating"
f.write(column_names)

for container in containers:
    phone_Type = container.div.img["alt"]

    phone_Price = container.findAll("div", {"class:", "col col-5-12 _2o7WAb"})
    price = phone_Price[0].text.strip()

    phone_Rating = container.findAll("div", {"class:", "niH0FQ"})
    rating = phone_Rating[0].text

    trim_price = price.split(' ')
    #print(trim_price[0])
    rm_rupee = trim_price[0].split("₹")
    #print(rm_rupee[1])
    ex_price = rm_rupee[1].split('E')
    #print(ex_price[0])
    final_price = "Rs."+ ex_price[0]
    #print(final_price)

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(phone_Type.replace(",", "|")+","+final_price+","+final_rating+"\n")
    f.write(phone_Type.replace(",", "|")+","+final_price+","+final_rating+"\n")



