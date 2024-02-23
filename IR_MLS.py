# These are the imported modules and functions needed for an information retrieval system 
# based on the Bernoulli process, including re for regular expression matching, math for 
# mathematical functions, defaultdict for a dictionary that automatically initializes 
# missing values, and Tk, Button, Label, Entry, filedialog, and Text from the tkinter 
# module for creating a graphical user interface.
import re
import math
import ctypes
import sys
from collections import defaultdict
from tkinter import Tk, Button, Label, Entry, filedialog, Text

# clean_text() is a function that uses the re module to remove all non-alphanumeric 
# characters (including punctuation and special characters) from a given text string.
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text)

icon_path = 'C:/Users/rayan/Downloads/ier.ico'
if hasattr(sys, '_MEIPASS'):
    # If the script is running from a PyInstaller executable
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(sys.executable)
else:
    # If the script is running as a regular Python script
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(icon_path)

# term_frequencies() is a function that takes in a document (text string) and returns
# a dictionary of term frequencies, where each key is a unique word in the document 
# and the corresponding value is the number of times that word appears in the document.
def term_frequencies(doc):
    words = clean_text(doc.lower()).split()
    freqs = defaultdict(int)
    for word in words:
        freqs[word] += 1
    return freqs


# miller_leek_schwartz_probability() is a function that implements the Miller-Leek-Schwartz 
# (MLS) probability measure for query likelihood in information retrieval. Given a query q, a 
# document length d, a dictionary of term frequencies freqs, and a total word count total_freq, 
# the function calculates the probability of observing the words in the query in a document of 
# length d using the MLS method.
def miller_leek_schwartz_probability(q, freqs, total_freq):
    words = set(clean_text(q.lower()).split())
    score = 0
    epsilon = 1e-10
    
    for word in words:
        fij = freqs[word]
        if fij > 0:
            p_ki_c = fij / total_freq
        else:
            Fi = sum(freqs.values())
            p_ki_c = Fi / total_freq
        
        p_ki_c = min(p_ki_c, 1 - epsilon)
        score += math.log(1 - p_ki_c) - math.log(p_ki_c)
    
    return -score


# binary_vector() is a function that takes in a document (text string) and a vocabulary 
# (a set of words) and returns a binary vector representation of the document using the given vocabulary.
def binary_vector(doc, vocab):
    words = set(clean_text(doc.lower()).split())
    return {word: 1 if word in words else 0 for word in vocab}


# jaccard_coefficient() is a function that calculates the Jaccard coefficient between 
# a query and a document, weighted by the Miller-Leek-Schwartz (MLS) probability measure for 
# query likelihood in information retrieval. Given a query vector q_vec, a document vector d_vec, 
# a query q, and a document d, the function first computes the Jaccard coefficient between the 
# binary vectors q_vec and d_vec, and then multiplies it by the absolute value of the MLS 
# probability measure for q and d.
def jaccard_coefficient(q_vec, d_vec, q, d):
    intersection = sum(1 for q_val, d_val in zip(q_vec.values(), d_vec.values()) if q_val == d_val == 1)
    union = sum(1 for q_val, d_val in zip(q_vec.values(), d_vec.values()) if q_val == 1 or d_val == 1)
    freqs = term_frequencies(d)
    total_freq = sum(freqs.values())
    probability = miller_leek_schwartz_probability(q, freqs, total_freq)
    positive_probability = abs(probability)
    return (intersection / union) * positive_probability if union != 0 else 0


# search() is a function that takes in a query (text string) and a list of documents (text strings), 
# and returns a list of search results, where each result is a tuple containing a document and its 
# score. The score is calculated using the Jaccard coefficient weighted by the Miller-Leek-Schwartz 
# (MLS) probability measure for query likelihood in information retrieval.
def search(query, documents):
    vocab = set()
    for doc in documents:
        vocab.update(clean_text(doc.lower()).split())
    query_vector = binary_vector(query, vocab)
    doc_vectors = [binary_vector(doc, vocab) for doc in documents]
    scores = [(doc, jaccard_coefficient(query_vector, doc_vector, query, doc)) for doc, doc_vector in zip(documents, doc_vectors)]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores


# open_files() is a function that uses the filedialog module to open one or more files selected by 
# the user through a GUI file dialog box. The contents of each file are read and added to a list called documents.
def open_files():
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            documents.append(content)


# process_query() is a function that processes a user query entered in a text entry widget called 
# query_entry, performs a search using the search() function, and displays the search results in a text widget called results.
def process_query():
    query = query_entry.get()
    results.delete(1.0, "end")
    ranked_docs = search(query, documents)
    for doc, score in ranked_docs:
        results.insert("end", f"Score: {score:.2f}\n{doc}\n\n")


# clear_docs() is a function that clears the contents of the documents list.
def clear_docs():
    documents.clear()

# Color palette used
backgroundColor = "#F5EFE7"
subBackgroundColor = "#D8C4B6"
textColor = "#213555"
# backgroundColor = "#FCE9F1"
# subBackgroundColor = "#F5EFE7"
# textColor = "#D8C4B6"


# Initialize the UI
# This is a script that creates a new top-level window object using the 
# Tk() function from the tkinter module, sets the title of the window to 
# "Information Retrieval with Bernoulli Process" using the title() method.
root = Tk()
root.title("Information Retrieval with Bernoulli Process")
root.config(bg=backgroundColor)


# This is a script that creates several UI components for an information 
# retrieval system based on the Bernoulli process using the Button(), Label(), 
# Entry(), and Text() functions from the tkinter module, and adds them to a 
# grid layout within the top-level window object.
open_button = Button(root, text="Open Files", command=open_files, bg=subBackgroundColor, fg=textColor)
open_button.grid(row=0, column=0, padx=10, pady=10)

clear_button = Button(root, text="Clear Documents", command=clear_docs, bg=subBackgroundColor, fg=textColor)
clear_button.grid(row=0, column=1, padx=10, pady=10)

query_label = Label(root, text="Query:", bg=subBackgroundColor, fg=textColor)
query_label.grid(row=1, column=0, sticky="W")

query_entry = Entry(root, bg=subBackgroundColor, fg=textColor)
query_entry.grid(row=1, column=1, padx=10, pady=10)

search_button = Button(root, text="Search", command=process_query, bg=subBackgroundColor, fg=textColor)
search_button.grid(row=2, column=0, columnspan=2)

results_label = Label(root, text="Results:", bg=subBackgroundColor, fg=textColor)
results_label.grid(row=3, column=0, sticky="W")

results = Text(root, wrap="word", bg=subBackgroundColor, fg=textColor)
results.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Global variables
documents = []
# Run the UI
root.mainloop()
