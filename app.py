import requests
from flask import Flask, Response
import xml.etree.ElementTree as ET
from expiringdict import ExpiringDict

app = Flask(__name__)
cache = ExpiringDict(max_len=100, max_age_seconds=3600)

FEED_URL = "https://www.biblegateway.com/votd/get/?format=json"


def fetch_and_convert():
    if "votd" not in cache:
        content = requests.get(FEED_URL).json()
        cache["votd"] = content
    else:
        content = cache["votd"]

    items_xml = f"""
    <item>
      <title>{content['votd']['reference']}</title>
      <link>{content['votd']['permalink']}</link>
      <description>Verse of the Day

      {content['votd']['text']}

      {content['votd']['reference']}
      </description>
    </item>"""

    # Build RSS 2.0 feed
    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Bible Gateway Verse of the Day</title>
    <link>https://biblegateway.com</link>
    <description>Bible Gateway Verse of the Day</description>
    {items_xml}
  </channel>
</rss>"""

    return rss_xml


@app.route("/")
def rss_feed():
    """Serve the RSS feed."""
    rss_content = fetch_and_convert()
    return Response(
        rss_content,
        mimetype="application/rss+xml",
        headers={
            "Cache-Control": "public, max-age=3600",
            "Access-Control-Allow-Origin": "*"
        }
    )


@app.route("/health")
def health():
    """Health check endpoint."""
    return "OK"


if __name__ == "__main__":
    # Run on all interfaces, port 8080, HTTP only
    app.run(host="0.0.0.0", port=8080, debug=False)
