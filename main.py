

import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('story.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()

#deprecation related issue have been fixed -- functionality is a bit weird,
#the output mp3 only have 1 line of the pdf transcribed from there