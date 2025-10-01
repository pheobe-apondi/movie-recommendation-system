from google import genai
from .tools import get_movie_recommendations
from google.adk.agents import LlmAgent
client = genai.Client()
def movie_recommendation_tool(user_query: str):
    return get_movie_recommendations(user_query)
class MultiToolAgent(LlmAgent):
    def __init__(self, name: str, model_name: str):
        super().__init__(
            name=name,  
            model=model_name, 
            instruction="""You are a helpful movie recommendation assistant.
            When handling movie requests:
            1. Use a Chain of Thought approach to reason step-by-step about the user's request:
               - First, analyze the request to identify key elements and potential ambiguities
               - Consider different possible interpretations of the request
               - Generate recommendations for each interpretation
               - Organize recommendations by category or interpretation
            2. For Zero-Shot responses:
               - Provide direct recommendations without excessive questions
               - Keep explanations concise but informative
               - Include 2-3 specific movie titles with brief reasons
            3. Format your response as follows:
               - Present recommendations in clearly labeled categories when appropriate
               - For each movie, include title, year, and a brief reason
            4. For complex queries (like "romantic movie about cancer"):
               - Break down into multiple interpretation categories
               - Provide 3-4 movie recommendations per category
            """
        )
    def start_chat(self):
        local_client = genai.Client()
        return local_client.chat_models.get_chat(self.model)
root_agent = MultiToolAgent(name="multi_tool_agent", model_name="gemini-1.5-flash")
def get_combined_recommendations(chat, user_query):
    """
    Uses a prompt combining chain-of-thought reasoning with zero-shot recommendations.
    Args:
        chat: The chat session object
        user_request: The user's movie request (may include genre but also other preferences)
    Returns:
        The model's response containing both reasoning and recommendations with detailed explanations
    """
    combined_prompt = (
        f"You are a knowledgeable movie recommendation assistant.\n\n"
        f"Let's think step by step about this movie request: \"{user_query}\"\n"
        f"Step 1: Analyze the request to identify key elements:\n"
        f"   - What genre(s) are mentioned or implied?\n"
        f"   - What mood or tone is the user looking for?\n"
        f"   - Are there specific themes, settings, or elements mentioned?\n"
        f"   - What might the user's unspoken preferences be?\n\n"
        f"Step 2: Consider different interpretations of the request\n"
        f"   - What are the possible ways to interpret this request?\n"
        f"   - What related genres or sub-genres might be relevant?\n\n"
        f"Step 3: Determine what makes a great movie recommendation for this request\n"
        f"   - Consider plot quality, character development, cinematography, direction\n"
        f"   - Consider critical reception, audience ratings, and cultural impact\n"
        f"   - Consider how well the movie matches the user's likely preferences\n\n"
        f"Step 4: Recommend 3 exceptional movies that match this request\n"
        f"   For each movie, provide:\n"
        f"   - Title and year of release\n"
        f"   - A detailed explanation (5-7 sentences) covering:\n"
        f"     * How it matches the user's request\n"
        f"     * What makes it outstanding (specific strengths)\n"
        f"     * Why viewers with these preferences would enjoy it\n"
        f"     * Notable performances or technical achievements\n\n"
        f"Format your response with clear headings for each movie. "
        f"Use a friendly, engaging tone. Do not ask follow-up questions."
    )
    response = chat.send_message(combined_prompt)
    return response.text

if __name__ == "__main__":
    chat = root_agent.start_chat()
    complex_query = "I need a romantic movie about cancer"
    complex_result = get_combined_recommendations(chat, complex_query)
    print("Response to complex query:")
    print(complex_result)
    specific_query = "Recommend a comedy with Jim Carrey"
    specific_response = chat.send_message(specific_query)
    print("\nResponse to specific query:")
    print(specific_response.text)


# from google import genai
# from .tools import get_movie_recommendations
# from google.adk.agents import LlmAgent

# # Initialize the Gemini client
# client = genai.Client()

# # Define your tool wrapper to pass into your AI application logic (if needed)
# def movie_recommendation_tool(user_query: str):
#     return get_movie_recommendations(user_query)

# # Define your root conversational agent using LlmAgent
# class MultiToolAgent(LlmAgent):
#     def __init__(self, name: str, model_name: str):
#         super().__init__(
#             name=name,
#             model=model_name,
#             instruction="""You are a helpful movie recommendation assistant. 
#             When handling movie requests:
#             1. Use a Chain of Thought approach to reason step-by-step about the user's request
#             2. First, analyze the request to identify key elements and potential ambiguities
#             3. Consider different possible interpretations of the request
#             4. Generate recommendations for each interpretation
#             5. Organize recommendations by category or interpretation
#             6. Keep explanations concise but informative
#             7. End by inviting more specific input for better recommendations
            
#             For specific queries, provide direct recommendations without excessive questions.
#             """
#         )
    
#     def start_chat(self):
#          # Create a new client instance when needed
#         local_client = genai.Client()
#         return local_client.chat_models.get_chat(self.model)

# # Create the root_agent with a name
# root_agent = MultiToolAgent(name="multi_tool_agent", model_name="gemini-1.5-flash")

# def get_combined_recommendations(chat, user_query):
#     """
#     Combines Zero-Shot and Chain of Thought techniques for optimized recommendations.
    
#     Args:
#         chat: The chat session object
#         user_query: The user's movie request
        
#     Returns:
#         The model's response with structured recommendations based on combined reasoning
#     """
#     combined_prompt = f"""
#     Let's think step by step about this movie request: "{user_query}"
    
#     Step 1: Analyze the request to identify key elements and potential ambiguities
#     Step 2: Consider different possible interpretations of the request
#     Step 3: For each interpretation, determine what would make a good movie recommendation
#     Step 4: Generate 2-3 movie recommendations for each interpretation with brief reasons
#     Step 5: Organize the recommendations by interpretation
    
#     Now, based on this reasoning, provide your response in this format:
#     1. Brief explanation of why the request needs clarification
#     2. 1-2 key questions to understand preferences
#     3. Organized recommendations by interpretation with brief explanations
#     4. Invitation for more specific input
#     """
    
#     response = chat.send_message(combined_prompt)
#     return response.text

# # Example usage
# if __name__ == "__main__":
#     chat = root_agent.start_chat()
    
#     # Test with a complex query
#     complex_query = "I want a movie centered around cancer"
#     complex_result = get_combined_recommendations(chat, complex_query)
#     print("Response to complex query:")
#     print(complex_result)
    
#     # Test with a specific query
#     specific_query = "Recommend a comedy with Jim Carrey"
#     specific_response = chat.send_message(specific_query)
#     print("\nResponse to specific query:")
#     print(specific_response.text)
