import pandas as p
from sklearn.neighbors import KNeighborsRegressor
import tkinter as tk
data = p.read_excel("dataset.xlsx")
data["credit_card_debt"] = p.to_numeric(data["credit_card_debt"], errors="coerce")
data["annual_salary"] = p.to_numeric(data["annual_salary"], errors="coerce")
data["net_worth"] = p.to_numeric(data["net_worth"], errors="coerce")
data["car_purchase_amount"] = p.to_numeric(data["car_purchase_amount"], errors="coerce")
X = data[["annual_salary", "credit_card_debt", "net_worth"]]
X.columns = ["annual_salary", "credit_card_debt", "net_worth"]
y = data["car_purchase_amount"]
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
pencere = tk.Tk()
pencere.geometry("400x200+300+300")
buton = tk.Button(pencere, text="Tıkla")
frame = tk.Frame(pencere)
textbox1 = tk.Entry(frame)
textbox2 = tk.Entry(frame)
textbox3 = tk.Entry(frame)
label1 = tk.Label(frame, text="Müşteri Yıllık Maaşı :")
label2 = tk.Label(frame, text="Müşteri Kredi Borcu :")
label3 = tk.Label(frame, text="Müşteri Net Değeri :")
label1.pack()
textbox1.pack()
label2.pack()
textbox2.pack()
label3.pack()
textbox3.pack()
frame.pack()
label = tk.Label(pencere, text="")
def butona_tiklandi():
    deger1 = textbox1.get()
    deger2 = textbox2.get()
    deger3 = textbox3.get()
    missing_data = [int(deger1), int(deger2), int(deger3)]
    predicted_value = model.predict([missing_data])
    label.config(text=f"Müşteri için tavsiye edilen harcama miktarı: {predicted_value}")
buton.config(command=butona_tiklandi)
buton.pack()
label.pack()
pencere.mainloop()