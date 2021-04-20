import requests
from bs4 import BeautifulSoup
import pandas
import  argparse
import connect

scattering_list = []
parser = argparse.ArgumentParser()
parser.add_argument("--page_max",type=int,help='Maximum number to take')
parser.add_argument("--dbname",help="database name")
agrs = parser.parse_args()
connect.connect(agrs.dbname)
page_max = agrs.page_max


for i in range(1, page_max):
    url = "https://www.oyorooms.com/hotels-in-bangalore/"+"?page="+str(i)
    print("Getting request for "+ url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}
    req = requests.get(url, headers=headers)

    response = req.status_code
    content = req.content
    soup = BeautifulSoup(content, "html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    for hotel in all_hotels:
        dicto = {}
        dicto["hotel_name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        dicto["hotel_address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        dicto["hotel_price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text
        try:
            dicto["hotel_rate"] = hotel.find("span", {"class" : "hotelRating__ratingSummary"}).text

        except:
            dicto["hotel_rate"] = None

        hotel_list = []
        hotel_ammenties = hotel.find("div", {"class": "amenityWrapper"})
        try:
            for hotel in hotel_ammenties.find_all("div", {"class": "amenityWrapper__amenity"}):

                hotel_list.append(hotel.find("span", {"class": "d-body-sm"}).text)
                dicto["hotel_list"] = ','.join(hotel_list[:-1])
                scattering_list.append(dicto)
                connect.insert_into_values(agrs.dbname,tuple(dicto.values()))
               # print(hotel_name, hotel_address, hotel_price, hotel_rate, hotel_list)
        except:
            pass

dataframe = pandas.DataFrame(scattering_list)
print("creating csv file....")
dataframe.to_csv("oyo.csv")
connect.get_all_values(agrs.dbname)
