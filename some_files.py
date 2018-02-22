import requests
link = requests.get(open('dataset_3378_3.txt').readline().strip()).text
while link[:2] != 'we':
    link2 = requests.get('http://stepic.org/media/attachments/course67/3.6.3/' + link)
    link = link2.text
link_latest = requests.get('http://stepic.org/media/attachments/course67/3.6.3/' + link)
print(link_latest.text)