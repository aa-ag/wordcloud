###--- IMPORTS ---###
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import PyPDF2


###--- FUNCTIONS ---###
def extract_text_from_pdf():
    '''
     extracts text from pdf in path
    '''
    pdf_file = open('courtdecision.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    count = pdf_reader.numPages

    with open('courtdecision.txt', 'w+') as cd:
        for i in range(count):
            page = pdf_reader.getPage(i)
            cd.write(page.extractText())


def read_csv_and_create_wordcloud():
    '''
      opens csv as dataframe, reads thru it and creates string with text,
      ignoring 192 stopwords. Then creates wordcloud with that string.
    '''
    text = open('courtdecision.txt', 'r')

    text_string = ''

    for line in text:
        text_string += line

    sw = set(STOPWORDS)

    wc = WordCloud(width=800, height=800, background_color='white',
                   stopwords=sw, min_font_size=10).generate(text_string)

    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wc)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

    text.close()


###--- DRIVER CODE ---###
if __name__ == '__main__':
    read_csv_and_create_wordcloud()
    # extract_text_from_pdf()
