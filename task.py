import requests
import getpass
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='Username to login on github')
    return parser.parse_args()
args = parse_args()
username = args.username
password = getpass.getpass(prompt='Enter Your Git pass: ', stream=None)

re = requests.get('https://api.github.com/user', auth=(username, password)).json()
print(re)

repos = requests.get('https://api.github.com/user/repos', auth=(username, password))
for repo in repos.json():
    if not repo['private']:
        print(repo['html_url'])

pulls = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
pullspr = requests.get(pulls, auth=(username, password)).json()
print(str(pullspr[13]['title']))


sor = ''
sor2 = ', '
print(pullspr)
for i in pullspr:
    sor = sor + str(i['user']['login']) + sor2
sor = sor.split(',')
print(set(sor))
li = []
for z in pullspr:
    if str(z['user']['login']) == 'Hrisanfov':
        print(str(z['url']))
        li.append(str(z['url']) + '/files')
#        print(requests.get(str(z['url']) + '/files').json())
for k in li:
    print(requests.get(str(k), auth=(username, password)).json()[0]['filename'])
