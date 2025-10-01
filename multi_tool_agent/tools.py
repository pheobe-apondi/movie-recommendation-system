from chromadb.config import Settings
import chromadb
from typing import List, Dict, Any
import os
import logging

from google import genai

client = genai.Client()

chroma_client = chromadb.PersistentClient(path="./chromadb_persist", settings=Settings())

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

def generate_text(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    return response.text
