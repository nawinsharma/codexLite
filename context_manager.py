from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def should_summarize_context(messages):
    """Check if context should be summarized"""
    total_tokens = sum(len(msg["content"]) for msg in messages)
    return total_tokens > 15000

def summarize_context(messages):
    """Summarize conversation context"""
    try:
        system_msg = messages[0]
        recent_messages = messages[-10:]
        
        middle_messages = messages[1:-10] if len(messages) > 11 else []
        
        if middle_messages:
            summary_prompt = """Summarize the following conversation between a user and a coding assistant. 
            Focus on: 1) What project was built, 2) Key features implemented, 3) Current state of the project.
            Keep it concise but informative."""
            
            summary_content = "\n".join([msg["content"] for msg in middle_messages])
            
            summary_response = client.chat.completions.create(
                model="gpt-4o-mini",  # Use cheaper model for summarization
                messages=[
                    {"role": "system", "content": summary_prompt},
                    {"role": "user", "content": summary_content}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            summary = summary_response.choices[0].message.content
            summary_msg = {"role": "system", "content": f"CONTEXT SUMMARY: {summary}"}
            
            return [system_msg, summary_msg] + recent_messages
        
        return messages
    except Exception as e:
        print(f"Error summarizing context: {e}")
        return messages 