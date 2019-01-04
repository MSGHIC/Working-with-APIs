# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:54:23 2018

@author: MSG
"""

"""Now we’ll begin to write a program to issue an API call and process the
results by identifying the most starred Python projects on GitHub:"""
#python_repos on github
import requests
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
#Status code tells us whether the request was successful. 
#(A status code of 200 indicates a successful response.)
print("Status code:", r.status_code)

# Store API response in a variable(disctionary)
response_dict = r.json()
# Process results.
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])
# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
  #  print(key)
   
    
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])    
    
#plot repo facts found
#lets visualize the results
    
#store name of each repo ,url and its corresponding stars
repo_name = []
url = []
repo_plot_dicts = []

for repo_dict in repo_dicts :
   repo_name.append(repo_dict['name'])
   # repo_stars.append(repo_dict['stargazers_count'])
   repo_plot_dict = {
                        'value': repo_dict['stargazers_count'],
                        'label': str(repo_dict['description']), 
                        'xlink': repo_dict['html_url'],
                    }
   repo_plot_dicts.append(repo_plot_dict)
    
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#make visualisation
my_style = LS('#337365', base_style=LCS)

#creating a configuration object that contains all of our customizations to pass to Bar():
my_config = pygal.Config()

my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

hist = pygal.Bar(my_config, style=my_style)
hist.title = "GitHub's Popular Python Repos;26/08/18"
hist.x_labels = repo_name
hist.x_title = "Repository Name"
hist.y_title = "Stars"
hist.add(' ', repo_plot_dicts)
hist.render_to_file("GitHub's Python Popular Repos.svg")

