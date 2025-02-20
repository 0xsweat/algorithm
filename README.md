# Algorithm

This Python script allows you to check the availability of usernames on a variety of sites

<h2> Multiple sites per list </h2>
<p>SITE EXAMPLES: Github, Repl, Instagram, Twitter, Codechef.</p>

## Usage
Clone the repository (or download the script):

- git clone https://github.com/0xsweat/algorithm
- cd algorithm
- python3 algorithm.py usersFile

<h3> Create a text file containing the usernames you want to check. Each username should be on a new line.</h3>

Run the script:

- python3 algorithm.py usersFile

## Editing the site list

To add a site you can use

- python3 siteEditor.py add name url minimumUsernameLength maximumUsernameLength
- python3 siteEditor.py add name url

To remove a site from the list you can use

- python3 siteEditor.py remove name
