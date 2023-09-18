import requests
timesp = requests.get("https://api.aladhan.com/v1/timingsByCity/18-09-2023?city=Jizan&country=Saudi+Arabia&method=4")
fullt = timesp.json()
times = fullt["data"]["timings"]

fajr ,fajrEnd ,duhr ,asr ,mag ,isha ,ishaEnd = times["Fajr"] , times["Sunrise"] ,times["Dhuhr"] ,times["Asr"] , times["Maghrib"] , times["Isha"] , times["Midnight"]

print("fajr starts at :  ",fajr ,"\n fahr ends at :  ", fajrEnd ,"\n duhr starts at :  ", duhr ,"\n asr starts at :  ", asr ,"\n magrib starts at :  ", mag ,"\n isha starts at :  ", isha ,"\n isha ends at : " ,ishaEnd)