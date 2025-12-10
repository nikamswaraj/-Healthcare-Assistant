# Intents and Knowledge Base for Healthcare Chatbot

KNOWLEDGE_BASE = {
    'greetings': {
        'hello': {
            'keywords': ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
            'response': 'Hi! I am your healthcare assistant. I can help you with general health information, symptoms awareness, first-aid guidance, and preventive tips. How can I assist you today?'
        },
        'how_are_you': {
            'keywords': ['how are you', 'how do you do', 'what\'s up'],
            'response': 'I am functioning well and ready to help with your health-related questions! What health topic would you like to know about?'
        }
    },
    'general_health': {
        'fever': {
            'keywords': ['fever', 'temperature', 'hot', 'feverish', 'high temperature'],
            'response': 'Fever is a temporary increase in body temperature, often due to illness. Normal body temperature is around 98.6°F (37°C). For mild fever: drink plenty of fluids, rest, and consider over-the-counter fever reducers. Contact a doctor if fever is very high or lasts more than 3 days.'
        },
        'cold': {
            'keywords': ['cold', 'runny nose', 'sneezing', 'congestion', 'stuffy nose'],
            'response': 'Common cold symptoms include runny nose, sore throat, cough, congestion, and mild body aches. Most colds resolve within 7-10 days. Get plenty of rest, drink fluids, use saline nasal spray, and consider over-the-counter cold medications for symptom relief.'
        },
        'headache': {
            'keywords': ['headache', 'migraine', 'head pain', 'head hurts'],
            'response': 'Headaches can have many causes including stress, dehydration, lack of sleep, or medical conditions. For mild headaches: rest in a quiet room, apply cold compress, stay hydrated, and consider over-the-counter pain relievers. Seek medical attention for severe or persistent headaches.'
        }
    },
    'diet_nutrition': {
        'healthy_diet': {
            'keywords': ['healthy diet', 'nutrition', 'balanced diet', 'eating healthy', 'good food'],
            'response': 'A healthy diet includes: fruits and vegetables, whole grains, lean proteins, healthy fats, and limited processed foods. Aim for variety, portion control, and regular meal timing. The WHO recommends at least 5 servings of fruits and vegetables daily.'
        },
        'hydration': {
            'keywords': ['hydration', 'water', 'drink water', 'dehydrated', 'thirsty'],
            'response': 'Proper hydration is essential for health. Adults should drink about 8 glasses (64 ounces) of water daily, more if active or in hot weather. Signs of dehydration include thirst, dark urine, fatigue, and dizziness.'
        },
        'vitamins': {
            'keywords': ['vitamins', 'supplements', 'vitamin d', 'vitamin c', 'multivitamin'],
            'response': 'Vitamins are essential for body functions. Best sources are whole foods: Vitamin C from citrus fruits, Vitamin D from sunlight and fatty fish, B vitamins from whole grains, etc. Supplements may help if dietary intake is insufficient.'
        }
    },
    'exercise_fitness': {
        'physical_activity': {
            'keywords': ['exercise', 'physical activity', 'workout', 'fitness', 'gym'],
            'response': 'WHO recommends at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity activity per week. Include muscle-strengthening activities 2+ days per week. Start slowly and gradually increase intensity.'
        },
        'walking': {
            'keywords': ['walking', 'walk', 'daily walk', 'brisk walk'],
            'response': 'Walking is excellent exercise. Aim for 30 minutes of brisk walking daily. It improves cardiovascular health, helps maintain weight, reduces stress, and strengthens bones. Start with 10-15 minutes if new to exercise.'
        }
    },
    'first_aid': {
        'basic_care': {
            'keywords': ['first aid', 'emergency', 'help', 'injury'],
            'response': 'For minor injuries: clean wounds with water, apply pressure to bleeding, elevate injured limb, use cold compress for swelling. Always seek medical help for severe injuries, deep cuts, or if unsure.'
        },
        'cuts': {
            'keywords': ['cut', 'wound', 'bleeding', 'scrape'],
            'response': 'For minor cuts: clean with water, apply antiseptic, cover with bandage. For deep cuts or heavy bleeding: apply firm pressure with clean cloth, elevate if possible, seek medical attention immediately.'
        },
        'burns': {
            'keywords': ['burn', 'burned', 'scald', 'heat burn'],
            'response': 'For minor burns: run cool (not cold) water for 10-20 minutes, cover with clean cloth. Don\'t use ice, butter, or ointments. For severe burns: seek emergency medical care immediately.'
        }
    },
    'mental_health': {
        'stress': {
            'keywords': ['stress', 'anxiety', 'relax', 'stress relief', 'tension'],
            'response': 'Common stress management techniques include: deep breathing exercises, regular physical activity, adequate sleep (7-9 hours), mindfulness meditation, and talking with friends/family. Limit caffeine and alcohol intake.'
        }
    }
}

# Safety keywords
EMERGENCY_KEYWORDS = [
    'chest pain', 'difficulty breathing', 'unconscious', 'severe bleeding',
    'heart attack', 'stroke', 'emergency', 'call 911', 'call ambulance',
    'can\'t breathe', 'unresponsive', 'fainting', 'severe pain'
]

DIAGNOSIS_KEYWORDS = [
    'diagnose', 'diagnosis', 'what do i have', 'what is wrong with me',
    'what condition', 'identify disease', 'medical diagnosis'
]

MEDICATION_KEYWORDS = [
    'medicine', 'medication', 'drug', 'prescribe', 'prescription',
    'what medicine', 'which drug', 'medical treatment', 'pill',
    'tablet', 'dosage'
]

def get_knowledge_base():
    return KNOWLEDGE_BASE

def get_emergency_keywords():
    return EMERGENCY_KEYWORDS

def get_diagnosis_keywords():
    return DIAGNOSIS_KEYWORDS

def get_medication_keywords():
    return MEDICATION_KEYWORDS
