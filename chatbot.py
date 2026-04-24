"""
Chatbot Module - Rule-based symptom guidance system
This module provides educational guidance about symptoms.
IMPORTANT: This does NOT diagnose or prescribe medications.
"""

import re

def get_symptom_guidance(user_input):
    """
    Analyze user input and provide educational guidance about symptoms.
    
    Args:
        user_input: String containing user's symptom description
    
    Returns:
        String with educational guidance, possible causes, care advice, and red flags
    """
    user_input_lower = user_input.lower()
    
    # Initialize response components
    possible_issues = []
    care_advice = []
    red_flags = []
    
    # Check for fever symptoms
    if any(word in user_input_lower for word in ['fever', 'temperature', 'hot', 'burning']):
        possible_issues.append("• May be related to infections, inflammatory conditions, or other underlying causes")
        care_advice.append("• Rest and stay hydrated")
        care_advice.append("• Monitor temperature regularly")
        care_advice.append("• Use cool compresses if comfortable")
        care_advice.append("• Over-the-counter fever reducers may help (consult pharmacist)")
        red_flags.append("• Fever above 103°F (39.4°C) or lasting more than 3 days")
        red_flags.append("• Severe headache, stiff neck, or confusion")
        red_flags.append("• Difficulty breathing or chest pain")
        red_flags.append("• Rash that spreads quickly")
    
    # Check for cold and cough symptoms
    if any(word in user_input_lower for word in ['cold', 'cough', 'sneeze', 'runny nose', 'congestion', 'nasal']):
        possible_issues.append("• May be related to common cold, allergies, or respiratory infections")
        care_advice.append("• Get plenty of rest")
        care_advice.append("• Stay hydrated with warm fluids")
        care_advice.append("• Use a humidifier or steam inhalation")
        care_advice.append("• Gargle with warm salt water for throat irritation")
        care_advice.append("• Wash hands frequently to prevent spread")
        red_flags.append("• Cough lasting more than 2-3 weeks")
        red_flags.append("• Difficulty breathing or wheezing")
        red_flags.append("• High fever (above 101°F/38.3°C)")
        red_flags.append("• Chest pain or coughing up blood")
        red_flags.append("• Severe headache or facial pain")
    
    # Check for headache symptoms
    if any(word in user_input_lower for word in ['headache', 'head pain', 'migraine', 'head ache']):
        possible_issues.append("• May be related to tension, dehydration, stress, or other factors")
        care_advice.append("• Rest in a quiet, dark room")
        care_advice.append("• Stay hydrated")
        care_advice.append("• Apply a cold or warm compress to forehead or neck")
        care_advice.append("• Practice relaxation techniques")
        care_advice.append("• Over-the-counter pain relievers may help (consult pharmacist)")
        red_flags.append("• Sudden, severe headache (worst of your life)")
        red_flags.append("• Headache after head injury")
        red_flags.append("• Headache with fever, stiff neck, or confusion")
        red_flags.append("• Headache with vision changes or weakness")
        red_flags.append("• Headache that worsens with activity")
    
    # Check for stomach pain symptoms
    if any(word in user_input_lower for word in ['stomach', 'abdominal', 'belly', 'nausea', 'vomit', 'diarrhea', 'constipation']):
        possible_issues.append("• May be related to digestive issues, food intolerance, or gastrointestinal conditions")
        care_advice.append("• Avoid solid foods for a few hours if nauseous")
        care_advice.append("• Sip clear fluids (water, broth)")
        care_advice.append("• Eat bland foods when ready (bananas, rice, toast)")
        care_advice.append("• Avoid spicy, fatty, or dairy foods")
        care_advice.append("• Rest and avoid strenuous activity")
        red_flags.append("• Severe abdominal pain or tenderness")
        red_flags.append("• Vomiting blood or blood in stool")
        red_flags.append("• Persistent vomiting or inability to keep fluids down")
        red_flags.append("• Signs of dehydration (dry mouth, no urination)")
        red_flags.append("• Pain that moves to right lower abdomen")
        red_flags.append("• Fever with abdominal pain")
    
    # Check for fatigue symptoms
    if any(word in user_input_lower for word in ['tired', 'fatigue', 'exhausted', 'weak', 'lethargy', 'low energy']):
        possible_issues.append("• May be related to lack of sleep, stress, nutritional deficiencies, or other factors")
        care_advice.append("• Ensure adequate sleep (7-9 hours per night)")
        care_advice.append("• Maintain a regular sleep schedule")
        care_advice.append("• Eat balanced meals regularly")
        care_advice.append("• Stay hydrated")
        care_advice.append("• Engage in light physical activity")
        care_advice.append("• Manage stress through relaxation techniques")
        red_flags.append("• Fatigue with unexplained weight loss")
        red_flags.append("• Severe fatigue affecting daily activities")
        red_flags.append("• Fatigue with chest pain or shortness of breath")
        red_flags.append("• Fatigue with persistent fever")
        red_flags.append("• Fatigue with depression or mood changes")
    
    # If no specific symptoms matched, provide general guidance
    if not possible_issues:
        response = """I understand you're experiencing some symptoms. Here's some general guidance:

**General Care Advice:**
• Rest and stay hydrated
• Monitor your symptoms
• Keep track of when symptoms started and any patterns
• Maintain good hygiene practices

**When to Consult a Doctor:**
• Symptoms that are severe or worsening
• Symptoms lasting more than a few days
• Any concerns about your health
• If you're unsure about your symptoms

**Important:** This is educational information only and not a substitute for professional medical advice. Please consult a healthcare provider for proper evaluation and treatment.

Is there a specific symptom you'd like to know more about? You can mention symptoms like fever, headache, stomach pain, cold/cough, or fatigue."""
        return response
    
    # Build comprehensive response
    response = "Based on your symptoms, here's some educational information:\n\n"
    
    response += "**Possible Health Issues (Educational Information):**\n"
    response += "\n".join(possible_issues) + "\n\n"
    
    response += "**General Care Advice:**\n"
    response += "\n".join(care_advice) + "\n\n"
    
    response += "**When to Consult a Doctor (Red Flags):**\n"
    response += "\n".join(red_flags) + "\n\n"
    
    response += "**Important Medical Disclaimer:**\n"
    response += "This information is for educational purposes only and is NOT a medical diagnosis or prescription. "
    response += "Always consult with a qualified healthcare provider for proper evaluation, diagnosis, and treatment. "
    response += "If you experience any of the red flags mentioned above, seek immediate medical attention."
    
    return response


