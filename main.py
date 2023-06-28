from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request
from urllib.parse import urlparse

# convert SRT to text

app = Flask('API')


@app.route('/summarize', methods=['GET'])
def hello():
    args = request.args
    youtube_link = args.get('link')

    url_parse = urlparse(youtube_link)
    youtube_id = url_parse.query.split("=")[1]

    captions = srt = YouTubeTranscriptApi.get_transcript(youtube_id)

    final_text = ""

    for time_stamp in captions:
        final_text += time_stamp["text"]
        final_text += " "

    return {"Text": final_text, "Summary": "In Progress"}
