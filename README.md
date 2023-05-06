# OpenBudget
O'rnatish ketma ketligi quyidagicha
1-qadam: `git clone https://github.com/usarvi/OpenBudget.git`
agar git yo'q bo'lsa `sudo apt install git`
yana qayta `git clone https://github.com/usarvi/OpenBudget.git` ni kiritamiz
2-qadam: `cd OpenBudget`
3-qadam: `pip install -r requirements.txt` yoki `pip3 install -r requirements.txt`; pip yo'q desa uni ham o'rnatamiz
`sudo apt-get install python3-pip` qilib serverga pythonni o'rnatamiz. Undan so'ng qayta yana zarur requirements.txt ni olamiz
4-qadam: `.env` fayl yasaymizda ichiga `nano .env` deb kirib `TOKEN=token_api` kiritib saqlab qo'yamiz
dasturimiz qanday ishlayotganini ko'rish uchun `sudo apt install screen` qilib o'zimizga o'rnatib olamiz. Keyin sessiyani ko'rish uchun `screen-S OpenBudget` ni yozamiz

Oxirgi qadam `python openbudget.py` yoki `python3 openbudget.py` ni kiritib ko'ramiz
