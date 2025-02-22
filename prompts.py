def get_system_prompt():
    return """
    You are a Hiring Assistant chatbot for TalentScout. Your task is to:
    1. Greet the candidate and collect their information.
    2. Generate technical questions based on their tech stack.
    3. Maintain context and handle follow-up questions.
    """

def generate_questions(tech_stack):
    return f"""
    Generate 3-5 technical questions to assess the candidate's proficiency in: {tech_stack}.
    Ensure the questions are relevant and challenging.
    """