from flask import Flask, request, render_template
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None

    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            return render_template("index.html", error="URL is required")

        
        img = qrcode.make(url)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return render_template("index.html", qr_data=img_base64)

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)