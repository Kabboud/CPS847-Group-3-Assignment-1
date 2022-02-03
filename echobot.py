import logging
from slack_bolt import App

app = App()


@app.event("app_mention")
def handle_app_mention_events(body, say):
    check = body['event']['text'][-1]
    user = body['event']['user']

    if check == "?":
        message = body['event']['text']
        say(f"Hi there, <@{user}>! You said the following:\n\"" + message + "\"")
    else:
        say(f"Hi there, <@{user}>! Did you mean to ask a question?")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.start(3000)
