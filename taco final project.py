import requests, docx,PIL


taco_url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'
response = requests.get(taco_url).json()

document = docx.Document()
document.add_heading('Taco Recipe', level=1)
def taco_data():
    response = requests.get(taco_url).json()
    seasoning = response['seasoning']

    condiment = response['condiment']
    mixin = response['mixin']
    base_layer = response['base_layer']
    shell = response['shell']
    print(seasoning)
    print(condiment)
    print(mixin)
    print(base_layer)
    print(shell)
    return seasoning,condiment,mixin,base_layer,shell


def taco_recipe_body():
    seasoning, condiment, mixin, base_layer, shell = taco_data()
    document.add_heading(f'{base_layer["name"]} with {mixin["name"]} with {shell["name"]} with {seasoning["name"]}')




document.add_picture('photo-1562059390-a761a084768e.jpg')



document.save('Taco Recipe.docx')
