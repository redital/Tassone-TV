import os, json
from config import MEDIA_ROOT, STATE_PATH, CHANNELS_PATH

def get_all_local_episodes(channel_path):
    episodes = []
    full_path = os.path.join(MEDIA_ROOT, channel_path)
    for root, dirs, files in os.walk(full_path):
        for f in sorted(files):
            if f.endswith('.mp4'):
                rel_root = os.path.relpath(root)
                rel = "{}\\{}".format(rel_root,f)
                rel = rel.replace("\\","/")
                episodes.append(rel)
    return episodes

def get_next_local_episode(channel_name, channel_path, state):
    episodes = get_all_local_episodes(channel_path)
    last = state.get("local_channels", {}).get(channel_name, {}).get("last_played")
    try:
        idx = episodes.index(last)
        next_ep = episodes[(idx + 1) % len(episodes)]
    except ValueError:
        next_ep = episodes[0]
    if "local_channels" not in state:
        state["local_channels"] = {}
    state["local_channels"][channel_name] = {"last_played": next_ep}
    with open(STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2)
    return next_ep



def load_state():

    if not os.path.exists(STATE_PATH):
        with open(STATE_PATH, 'w') as f:
            print("NON HO TROVATO IL FILE IN {} E QUINDI LO CREO")
            json.dump({"current_channel": "rai_tg24", "local_channels": {}}, f)
    with open(STATE_PATH) as f:
        return json.load(f) 

def save_state(state):
    with open(STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def load_channels():
    with open(CHANNELS_PATH) as f:
        return json.load(f)