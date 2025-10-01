
# Movie Recommendation AI Agent

## Overview

This repository hosts an AI-powered movie recommendation system built using Google’s Agent Development Kit (ADK). The agent leverages Retrieval-Augmented Generation (RAG) techniques to recommend movies based on user preferences. It intelligently integrates external knowledge retrieval with generative AI to provide personalized, accurate movie suggestions.

## Features

- **Interactive AI Agent:** Uses Google ADK to handle conversational user input and preferences.
- **RAG System Architecture:** Combines retrieval of relevant movie data and language generation to deliver precise recommendations.
- **Personalization:** Tailors suggestions according to user requests such as genres, moods, themes, actors, or specific interests.
- **Context-aware Recommendations:** Ensures suggestions align with current user context and preferences to improve relevance.
- **Explainability:** Provides explanations or reasoning behind each recommendation to enhance trust and transparency.

## Architecture

The system architecture consists of:

- **User Interface:** Receives user input describing what kind of movies they want.
- **Retrieval Module:** Searches relevant movie data or documents to find contextually appropriate content.
- **Generation Module:** Uses an AI language model integrated in ADK to generate recommendation outputs.
- **RAG Integration:** Combines retrieval and generation to ground output on factual movie data and minimize hallucinations.

## Additional Implementation Details

- Embedded movie metadata using **ChromaDB** for fast semantic search of movie information.
- Orchestrated the recommendation workflow with Google ADK for modular reasoning across multiple steps.
- Tested different prompting strategies including few-shot, zero-shot, and chain-of-thought prompting.
- Found a **zero-shot + chain-of-thought hybrid** approach to be the most reliable for recommendation quality.

## Installation

1. Clone the repo:
   ```
   git clone https://github.com/pheobe-apondi/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install dependencies (Python example):
   ```
   pip install -r requirements.txt
   ```
3. Set up Google ADK credentials and environment variables as explained in the [Google ADK documentation](https://google.github.io/adk-docs/).

## Usage

Start the agent and interact via the command line or web interface:

```
adk web
```

Enter your movie preferences as prompted (e.g., "I'm in the mood to watch a movie where the protagonist battles with cancer").

The agent will process your input, retrieve relevant movie information, then generate and display recommendations.

## How It Works

1. User input is parsed and sent to the retrieval system.
2. The retrieval module returns relevant movie data enriched with metadata stored in ChromaDB.
3. The generative model within the Google ADK agent uses this retrieved data as context to formulate recommendations.
4. Results are returned to the user with explanations when applicable.

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements, new features, or bug fixes.


