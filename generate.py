from jinja2 import Template
import random

INTENTS = ["Volunteer mission", "Business trip", "Extreme tourism", "Scientific research"]
INFRASTRUCTURES = ["None (Off-grid)", "Basic (Rural)", "Mixed", "Urban/Modern"]
CLIMATES = ["Tropical Rain", "Arid Desert", "Arctic Cold", "High Altitude"]
RISKS = ["High humidity", "Dust storms", "Poor water quality", "Power instability"]

def get_random_duration():
    return random.choices(
        population=[
            random.randint(1, 3),
            random.randint(4, 10),
            random.randint(11, 30),
            random.randint(31, 90)
        ],
        weights=[0.3, 0.4, 0.2, 0.1]
    )[0]

template = Template("""
Role: Expert Logistics Officer.
Task: Create a precise packing list.

Context:
- Intent: {{ intent }}
- Duration: {{ duration }} days
- Infrastructure: {{ infra }}
- Risk Factor: {{ risk }}

Requirements:
1. Scale quantities based on the {{ duration }} days duration. 
2. For hygiene and clothing, use a logical formula (e.g., N or N+1).
3. If infrastructure is Low and duration is > 7 days, include maintenance/repair kits.
4. Return the result in structured JSON.
""")