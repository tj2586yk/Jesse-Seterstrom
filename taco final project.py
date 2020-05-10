import requests, docx,PIL


taco_url = 'https://api.taco-1150.herokuapp.com/random/?full_taco=true'
response = requests.get(taco_url).json()

document = docx.Document()
document.add_heading('Taco Recipe', 'Title')




document.add_picture('photo-1562059390-a761a084768e.jpg')



document.save('Taco Recipe.docx')
