# Information Retrieval with Bernoulli Process

This Python script provides a simple GUI application for document retrieval using the Bernoulli Process, combining Jaccard Coefficient and Miller-Leek-Schwartz probability to rank documents based on their relevance to a user query.

## Dependencies
* Python 3.7 or higher
* re (regular expression library)
* math
* tkinter

## Usage
*	Download the script and the documents in the testcase files.
*	Run the script.
*	The GUI application will open.
*	Click the "Open Files" button to select and load one or more text files by navigating into the proper directory.
*	Type your query in the "Query" entry field.
*	Click the "Search" button to process the query and display ranked documents based on their relevance to the query.
*	The results will appear in the "Results" text box, with the document's score and content.
*	Click the "Clear Documents" button to remove all currently loaded documents.

## Functions
*	clean_text(text): Removes punctuation and special characters from a given text.
*	term_frequencies(doc): Returns the term frequencies of words in a given document.
*	miller_leek_schwartz_probability(q, d, freqs, total_freq): Calculates the Miller-Leek-Schwartz probability of a given query and document.
*	binary_vector(doc, vocab): Returns a binary vector representation of a document for a given vocabulary.
*	jaccard_coefficient(q_vec, d_vec, q, d): Computes the Jaccard Coefficient combined with the Miller-Leek-Schwartz probability for a given query and document.
*	search(query, documents): Searches for the query within the documents and ranks them based on their relevance.
*	open_files(): Opens a file dialog to select and load one or more text files.
*	process_query(): Processes the user query and displays the ranked documents.
*	clear_docs(): Clears the currently loaded documents.

## GUI Elements
*	Open Files button: Loads one or more text files.
*	Clear Documents button: Clears the loaded documents.
*	Query label: Displays the "Query:" text.
*	Query entry: Field to enter the user query.
*	Search button: Processes the user query and displays ranked documents.
*	Results label: Displays the "Results:" text.
*	Results text box: Displays the ranked documents and their scores.

## Troubleshooting
*	If the script doesn't run, make sure you have Python 3.7 or higher installed. Check your Python version by running python --version in the terminal or command prompt.
*	Ensure that the necessary libraries (re, math, and tkinter) are installed and available for your Python environment.
*	If you encounter issues while loading files, make sure the files are in the correct format (plain text) and accessible by the application.

## Future Developments
*	This project was done as an assignment in my university for the course Information Extraction and Retrieval and as a result was made without using a proper framework.
*	This project will soon be implemented using a different framework such as PyQt or Django.
