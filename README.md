# Obsidian RAG

This Python script utilizes the Cohere API to answer questions by referencing documents stored in an Obsidian Vault. It's designed to search through all markdown files in the vault, to find relevant information in response to user queries.

## Prerequisites
- Cohere API Key: Sign up at [Cohere](https://cohere.ai/) to get an API key.
- An Obsidian Vault with `.md` files.

## Example

Using the "./notes" directory as an Obsidian Vault, you can leverage the RAG to find answers in the vault.
```bash
python main.py "Who is Alex Boden"
```
Output:
```
Alex Boden is a third-year computer science student at the University of Waterloo. 

Would you like to know more about the University of Waterloo?
Top Source: 'About Alex.md', notes/About Alex.md
```