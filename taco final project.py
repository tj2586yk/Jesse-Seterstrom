# request document from word pil is to import picture.

import requests,docx,PIL

# web site for the taco recipe.
taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
# json file request for web site.
response = requests.get(taco_url).json()
# document for  word to enter data.
document = docx.Document()
# this is the header for the top of page.
document.add_paragraph('                       Random Taco Recipe','Title')
# This is the taco picture.

document.add_picture('ryan-concepcion-50KffXbjIOg-unsplash.jpg')
# Picture by Ryan Concepcion.
def taco_data():
# define the taco data.
    response = requests.get(taco_url).json()
# Request the 5 items from the recipe.
    seasoning = response['seasoning']
# response for seasoning.
    condiment = response['condiment']
# response for condiment.
    mixin = response['mixin']
# response for mixin.
    base_layer = response['base_layer']
# response for base layer.
    shell = response['shell']
# response for shell.
    print(seasoning)
# print seasoning line from file.
    print(condiment)
# print condiment line file.
    print(mixin)
# print mixin line from file.
    print(base_layer)
# print base layer from line file.
    print(shell)
# print shell from line file.
    return seasoning,condiment,mixin,base_layer,shell
# Return all from recipe data.

def taco_recipe_body():
# Define a new string.
    seasoning, condiment, mixin, base_layer, shell = taco_data()
# pull every this from taco data.
    document.add_heading(f'{base_layer["name"]} with {mixin["name"]} with {shell["name"]} with {seasoning["name"]}')
# Lined up all dictionary with names for ingredients.
    document.add_paragraph(base_layer['recipe'])
# calling out base layer recipe ingredients.
    document.add_paragraph(seasoning['recipe'])
# calling out seasoning recipe ingredients.
    document.add_paragraph(condiment['recipe'])
# calling out condiments ingredients.
    document.add_paragraph(mixin['recipe'])
# calling out mixin recipe ingredients.
    document.add_paragraph(shell['recipe'])
# calling out the shell ingredients.
taco_recipe_body()
# call out each taco name.
taco_recipe_body()
# call out each taco name
taco_recipe_body()
# call out each taco name.

# save taco recipe to a word document.
document.save('Taco Recipe.docx')
