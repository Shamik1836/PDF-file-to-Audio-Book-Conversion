import pyttsx3
import PyPDF2

pdf_file = open('Cracking_the_Coding_Interview_6th_Editio.pdf', 'rb')

reading_pdf = PyPDF2.PdfFileReader(pdf_file)

pdf_pages = reading_pdf.numPages

pdf_speaker = pyttsx3.init()
voices = pdf_speaker.getProperty('voices')
pdf_speaker.setProperty('voice', voices[0].id)
page_chosen = reading_pdf.getPage(24)
pdf_text = page_chosen.extractText()
# pdf_speaker.say("Hi This is John here How may I help")
pdf_speaker.say(pdf_text)
pdf_speaker.runAndWait()
