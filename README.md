=========================================================================================================
 Cewl
=========================================================================================================
To run the Cewl emmulator run the following commands
$ python3 cewl.py

then you will be prompted to fill in a couple options:

input link to site your trying to scrape: http://www.umass.edu/gateway/academics/schools-and-colleges
(here I have used the umass academics page as an example)

Go offsite? [yes/no] yes
(answer yes if you wish to visit links off the site and no if you wish to stay within same domain)

how deep do you wish to scrape? (enter a number recommended = 2): 2
(how deep do you wish to follow all the links on the page and scrape the pages in those links aswell)

minimum word length: 3
(words under this length will be thrown away and not saved as possible passwords)

enter name of output file followed by .txt: possible_passwords.txt
(pick a file location where the scraped words will be saved)

then you will see a loading status bar until the program is done scraping 

then you will get a return message:

all passwords with counts saved to file possible_passwords_counts.txt
all possible passwords saved to file possible_passwords.txt
all links visited saved to file all_links_visited.txt

(those files are where all the output is saved to)

=========================================================================================================
 John the Reaper + Crunch
=========================================================================================================
To run the John the Reaper emmulator run the following command
$ python3 John_the_reaper.py 

then you will be prompted to fill in a couple options:

input password to guess: cats
(if doing brute force method keep passwords guessed short to save time longer passwords will take longer)
(this only supports lm hash mode so passwords will not be case sensitive)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(Brute force mode)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pick attack mode dictionary or brute_force: brute_force
(in brute force mode the program will try all possible alphaneumeric permutations to guess password)

input min password length: 4
input max password length: 4
(telling program password is 4 characters long) 
(it can be between 4 chracters and a larger number if specified)

the password's hash is: 
6b7db1f9e51d69d0aad3b435b51404ee
(program will show user the lm hash of the password)

(after some time the program will return a found password here the password was "cats")
password is: 
cats
guessed in 94015 tries.
(guessed password is returned with number of attempts it took to find it)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(Brute force mode with Crunch)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pick attack mode dictionary or brute_force: brute_force
(in brute force mode the program will try all possible alphaneumeric permutations to guess password)

enter crunch mode [yes/no] (user input possible chracters) yes
(in crunch mode the user picks the chracters used in the possible password permutations)

input crunch string to permutate into password tac12
(only the chracters in this string are permutated and used to crack password)

input min password length: 3
input max password length: 4
(telling program password is at least 3 characters long) 
(this password can be between 3 and 4 chracters loading)

the password's hash is: 
bbc70d3c8f0049a5aad3b435b51404ee
(program will show user the lm hash of the password)

(after some time the program will return a found password here the password was "cat")
password is: 
cat
guessed in 56 tries.
(guessed password is returned with number of attempts it took to find it)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(Dictionary mode)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pick attack mode dictionary or brute_force: dictionary
(in dictionary mode the user specifies a dictionary .txt file for program to use as possible passwords)

enter file path to dictionary where list is contained: possible_passwords.txt
(here I am using the dictionary obtained from running Cewl and scraping umass amherst's academic page)

the password's hash is: 
e52cac67419a9a224a3b108f3fa6cb6d
(program will show user the lm hash of the password)

(after some time the program will return a found password here the password was "password")
password is: 
password
guessed in 1303 tries.
(guessed password is returned with number of attempts it took to find it)


