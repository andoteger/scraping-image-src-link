from bs4 import BeautifulSoup
import requests
import re

url = "https://www.google.com/search?q=bird&safe=strict&rlz=1C1CHBF_enID842ID842&sxsrf=ALeKk01ncOMnpqFnxpf92NytEfmTzes0XA:1586260439046&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjH8vXPoNboAhUMeisKHRrACNEQ_AUoAXoECBgQAw&biw=1242&bih=632"

respon = requests.get(url)

page = BeautifulSoup(respon.text, "html.parser")

filter = page.find_all("img")

print(filter[3])
print("")
print(filter[3].get("src"))
print("")

i = []

for gambar in filter:
	print(gambar['src'])
