from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    override = request.args.get('luck_override')
    
    if override == 'true':
        html = """
        <!DOCTYPE html>
        <html>
          <body style="font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', sans-serif; background-color: #fcf9f2; color: #5c4a72; padding: 50px;">
            <div style="border: 4px dashed #ffb3ba; border-radius: 15px; padding: 30px; background-color: #fff0f5; box-shadow: 0 0 15px rgba(255, 179, 186, 0.5);">
                <h1 style="color: #ff9aa2;">🌸 OVERRIDE ACCEPTED 🌸</h1>
                <p>Spring Incident Response Team API call received. Processing request...</p>
                <p style="color: #2e8b57; font-weight: bold;">[LEPRECHAUN INTERCEPT] I'm checking the headers before I let you through.</p>
            </div>
          </body>
        </html>
        """
        response = make_response(render_template_string(html))
        response.headers['X-Luck-Override-Token'] = 'WICYS{h34d3r_h1dd3n_lck_byp4ss}'
        return response
        
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Bunny Network API</title>
        <style>
          body { font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', sans-serif; background-color: #fcf9f2; color: #5c4a72; margin: 0; padding: 50px; }
          .container { width: 80%; margin: 0 auto; border: 4px dashed #bae1ff; border-radius: 20px; background-color: #f0f8ff; padding: 40px; box-shadow: 0 0 20px rgba(186, 225, 255, 0.5); }
          header { border-bottom: 4px dotted #ffdfba; padding-bottom: 15px; margin-bottom: 25px; color: #ffb3ba; text-align: center; }
          h1 { margin: 0; font-size: 2.5em; text-shadow: 2px 2px 0px #fff; }
          .terminal-text { text-align: left; display: inline-block; background: #fffaf0; padding: 25px; border: 2px solid #baffc9; border-radius: 10px; margin-top: 20px; width: 100%; box-sizing: border-box; font-family: 'Courier New', monospace; font-size: 1.1em; color: #2e8b57; }
          .error-msg { color: #ff9aa2; font-weight: bold; }
        </style>
      </head>
      <body>
        <div class="container">
          <header>
            <h1>🐰 Bunny Network - API Endpoint V1 🐰</h1>
          </header>
          <div style="text-align: center;">
            <p style="font-size: 1.2em;">Basket Routing & Egg Schedule Synchronization Service</p>
          </div>
          <div class="terminal-text">
            > Service Status: <span style="color: #ff9aa2; font-weight: bold;">HIJACKED</span><br>
            > Luck Engine Interference: 100%<br>
            > Awaiting Spring Incident Response configuration override...<br>
            > <span class="error-msg">ERROR: Missing required GET parameter. Access to Easter Prep routing denied.</span><br>
            > <span style="color: #5c4a72;">[HEAP MACCIPHER NOTE] Nice try, bunnies. The API documentation is hidden where you can't see it.</span>
          </div>
          <!-- Internal Dev Note: To perform a manual override and bypass the Luck Engine, you must pass the 'luck_override' parameter in the URL and set it to 'true'. Note: The confirmation token is returned out-of-band in the response headers to prevent Leprechaun interception. -->
        </div>
      </body>
    </html>
    """
    
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
