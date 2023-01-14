# Code that Intakes PDF, converts to text, and then inputs to OpenAI to Summarize

import openai
import os
import sys
import PyPDF2

# OpenAI API Key
openai.api_key = "YOUR_API_KEY"

# Loop that Checks Each pdf page using PyPDF2
loopcount = 0
pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

while loopcount < len(pdfReader.pages):
    # PDF File Path
    pdfFileObj = open('test.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pageObj = pdfReader.pages[loopcount]
    loopcount = loopcount + 1
    # PDF to Text
    text = pageObj.extract_text()
    # OpenAI Summarization
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Please Summarize the Following Text into a brief description: " + text,
        temperature=0.9,
        max_tokens=900,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    print(response["choices"][0]["text"])

