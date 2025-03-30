from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Το backend σου τρέχει!"

@app.route("/track", methods=["POST"])
def track_listings():
    data = request.get_json()
    url = data.get("url", "")

    if "spitogatos.gr" in url:
        return jsonify({
            "new_listing_found": True,
            "title": "Ενοικιάζεται γκαρσονιέρα στο κέντρο",
            "price": "650€",
            "link": "https://www.spitogatos.gr/aggelies/12345"
        })
    else:
        return jsonify({
            "new_listing_found": False,
            "message": "Δεν βρέθηκαν αγγελίες ή το URL δεν υποστηρίζεται ακόμα."
        })
