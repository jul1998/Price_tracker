import requests
import bs4 as bs
import smtplib

headers = {
    'Accept-Language': "xxxxx",
    'User-Agent':"xxxxxxxxxx"
}

res = requests.get(url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463",
                   headers=headers)
soup = bs.BeautifulSoup(res.text, 'html.parser')
price = int(float(soup.find(name="span", class_="a-offscreen").text.strip("$")))
print(price)


MY_GMAIL="YOUR EMAIL"
PASS="YOUR PASSWORD"

if price < 200:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(user=MY_GMAIL, password=PASS)
        subject = "Price is quite low!"
        body = f"The product you want is at ${price}. Buy it now!"
        msg = f"Subject: {subject}\n\n{body}"

        connection.sendmail(from_addr=MY_GMAIL,
                            to_addrs="address",
                            msg=msg)
else:
    print("Price is high yet")
