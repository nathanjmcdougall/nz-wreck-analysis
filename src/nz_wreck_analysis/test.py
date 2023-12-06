"""Example."""
from urllib.request import urlopen

url = input("Enter a URL: ")

if not url.startswith(("http:", "https:")):
    msg = "URL must start with 'http:' or 'https:'"
    raise ValueError(msg)

with urlopen(url) as response:  # noqa: S310
    ...
