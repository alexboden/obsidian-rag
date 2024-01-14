import os, sys
import cohere

# USER INPUTS
COHERE_API_KEY = ''
OBSIDIAN_VAULT_PATH = 'notes'

# CODE
co = cohere.Client(COHERE_API_KEY)

# helper
def read_txt_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Check if the user has provided an input argument
if len(sys.argv) < 2:
    print("Usage: python script.py <your_question>")
    sys.exit(1)

user_question = sys.argv[1]

# Create a list of documents from the Obsidian vault
documents = []
for dirpath, dirnames, filenames in os.walk(OBSIDIAN_VAULT_PATH):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(dirpath, filename)
            documents.append({
                "title": filename,
                "snippet": read_txt_file(file_path)
            })

# Take the first command line argument as the prompt when running the script
# prompt = 
response = co.chat(
    model="command",
    prompt_truncation='AUTO',
    message=user_question,
    documents=documents
)

# Extract the top source document for the response
top_source = response.documents[0] if response.documents else None
top_source_title = top_source['title'] if top_source else 'No source available'
top_source_snippet = top_source['snippet'] if top_source else 'No snippet available'

# User-friendly display of the response and source document
print(f"{response.text}\nTop Source: '{top_source_title}', {os.path.join(OBSIDIAN_VAULT_PATH, top_source_title)}")
