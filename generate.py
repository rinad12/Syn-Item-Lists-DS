"""Generate synthetic packing-list dataset using Google Gemini."""

import argparse
import json
import math
import random
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv
from jinja2 import Template
from tqdm import tqdm
import os

load_dotenv()

INTENTS = [
    "Beach vacation",
    "Camping / Backpacking",
    "Business trip",
    "City sightseeing",
    "Hiking / Trekking",
    "Ski / Snowboard",
    "Road trip",
    "Volunteer mission",
    "Extreme tourism",
    "Scientific research expedition",
    "Digital nomad relocation",
    "Humanitarian aid mission",
    "Photography expedition",
    "Spiritual pilgrimage",
    "Competitive sports event",
    "Formal event / Destination wedding",
    "Medical tourism",
    "Language immersion program",
    "Culinary tourism",
    "Wildlife safari",
    "Festival attendance",
    "Academic / Study abroad",
]

INFRASTRUCTURES = [
    "None — off-grid / wilderness",
    "Basic — rural / remote village",
    "Developing — inconsistent utilities",
    "Mixed — standard town",
    "Urban / Modern — full services",
    "Industrial / Work site",
    "Resort / Managed environment",
    "Marine / Live-aboard boat",
    "Underground / Cave system",
    "High-altitude research station",
    "Temporary field camp",
    "Luxury / All-inclusive resort",
]

CLIMATES = [
    "Tropical rain (high humidity)",
    "Arid desert (dry heat)",
    "Arctic / Sub-zero cold",
    "High altitude (thin air / intense UV)",
    "Temperate (variable / four seasons)",
    "Mediterranean (dry summer / wet winter)",
    "Maritime (high wind / salt spray)",
    "Monsoonal (seasonal heavy rain)",
    "Subpolar / Tundra",
    "Subtropical (hot humid summer)",
    "Continental (extreme seasonal swings)",
    "Coastal fog / marine layer",
    "Volcanic / geothermal zone",
    "Equatorial rainforest (dense canopy)",
]

RISKS = [
    "High humidity / mold",
    "Dust & sandstorms",
    "Poor water quality",
    "Power instability",
    "Vector-borne disease (mosquitoes / ticks)",
    "High UV exposure",
    "Physical theft / pickpocketing",
    "Civil instability",
    "Extreme wildlife encounters",
    "Air pollution / smog",
    "Seismic activity / earthquakes",
    "Flash floods",
    "Avalanche risk",
    "Jellyfish / marine hazards",
    "Altitude sickness",
    "Frostbite / hypothermia",
    "Food safety / contamination",
    "Communication barriers / no signal",
]

PROMPT_TEMPLATE = Template("""\
Role: Expert Logistics Officer.
Task: Create a highly precise, context-aware packing list.

Context:
- Intent: {{ intent }}
- Duration: {{ duration }} days
- Infrastructure Level: {{ infrastructure }}
- Climate: {{ climate }}
- Risk Factors:
{% for risk in risks %}  * {{ risk }}
{% endfor %}
Requirements:
1. **Adaptive Scaling:** Calculate quantities strictly based on the {{ duration }}-day duration. Use logical formulas (N or N+1) for daily essentials.
2. **Risk Mitigation:** For every risk factor listed, include at least one specific item addressing it.
3. **Compound Threats:** If multiple risks overlap, prioritize items that address both simultaneously.
4. **Infrastructure Logic:** If infrastructure is off-grid or basic and duration > 7 days, include sustainability items (repair kits, laundry solutions, extra batteries).
5. **Output Format:** Return a JSON object with two keys:
   - "reasoning": 2–3 sentences explaining how risks, climate, and duration shaped the list
   - "packing_list": object whose keys are category names and values are arrays of specific items with quantities
""")

