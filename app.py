from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
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
        # Check for greetings first
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
    
    def process_query(self, query, knowledge_base):
        tokens = self.preprocess_text(query)
        keywords = self.extract_keywords(query)
        intent = self.get_intent_from_keywords(keywords, knowledge_base)
        
        return {
            'original_query': query,
            'tokens': tokens,
            'keywords': keywords,
            'intent': intent
        }

class HealthcareChatbot:
    def __init__(self):
        self.nlp_processor = SimpleNLPProcessor()
        self.knowledge_base = get_knowledge_base()
        self.emergency_keywords = get_emergency_keywords()
        self.diagnosis_keywords = get_diagnosis_keywords()
        self.medication_keywords = get_medication_keywords()
    
    def check_emergency(self, query):
        query_lower = query.lower()
        for keyword in self.emergency_keywords:
            if keyword in query_lower:
                return True
        return False
    
    def check_diagnosis_request(self, query):
        query_lower = query.lower()
        for keyword in self.diagnosis_keywords:
            if keyword in query_lower:
                return True
        return False
    
    def check_medication_request(self, query):
        query_lower = query.lower()
        for keyword in self.medication_keywords:
            if keyword in query_lower:
                return True
        return False
    
    def process_query(self, query):
        # Check for emergency
        if self.check_emergency(query):
            return {
                'response': 'This sounds like a medical emergency. Please call emergency services immediately (911 or your local emergency number).',
                'type': 'emergency'
            }
        
        # Check for diagnosis request
        if self.check_diagnosis_request(query):
            return {
                'response': 'I cannot provide medical diagnosis. Please consult a qualified healthcare provider for personal medical concerns.',
                'type': 'safety_diagnosis'
            }
        
        # Check for medication request
        if self.check_medication_request(query):
            return {
                'response': 'I cannot provide medication advice. Consult your doctor or pharmacist for medication-related questions.',
                'type': 'safety_medication'
            }
        
        # Process with NLP
        nlp_result = self.nlp_processor.process_query(query, self.knowledge_base)
        
        if nlp_result['intent']:
            intent_data = nlp_result['intent']
            return {
                'response': intent_data['data']['response'],
                'type': intent_data['topic']
            }
        
        # Default response
        return {
            'response': 'I can help with general health questions about fever, cold, headache, diet, exercise, first aid, and stress management. Please ask about these topics.',
            'type': 'default'
        }
    
    def get_chatbot_info(self):
        return {
            'name': 'Healthcare Assistant',
            'version': '1.0',
            'capabilities': [
                'General health information',
                'Symptom awareness',
                'First aid guidance',
                'Preventive health tips'
            ],
            'limitations': [
                'No medical diagnosis',
                'No medication advice',
                'Not for emergencies',
                'Consult healthcare professionals for medical concerns'
            ]
        }

# Flask App
app = Flask(__name__)
CORS(app)

# Initialize chatbot
chatbot = HealthcareChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        result = chatbot.process_query(user_message)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/info')
def info():
    return jsonify(chatbot.get_chatbot_info())

if __name__ == '__main__':
    print('Starting Healthcare Chatbot...')
    print('Open your browser and go to: http://localhost:5000')
    app.run(debug=True, host='0.0.0.0', port=5000)
