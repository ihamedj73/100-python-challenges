"""
Track a product price in Amazon website
"""
from email.mime.text import MIMEText
import smtplib
import requests
from bs4 import BeautifulSoup


my_email = "yourEmail"
password = "YourPassword"


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}
clone_url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.com/Instant-Pot-Electric-Multi-Cooker-Pressure/dp/B0B4PQDFCL/ref=pd_ci_mcx_di_int_sccai_cn_d_sccl_1_2/141-4913447-7127328?pd_rd_w=DQWpm&content-id=amzn1.sym.751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_p=751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_r=H5MJ516ZJMJ8NH3ZZ51J&pd_rd_wg=FAt7v&pd_rd_r=529b66a2-7b78-4a4e-afc4-c7ca415939e2&pd_rd_i=B0B4PQDFCL&th=1"
res = requests.get(url, headers=header)

res.raise_for_status()
html_text = res.text
soup = BeautifulSoup(html_text, "html.parser")
title = soup.select_one("#title").text.strip()
price = float(soup.find(class_="a-offscreen").get_text().split("$")[1])


BUY_PRICE = 150

if price < BUY_PRICE:
    mime_message = MIMEText(
        f"{title}\nnow {price}\n{clone_url}", "plain", "utf-8")
    mime_message["From"] = my_email
    mime_message["To"] = my_email
    mime_message["Subject"] = "Amazon Price alert"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=mime_message.as_string()
        )
