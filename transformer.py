from datetime import datetime

class Transformer:
    def __init__(self):
        self.__bulk_date = None
        self.entries = []

    def get_bulk_date(self):
        return self.__bulk_date

    def transform(self, data):
        for idx, entry in enumerate(data):

            if entry["DATE"] != "":
                if idx == 1:
                    self.__bulk_date = datetime.strptime(entry["DATE"], "%d-%b-%Y")
                self.entries.append({
                    "date": datetime.strptime(entry["DATE"], "%d-%b-%Y"),
                    "symbol": entry["SYMBOL"],
                    "security_name": entry["SECURITY NAME"],
                    "client_name": entry["CLIENT NAME"],
                    "trade_type": entry["BUY / SELL"],
                    "quantity_traded": int(entry["QUANTITY TRADED"].replace(",", "")),
                    "wt_price": float(entry["TRADE PRICE / WGHT. AVG. PRICE"].replace(",", "")),
                })
        return self.entries