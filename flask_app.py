from flask import Flask, render_template, request, jsonify, redirect
from utils import *
from config import *

app = Flask(__name__, **flask_app_init)

app.config.from_object(Config)


@app.route("/diretta")
def diretta():
    state = load_state()
    channels = load_channels()
    current = state.get("current_channel")
    ch = channels.get(current)

    if not ch:
        return "Canale non trovato", 404

    if ch["type"] == "local":
        ep_path = get_next_local_episode(current, ch["path"], state)
        video_src = ep_path
    else:
        video_src = ch["url"]

    return render_template("player.html", video_src=video_src)

@app.route("/change_channel")
def change_channel():
    name = request.args.get("name")
    channels = load_channels()
    if name not in channels:
        return "Canale non disponibile", 400
    state = load_state()
    state["current_channel"] = name
    save_state(state)
    #return redirect(url_for("diretta"))
    return redirect("http://{}.local".format(DASHBOARD_HOSTNAME))

@app.route("/api/status")
def status():
    state = load_state()
    return jsonify(state)

@app.route("/api/next", methods=["POST"])
def next_episode():
    state = load_state()
    channels = load_channels()
    current = state.get("current_channel")
    ch = channels.get(current)
    ep_path = get_next_local_episode(current, ch["path"], state)
    return jsonify({"video_src": f"/{ep_path}"})

if __name__ == "__main__":
    app.run(**flask_app_config)