import docx

# Creating a Word document object
document = docx.Document("file.docx")

# Create an empty string to store the document's text
docu = ""

# Loop through each paragraph in the Word document and append the text
for para in document.paragraphs:
    docu += para.text + "\n"  # Adding a newline character for readability

# Print the output
print(docu)
