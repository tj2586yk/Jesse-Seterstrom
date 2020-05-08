import requests,PIL,docx
taco_url = 'https://raw.github.com/sinker/tacofancy/master/seasonings/sriracha_salt.md'
taco_recipe = requests.get(taco_url).json()

document = docx.Document()
document.add_paragraph('Taco Recipe!!,  Title')




document.save('taco_url.docx')


