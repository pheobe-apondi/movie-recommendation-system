from chromadb.config import Settings
import chromadb
from typing import List, Dict, Any
import os
import logging

# Import new Google GenAI SDK client
from google import genai

# Configure Gemini API client
client = genai.Client()

# Use PersistentClient pointing to your persisted embedding storage
chroma_client = chromadb.PersistentClient(path="./chromadb_persist", settings=Settings())

# Access your collection
collection = chroma_client.get_or_create_collection(name="movie_collection")
logging.critical(f"Loaded collection: {collection.name}")

def get_movie_recommendations(user_query: str) -> List[Dict[str, Any]]:
    """Retrieve movie recommendations based on a user query from the ChromaDB collection."""
    results = collection.query(
        query_texts=[user_query],
        n_results=5,
        include=['documents', 'metadatas']
    )
    recommendations = []
    for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
        recommendations.append({
            "Title": metadata.get("Title", ""),
            "Genre": metadata.get("Genre", ""),
            "Rating": metadata.get("Rating", 0),
            "Review_Title": metadata.get("Review_Title", ""),
            "Review": doc,
        })
    return recommendations

# Example of calling the Gemini model (optional)
def generate_text(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    return response.text