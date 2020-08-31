filename = "raw.pdf"

import textract

text = textract.process(filename)

output = open("output.txt", 'w')
text = str(text, 'utf-8')
output.write(text)
output.close()
