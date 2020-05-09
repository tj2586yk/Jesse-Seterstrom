import requests,PIL,docx
taco_url = 'https://raw.github.com/sinker/tacofancy/master/seasonings/sriracha_salt.md'
taco_recipe = requests.get(taco_url).json()

document = docx.Document()
document.add_paragraph('Taco Recipe', 'Title')


image = Image.open('photo-1562059390-a761a084768e.jpg')
image.save('photo-1562059390-a761a084768e.jpg')


document.save('Taco Recipe.docx')
