import datetime
from bulk import BulkScrapper
from prisma import Prisma, register
from flask import Flask, jsonify
from flask import Blueprint
from transformer import Transformer
from prisma.models import Bulkdeals, BulkDates


prisma = Prisma()
prisma.connect()
register(prisma)
app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    b = BulkScrapper()
    b.crawl("https://www.nseindia.com/report-detail/display-bulk-and-block-deals")
    data = b.run_scrapper()
    b.quit_driver()
    serialize = Transformer()
    entries = serialize.transform(data)
    bulk_date = serialize.get_bulk_date()
    Bulkdeals.prisma().create_many(entries)
    BulkDates.prisma().create({"date": bulk_date})
    return jsonify({
        "message": "bulk details inserted into db"
    })

@app.route("/bulk", methods=["GET"])
def get_bulk():
    stocks = Bulkdeals.prisma().find_many()
    return jsonify({
        "data": [stock.model_dump() for stock in stocks]
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)