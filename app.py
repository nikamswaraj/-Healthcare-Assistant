# -*- coding: utf-8 -*-
import streamlit as st
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from intents import get_knowledge_base, get_emergency_keywords, get_diagnosis_keywords, get_medication_keywords

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

class SimpleNLPProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = word_tokenize(text)
        filtered_tokens = []
        for token in tokens:
            if token not in self.stop_words and len(token) > 2:
                lemmatized = self.lemmatizer.lemmatize(token)
                filtered_tokens.append(lemmatized)
        return filtered_tokens
    
    def extract_keywords(self, text):
        text_lower = text.lower()
        greetings = ['hi', 'hello', 'hey', 'greetings']
        for greeting in greetings:
            if greeting in text_lower:
                return [greeting]
        return self.preprocess_text(text)
    
    def get_intent_from_keywords(self, keywords, knowledge_base):
        intent_scores = {}
        for category, topics in knowledge_base.items():
            for topic, data in topics.items():
                topic_keywords = [kw.lower() for kw in data['keywords']]
                matches = 0
                for keyword in keywords:
                    for topic_keyword in topic_keywords:
                        if keyword in topic_keyword or topic_keyword in keyword:
                            matches += 1
                if matches > 0:
                    intent_key = f'{category}_{topic}'
                    intent_scores[intent_key] = {
                        'score': matches,
                        'category': category,
                        'topic': topic,
                        'data': data
                    }
        if intent_scores:
            best_intent = max(intent_scores.items(), key=lambda x: x[1]['score'])
            return best_intent[1]
        return None

class HealthcareChatbot:
    def __init__(self):
        self.nlp_processor = SimpleNLPProcessor()
        self.knowledge_base = get_knowledge_base()
        self.emergency_keywords = get_emergency_keywords()
        self.diagnosis_keywords = get_diagnosis_keywords()
        self.medication_keywords = get_medication_keywords()
    
    def check_emergency(self, query):
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.emergency_keywords)
    
    def check_diagnosis_request(self, query):
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.diagnosis_keywords)
    
    def check_medication_request(self, query):
        query_lower = query.lower()
        return any(keyword in query_lower for keyword in self.medication_keywords)
    
    def process_query(self, query):
        if self.check_emergency(query):
            return {
                'response': '🚨 **EMERGENCY ALERT**\n\nThis sounds serious! Please call emergency services immediately (911 or your local emergency number).',
                'type': 'emergency'
            }
        
        if self.check_diagnosis_request(query):
            return {
                'response': '⚠️ **Medical Advice Notice**\n\nI cannot provide medical diagnosis. Please consult a qualified healthcare provider for personal medical concerns.',
                'type': 'safety_diagnosis'
            }
        
        if self.check_medication_request(query):
            return {
                'response': '💊 **Medication Notice**\n\nI cannot provide medication advice. Please consult your doctor or pharmacist for medication-related questions.',
                'type': 'safety_medication'
            }
        
        keywords = self.nlp_processor.extract_keywords(query)
        intent = self.nlp_processor.get_intent_from_keywords(keywords, self.knowledge_base)
        
        if intent:
            return {
                'response': intent['data']['response'],
                'type': intent['topic']
            }
        
        return {
            'response': '👋 **Hi there!**\n\nI\'m your healthcare assistant. I can help with general health information about:\n\n• Fever\n• Cold & Flu\n• Headache\n• Diet & Nutrition\n• Exercise\n• First Aid\n• Stress Management\n\nWhat would you like to know?',
            'type': 'default'
        }

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = HealthcareChatbot()
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Page config
st.set_page_config(
    page_title="Healthcare Assistant",
    page_icon="🫥"
)

# App title and description
st.title("🫥 Healthcare Assistant")
st.markdown("""
I'm here to provide general health information. I can help with:
- 🨒 Fever, cold, and headache
- 🥗 Diet and nutrition
- 🏃 Exercise and fitness
- 🫤 First aid
- 🧘 Stress management
""")

# Chat interface
with st.container():
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about health..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get bot response
        response = st.session_state.chatbot.process_query(prompt)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response['response']})
        
        # Rerun to update the chat
        st.rerun()

# Sidebar with additional info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **Healthcare Assistant** provides general health information only.
    
    **Not for emergencies** - Call 911 for medical emergencies.
    
    **Not medical advice** - Always consult healthcare professionals.
    """)
    
    st.markdown("---")
    st.markdown("**Topics I can help with:**")
    st.markdown("""
    - 🨒 Fever, Cold, Headache
    - 🥗 Diet & Nutrition
    - 🏃 Exercise & Fitness
    - 🫤 First Aid
    - 🧘 Stress Management
    """)

# Add some styling
st.markdown("""
<style>
    .stChatFloatingInputContainer {
        bottom: 20px;
    }
    .stChatMessage {
        padding: 12px 16px;
        border-radius: 15px;
        margin: 8px 0;
    }
</style>
""", unsafe_allow_html=True)