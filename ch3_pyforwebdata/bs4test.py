
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Test Page</title></head>
<body>
<p class="title"><b>Hello, BeautifulSoup!</b></p>
<p class="content">This is a test paragraph.</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print("Page title:", soup.title.string)
print("First paragraph:", soup.p.text)
