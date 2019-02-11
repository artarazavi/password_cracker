# ==========================================================================================
# Crated by Seyedeh Arta Razavi
# For class CS590A

import urllib.request as urllib2
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from collections import Counter
import re
import operator
import time
import sys

# ==========================================================================================
# Functions


def remove_min(lst, min):
    new_lst = []
    for l in lst:
        if len(l) >= 3:
            new_lst.append(l)
    return new_lst


def scrape(site_url, offsite, min_length):
    parsed_uri = urlparse(site_url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    # download html from site
    f = urllib2.urlopen(site_url)
    html = f.read()
    f.close()
    soup = BeautifulSoup(html, 'html.parser')
    # these are the html tags I have chosen to scrape from each site
    tags = ['p', 'a', 'h1', 'h2', 'h3', 'ul', 'ol', 'span', 'title', 'table']
    possible_passwords = []
    possible_links = []
    for tag in tags:
        # get http links from site
        if tag == 'a':
            tag_extracted = soup.find_all('a', href=True)
            regex = re.compile('^http')
            for t in tag_extracted:
                # these are links that do not go offsite
                if regex.match(t['href']) is None:
                    link = t['href']
                    pattern1 = re.compile("^\.\.")
                    pattern2 = re.compile("^//")
                    if (pattern1.match(link) == None) and (pattern2.match(link) == None):
                        possible_links.append(domain+link)
                # if user decides to go offsite gather offsite links
                if offsite == 'yes':
                    if regex.match(t['href']) is not None:
                        possible_links.append(t['href'])

        tag_extracted = soup.find_all(tag)
        length = len(tag_extracted)
        all_tags = []
        for i in range(0, length):
            # strip all non-word new-line and other extra characters
            alphanu_strip = re.sub(
                r'\W+', ' ', tag_extracted[i].get_text().strip('\n'))
            splitted = alphanu_strip.lower().split()
            # remove words that are under the minimum word length
            min_removed = remove_min(splitted, min_length)
            all_tags = all_tags+min_removed
        possible_passwords = possible_passwords + all_tags

    return (possible_links, possible_passwords)


def remove_pdf(links):
    new_links = []
    for l in links:
        if ".pdf" not in l:
            new_links.append(l)
    return new_links


def remove_dup(all_links, links):
    new_links = []
    for link in links:
        if link not in all_links:
            new_links.append(link)
    return new_links

# ==========================================================================================
# Main method


# gather options from user input
site_url = input("input link to site your trying to scrape: ")
offsite = input("Go offsite? [yes/no] ")
depth = input(
    "how deep do you wish to scrape? (enter a number recommended = 2): ")
min_length = input("minimum word length: ")
output_file = input("enter name of output file followed by .txt: ")

all_links = []
possible_links = []
possible_passwords = []
possible_links.append(site_url)
all_links.append(site_url)

# loading animation used
animation1 = "♡★♥☆"
animation2 = "|/-\\"
animation3 = "☠☢☹♘⚔⚰⚠☣"
i = 0

# go in links depth, depth specified by user
for x in range(int(depth)):
    temp_links = []
    for link in possible_links:
        # this start of code for a loading graphic
        i = i + 1
        time.sleep(0.1)
        sys.stdout.write("\r" + "Loading " +
                         animation3[i % len(animation3)] + " ")
        sys.stdout.flush()
        # end loading graphic
        try:
            new_links, new_pass = scrape(link, offsite, min_length)
            # do not visit links which are pdfs
            new_links = remove_pdf(new_links)
            # do not visit linked you have visited before
            new_links = remove_dup(all_links, new_links)
            temp_links = temp_links + new_links
            all_links = all_links + new_links
            # store all possible passswords gathered at link
            possible_passwords = possible_passwords + new_pass
        except Exception:
            pass
    possible_links = temp_links


# count occurances of all possible passwords store in tuples (password, count)
counts = Counter(possible_passwords)
counts_tuples = sorted(
    counts.items(), key=lambda kv: kv[1], reverse=True)

# write passwordword count tuples to file count (tab) word
filename = 'possible_passwords_counts.txt'
with open(filename, mode="w") as outfile:
    outfile.write('\n'.join('{} \t {}'.format(
        x[1], x[0]) for x in counts_tuples))

# write all possible passwords to seperate file 1 word per line
filename3 = output_file
with open(filename3, mode="w") as outfile3:
    outfile3.write('\n'.join('{}'.format(
        x[0]) for x in counts_tuples))

# store all links visited during scrape to file 1 link per line
filename2 = 'all_links_visited.txt'
with open(filename2, mode="w") as outfile2:
    for x in all_links:
        outfile2.write("%s\n" % x)

print("\nall passwords with counts saved to file possible_passwords_counts.txt")
print("all possible passwords saved to file " + output_file)
print("all links visited saved to file all_links_visited.txt")
