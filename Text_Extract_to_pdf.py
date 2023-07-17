# import pdfplumber

# with pdfplumber.open("path/to/file.pdf") as pdf:
#     first_page = pdf.pages[0]
#     text = first_page.extract_text()
#     print(text)




#----------------------------------------- All Pages Text ----------------------------------->


# import pdfplumber

# with pdfplumber.open("Transformer.pdf") as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()
#         print()
#         print()

#         print(text)


#----------------------------------------- One Page Text ----------------------------------->


# import pdfplumber

# with pdfplumber.open('Transformer.pdf') as pdf:
#     page = pdf.pages[1]
#     text = page.extract_text()
#     print(text)

#----------------------------------------- Difficult Words ----------------------------------->

# import pdfplumber
# import nltk
# from nltk.corpus import words


# # do = nltk.download('words')
# # Load the set of English words
# word_set = set(words.words())

# with pdfplumber.open("Transformer.pdf") as pdf:
#     first_page = pdf.pages[0]
#     text = first_page.extract_text()
#     # Tokenize the text into words
#     tokens = nltk.word_tokenize(text)
#     # Identify difficult words
#     difficult_words = [word for word in tokens if word not in word_set]
#     print(difficult_words)

#----------------------------------------- Difficult Words 2 ----------------------------------->

'''
import pdfplumber

def get_difficult_words(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        words = []
        for page in pdf.pages:
            for word in page.extract_words():
                if word.is_difficult():
                    words.append(word)
    return words

if __name__ == "__main__":
    difficult_words = get_difficult_words("Transformer.pdf")
    print(difficult_words)
'''