from flask import Flask, render_template, request
from main import İnstagramVideoDownloader


app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        __input = request.form.get("videoId")
        cl_ = İnstagramVideoDownloader(url=__input)
        cl_.Downloader()
        request.close
        return render_template("index.html", inputId=__input)
        
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
    
    