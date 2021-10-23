from fastapi import FastAPI
import textdistance


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


sygnatury = [
	("Przesylka posiada bledny adres twojej dostawy. Wiecej na stronie DPD. Nowa aplikacja czeka na ciebie abys mogl otrzymac kod odbioru.", "https://niebezpiecznik.pl/post/uwaga-na-zlosliwe-sms-w-sprawie-paczek/"),
	("Przesylka posiada bledny adres twojej dostawy. Wiecej na stronie DPD.", "https://niebezpiecznik.pl/post/uwaga-na-zlosliwe-sms-w-sprawie-paczek/"),
	("Poczta głosowa: Masz 1 nowa poczte glosowa. Przejdz do: http://persian-repair.com/cos-tam.php","https://niebezpiecznik.pl/post/uwaga-na-zlosliwe-sms-y-do-poczty-glosowej/"),
	("Masz do odebrania 800 zl z tarczy antykryzysowej. Aby odebrac wykonaj przelew potwierdzajacy tozsaomosc 1 PLN. Srodki otrzymasz w ciagu 24h. www.urzedy9[.]net/XXXX","https://niebezpiecznik.pl/post/uwaga-na-zlosliwe-sms-y-do-poczty-glosowej/"),
]

@app.get("/sms/{text}")
async def check_sms(sms):
	for syg, link in sygnatury:
		print(textdistance.hamming.normalized_similarity(syg, sms))
		if textdistance.hamming.normalized_similarity(syg, sms) >= 0.25:
			return {"sms": sms, "status": "FRAUD", "link": link}
	return {"sms": sms, "status": "OK", "link":""}
