import requests
from bs4 import BeautifulSoup

text = requests.get("https://www.python.org/jobs").text
soup = BeautifulSoup(text, 'html.parser')

jobs = set()
for job in soup.body.section('h2'):
    jobs.add(f'{job.a.string} ({job.a["href"]})')

print('\n'.join(sorted(jobs, key=str.lower)))
