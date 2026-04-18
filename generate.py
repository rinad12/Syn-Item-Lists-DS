from jinja2 import Template
import random

# The "Why": Dictates specialized gear and formal/functional requirements
INTENTS = [
    "Volunteer mission", "Business trip", "Extreme tourism", 
    "Scientific research", "Digital nomadism", "Humanitarian aid",
    "Photography expedition", "Spiritual pilgrimage", "Competitive sports",
    "Formal event/Wedding", "Family vacation"
]

# The "Where": Determines the need for self-sufficiency and utility tools
INFRASTRUCTURES = [
    "None (Off-grid/Wilderness)", "Basic (Rural/Remote)", 
    "Developing (Inconsistent utilities)", "Mixed (Standard)", 
    "Urban/Modern (High-tech)", "Industrial/Work site",
    "Resort/Managed environment"
]

# The "Environment": Focuses on layering, fabrics, and protection
CLIMATES = [
    "Tropical Rain (High Humidity)", "Arid Desert (Dry Heat)", 
    "Arctic Cold (Sub-zero)", "High Altitude (Thin Air/UV)",
    "Temperate (Variable/Four Seasons)", "Mediterranean (Dry Summer/Wet Winter)",
    "Maritime (High Wind/Salt Spray)", "Monsoonal (Seasonal Heavy Rain)"
]

# The "Precaution": Triggers health, security, and maintenance items
RISKS = [
    "High humidity/Mold", "Dust & Sand storms", "Poor water quality", 
    "Power instability", "Vector-borne disease (Mosquitoes/Ticks)",
    "High UV exposure", "Physical theft/Pickpocketing", 
    "Civil instability", "Extreme wildlife", "Air pollution/Smog"
]

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

current_risks = random.sample(RISKS, k=random.randint(1, 3))

template = Template("""
Role: Expert Logistics Officer.
Task: Create a highly precise, context-aware packing list.

Context:
- Intent: {{ intent }}
- Duration: {{ duration }} days
- Infrastructure Level: {{ infra }}
- Risk Factors: 
{% for risk in risks %}  * {{ risk }}
{% endfor %}

Requirements:
1. **Adaptive Scaling:** Calculate quantities strictly based on the {{ duration }}-day duration. Use logical formulas ($N$ or $N+1$) for daily essentials.
2. **Risk Mitigation:** For every risk factor listed, include at least one specific item or preparation measure. 
3. **Compound Threats:** If multiple risks overlap (e.g., "Heavy Rain" and "No Electricity"), prioritize items that address both (e.g., waterproof power bank or manual backup tools).
4. **Infrastructure Logic:** If Infrastructure is "Low" or "Zero" and duration > 7 days, include sustainability items (repair kits, laundry solutions, extra batteries).
5. **Output Format:** Return a structured JSON with a "reasoning" field explaining how risks and duration influenced the final list.
""")