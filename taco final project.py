import requests,PIL,docx
taco_url = 'https://raw.github.com/sinker/tacofancy/master/seasonings/sriracha_salt.md'
taco_recipe = requests.get(taco_url).json()

document = docx.Document()
document.add_paragraph('Taco Recipe!!,  Title')

image = Image.open('photo-1582234372722-50d7ccc30ebd.jpg')
img_draw = ImageDraw.Draw(image)
taco final project.py:10
document.save('taco_url.docx')


