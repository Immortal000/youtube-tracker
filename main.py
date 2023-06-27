from youtube_transcript_api import YouTubeTranscriptApi

captions = YouTubeTranscriptApi.get_transcript("XjV4HYZTJB8")
# convert SRT to text

final_text = ""

for time_stamp in captions:
    final_text += time_stamp["text"]
    final_text += " "
