from flask import Flask, render_template, request

emergencies = {
    # Drowning / Water emergencies
    "drowning": "Call emergency services immediately. Remove the person from water safely. Check breathing and pulse. Start CPR if needed.",
    "submerged": "Call emergency services immediately. Remove the person from water safely. Check breathing and pulse. Start CPR if needed.",
    "water": "If someone is struggling in water, call emergency services immediately and provide help safely.",
    
    # Choking
    "choking": "If the person cannot breathe, perform the Heimlich maneuver. Call emergency services if obstruction persists.",
    "food stuck": "Perform the Heimlich maneuver if the person cannot breathe. Call emergency services.",
    "airway blocked": "Clear the airway if possible and perform the Heimlich maneuver. Call emergency services if needed.",
    
    # Heart / Cardiac issues
    "heart attack": "Call emergency services immediately. Start chest compressions (CPR) if unconscious and not breathing.",
    "chest pain": "Call emergency services immediately. Keep the person calm and seated if conscious.",
    "palpitations": "Monitor the person and call emergency services if symptoms persist or worsen.",
    
    # Bleeding / Injury
    "cut": "Apply pressure to stop bleeding. Elevate injured limb if possible. Call emergency services if bleeding is severe.",
    "bleeding": "Apply pressure to stop bleeding. Elevate injured limb if possible. Call emergency services if severe.",
    "wound": "Clean minor wounds and apply bandage. Call emergency services for deep or severe wounds.",
    "bone": "Immobilize the injured limb and call emergency services for suspected fractures.",
    "fracture": "Immobilize the limb and seek medical help immediately.",
    
    # Dizziness / Fainting
    "dizzy": "Sit or lie down immediately. Elevate legs if feeling faint. Call emergency services if person loses consciousness.",
    "faint": "Sit or lie down. Elevate legs. Call emergency services if person loses consciousness.",
    "lightheaded": "Sit or lie down. Drink water if dehydrated. Call emergency services if symptoms persist.",
    
    # Burns
    "burn": "Cool the burn under running water for at least 10 minutes. Remove tight items. Call emergency services for severe burns.",
    "fire": "Move away from fire and cool any burns. Call emergency services if severe.",
    "scald": "Cool the burn immediately under running water. Seek medical help for severe burns.",
    
    # Allergic reaction / Anaphylaxis
    "allergy": "Use an epinephrine auto-injector if available. Call emergency services immediately.",
    "swelling": "Monitor for breathing difficulty. Use epinephrine if severe and call emergency services.",
    "hives": "Call emergency services if accompanied by difficulty breathing.",
    "trouble breathing": "Call emergency services immediately. Administer epinephrine if severe.",
    "anaphylaxis": "Use epinephrine auto-injector immediately. Call emergency services.",
    
    # Stalking / Safety / Threat
    "stalked": "Move to a safe, public location. Call police or local emergency services immediately.",
    "following": "Go to a safe area. Call emergency services. Avoid isolated areas.",
    "threat": "Stay safe and call police or emergency services immediately.",
    "unsafe": "Seek a safe location and call emergency services if needed.",
    
    # Concussion / Head injury
    "hit head": "Keep the person still and calm. Monitor for vomiting, confusion, or unconsciousness. Call emergency services immediately.",
    "concussion": "Monitor symptoms closely and call emergency services if severe.",
    "head injury": "Keep the person still. Seek medical attention immediately.",
    
    # Seizures
    "seizure": "Move objects away to prevent injury. Do not restrain. Time the seizure. Call emergency services if it lasts over 5 minutes or first-time.",
    "convulsion": "Protect from injury. Do not restrain. Call emergency services if seizure is prolonged or first-time.",
    "uncontrollable shaking": "Move hazards away. Call emergency services if necessary.",
    
    # Other life-threatening emergencies
    "unconscious": "Check breathing and pulse. Call emergency services immediately. Start CPR if needed.",
    "not breathing": "Call emergency services immediately. Begin CPR immediately.",
    "collapsed": "Check responsiveness. Call emergency services. Provide first aid as needed."
}


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_text = request.form.get('user_input')
    response = ""

    for keyword, advice in emergencies.items():
        if keyword in user_text.lower():
            response = advice
            break
    else:
        response = "Sorry, I do not know how to help with that. The best answer is to call emergency services as soon as possible."

    # Render the template and pass the response to it
    return render_template('index.html', server_response=response)


if __name__ == '__main__':
    app.run(debug=True)

"""
ORIGINAL PLAN - AI GENERATED RESPONSES

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_text = request.form['user_input']
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"I'm in an emergency: {user_text}. Give step-by-step first aid instructions."}]
    )
    
    instructions = response['choices'][0]['message']['content']
    return render_template('index.html', instructions=instructions)

if __name__ == "__main__":
    app.run(debug=True)
"""