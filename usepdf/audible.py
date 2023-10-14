from pypdf import PdfReader


import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

whatread = input("Enter the file name with location to audify: ")
reader = PdfReader(f"{whatread}")
print(len(reader.pages))

for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text().replace("\n", " ")
    speak.Speak(text)
