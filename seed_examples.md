# Seed Examples: Synthetic Travel & Mission-Prep Dataset

---

### Scenario 1: City Sightseeing — 7-Day Urban International

```json
{
  "input": {
    "intent": "City sightseeing",
    "duration": 7,
    "infrastructure": "Mixed — standard town",
    "climate": "Temperate (variable / four seasons)",
    "risks": ["Physical theft / pickpocketing", "Flash floods", "Food safety / contamination"],
    "max_items": 13
  },
  "output": [
    {"item": "T-Shirt / Casual Top", "quantity": 7, "reason": "One per day; hygiene baseline eliminates laundry dependency."},
    {"item": "Underwear", "quantity": 7, "reason": "Daily change; hygiene non-negotiable for 7-day window."},
    {"item": "Socks", "quantity": 8, "reason": "N+1 buffer covers wet feet or extended days."},
    {"item": "Pants / Jeans", "quantity": 2, "reason": "Two pairs cover day and evening role separation."},
    {"item": "Packable Rain Shell", "quantity": 1, "reason": "Mitigates flash flood and weather disruption risk."},
    {"item": "Walking Shoes", "quantity": 1, "reason": "Primary urban footwear; break in before departure."},
    {"item": "First Aid Kit (blister patches, bandages, antiseptic)", "quantity": 1, "reason": "Minor injuries common when pharmacy proximity uncertain."},
    {"item": "Anti-Diarrheal Medication", "quantity": 1, "reason": "Addresses food safety contamination risk in new environments."},
    {"item": "Sunscreen SPF 50", "quantity": 1, "reason": "UV risk increases during high-activity outdoor sightseeing."},
    {"item": "Hand Sanitizer", "quantity": 1, "reason": "Hygiene continuity in transit and street-food contexts."},
    {"item": "Phone + Charger", "quantity": 1, "reason": "Primary navigation and emergency contact device."},
    {"item": "Universal Power Adapter", "quantity": 1, "reason": "Eliminates grid incompatibility across international destinations."},
    {"item": "Travel Wallet (RFID-blocking)", "quantity": 1, "reason": "Centralized document security mitigates pickpocketing risk."}
  ]
}
```

---

### Scenario 2: City Sightseeing — 5-Day Carry-On Only

```json
{
  "input": {
    "intent": "City sightseeing",
    "duration": 5,
    "infrastructure": "Urban / Modern — full services",
    "climate": "Temperate (variable / four seasons)",
    "risks": ["Physical theft / pickpocketing", "Air pollution / smog", "Flash floods"],
    "max_items": 12
  },
  "output": [
    {"item": "Underwear", "quantity": 5, "reason": "One per day; daily change is hygiene baseline."},
    {"item": "Socks", "quantity": 5, "reason": "Daily change for high-step sightseeing comfort."},
    {"item": "Casual T-Shirt / Top", "quantity": 3, "reason": "Three tops for 5 days assumes one repeat wear."},
    {"item": "Dress Shirt / Smart Casual Top", "quantity": 1, "reason": "Covers semi-formal dinners without dedicated formal category."},
    {"item": "Pants / Jeans", "quantity": 2, "reason": "Two pairs separate casual and evening looks."},
    {"item": "Scarf / Light Wrap", "quantity": 1, "reason": "Counters thermal shock from extreme aircraft A/C."},
    {"item": "Walking Shoes", "quantity": 1, "reason": "Primary footwear for 5 high-mileage sightseeing days."},
    {"item": "Dress Shoes or Smart Sandals", "quantity": 1, "reason": "Evening and restaurant pairing for dressier outfit."},
    {"item": "Toiletries Kit", "quantity": 1, "reason": "Travel-size ≤100ml complies with carry-on liquid rules."},
    {"item": "Phone + Charger", "quantity": 1, "reason": "Navigation, translation, and emergency contact backbone."},
    {"item": "Portable Power Bank", "quantity": 1, "reason": "Extends phone runtime during long sightseeing days."},
    {"item": "Travel Wallet (RFID-blocking)", "quantity": 1, "reason": "RFID shielding prevents electronic pickpocketing in crowds."}
  ]
}
```

---

### Scenario 3: Volunteer Mission — 8-Day Tropical

```json
{
  "input": {
    "intent": "Volunteer mission",
    "duration": 8,
    "infrastructure": "Developing — inconsistent utilities",
    "climate": "Tropical rain (high humidity)",
    "risks": ["High humidity / mold", "Vector-borne disease (mosquitoes / ticks)", "Poor water quality"],
    "max_items": 13
  },
  "output": [
    {"item": "Merino Wool Socks", "quantity": 8, "reason": "Daily change; odor resistance critical in high humidity."},
    {"item": "Underwear", "quantity": 8, "reason": "One per day; quick-dry fabric for overnight washing."},
    {"item": "Quick-Dry Tops (vests, T-shirts, hiking shirts)", "quantity": 8, "reason": "One per day for all volunteer work contexts."},
    {"item": "Leggings / Cycle Shorts", "quantity": 1, "reason": "Athletic base for outdoor volunteer and hiking days."},
    {"item": "Jeans / Durable Trousers", "quantity": 1, "reason": "Social and travel-day bottom; air-dries between uses."},
    {"item": "Waterproof Raincoat", "quantity": 1, "reason": "Essential outer shell for tropical rain climate."},
    {"item": "Sandals / Flip-Flops", "quantity": 1, "reason": "Required for communal showers; prevents fungal infection."},
    {"item": "Walking / Tennis Shoes", "quantity": 1, "reason": "All-purpose footwear for urban and volunteer navigation."},
    {"item": "Microfiber Travel Towel", "quantity": 1, "reason": "Dries in under an hour; not always provided."},
    {"item": "Laundry Kit (solid detergent, color catchers)", "quantity": 1, "reason": "Enables sink washing when laundromat access fails."},
    {"item": "DEET Insect Repellent (30%+)", "quantity": 1, "reason": "Prevents vector-borne disease at dawn and dusk."},
    {"item": "Water Purification Tablets / Filter", "quantity": 1, "reason": "Directly mitigates poor water quality risk."},
    {"item": "Portable Battery Charger (10,000 mAh+)", "quantity": 1, "reason": "Sustains devices through inconsistent utility outages."}
  ]
}
```

---

### Scenario 4: Hiking / Trekking — 7-Day High Altitude

```json
{
  "input": {
    "intent": "Hiking / Trekking",
    "duration": 7,
    "infrastructure": "None — off-grid / wilderness",
    "climate": "High altitude (thin air / intense UV)",
    "risks": ["Altitude sickness", "Frostbite / hypothermia", "High UV exposure"],
    "max_items": 15
  },
  "output": [
    {"item": "Technical T-Shirts / Base Layer Tops", "quantity": 5, "reason": "N-2; planned rest-day laundry; quick-dry allows rewear."},
    {"item": "Moisture-Wicking Underwear", "quantity": 7, "reason": "Daily change prevents chafing on high-exertion days."},
    {"item": "Merino Wool Hiking Socks", "quantity": 8, "reason": "N+1 buffer for stream-crossing saturation events."},
    {"item": "Hiking / Convertible Pants", "quantity": 4, "reason": "N/2; zip-off design effectively doubles bottom count."},
    {"item": "Fleece Mid-Layer Jacket", "quantity": 1, "reason": "Insulating warmth at altitude without down weight."},
    {"item": "Waterproof Rain Jacket", "quantity": 1, "reason": "Hypothermia onset accelerates when wet at altitude."},
    {"item": "Rain Pants", "quantity": 1, "reason": "Full lower-body waterproofing on multi-day trail exposure."},
    {"item": "Waterproof Hiking Boots (ankle support)", "quantity": 1, "reason": "Ankle support is primary musculoskeletal injury mitigation."},
    {"item": "Camp Sandals", "quantity": 1, "reason": "Boot rest at camp prevents cumulative foot fatigue."},
    {"item": "Sunscreen SPF 50", "quantity": 1, "reason": "Intense UV at altitude demands daily full reapplication."},
    {"item": "Headlamp + Spare Batteries", "quantity": 1, "reason": "Primary light in off-grid terrain; batteries drain in cold."},
    {"item": "Water Purification Filter", "quantity": 1, "reason": "Removes dependency on carried water weight on trail."},
    {"item": "First Aid Kit (blister, ace bandage, anti-chafe)", "quantity": 1, "reason": "On-trail blister and joint management capability."},
    {"item": "Navigation (offline maps + compass)", "quantity": 1, "reason": "Redundant routing when phone battery or signal fails."},
    {"item": "Portable Power Bank (20,000 mAh)", "quantity": 1, "reason": "No grid charging; sustains devices over 7 days."}
  ]
}
```

---

### Scenario 5: City Sightseeing — 14-Day Summer Europe Group

```json
{
  "input": {
    "intent": "City sightseeing",
    "duration": 14,
    "infrastructure": "Urban / Modern — full services",
    "climate": "Mediterranean (dry summer / wet winter)",
    "risks": ["Physical theft / pickpocketing", "High UV exposure", "Seismic activity / earthquakes"],
    "max_items": 18
  },
  "output": [
    {"item": "Tops (lightweight, breathable)", "quantity": 5, "reason": "5-4-3-2-1 capsule; weekly laundry covers full trip."},
    {"item": "Bottoms (pants, skirts, shorts — neutral palette)", "quantity": 4, "reason": "Neutral palette maximizes cross-pairing with all tops."},
    {"item": "Dresses", "quantity": 2, "reason": "Covers casual sightseeing and evening dining looks."},
    {"item": "Shoes (sneakers, dressy sandals, flip-flops)", "quantity": 3, "reason": "Three pairs cover sightseeing, evenings, and pool."},
    {"item": "Accessories Set (jewelry, belt, hair ties)", "quantity": 1, "reason": "Minimal set transforms tops across outfit contexts."},
    {"item": "Underwear", "quantity": 14, "reason": "Daily change; capsule compression cannot reduce underwear."},
    {"item": "Socks", "quantity": 14, "reason": "Daily change critical for 15,000-step sightseeing days."},
    {"item": "Lightweight Sweater / Cardigan", "quantity": 1, "reason": "Mediterranean evenings drop 10-15°C from afternoon peak."},
    {"item": "Packable Rain Jacket", "quantity": 1, "reason": "Northern European legs carry high summer precipitation."},
    {"item": "Scarf / Pashmina", "quantity": 1, "reason": "Mandatory shoulder coverage at heritage and religious sites."},
    {"item": "Compact Crossbody Bag (internal zipper pocket)", "quantity": 1, "reason": "Valuables inaccessible during tourist-crowd pickpocketing attempts."},
    {"item": "Waterproof Daypack (20L)", "quantity": 1, "reason": "Day-trip loadout bag; waterproofing protects electronics from rain."},
    {"item": "Sunscreen SPF 50", "quantity": 2, "reason": "Two bottles needed for 14 days of Mediterranean UV."},
    {"item": "Electrolyte Packets", "quantity": 7, "reason": "Mitigates heat exhaustion risk on high-exertion days."},
    {"item": "OTC Medications Kit (ibuprofen, antihistamine, anti-diarrheal)", "quantity": 1, "reason": "Language barriers and closures may delay pharmacy access."},
    {"item": "Phone + Charger", "quantity": 1, "reason": "Digital ticketing backbone; mandatory for EU museum entry."},
    {"item": "Portable Power Bank", "quantity": 1, "reason": "Navigation and translation drain batteries on long days."},
    {"item": "Universal Power Adapter (EU)", "quantity": 1, "reason": "Multi-country circuit crosses Type C, F, and G standards."}
  ]
}
```

---

### Scenario 6: City Sightseeing — 10-Day European Fashion Trip

```json
{
  "input": {
    "intent": "City sightseeing",
    "duration": 10,
    "infrastructure": "Urban / Modern — full services",
    "climate": "Mediterranean (dry summer / wet winter)",
    "risks": ["High UV exposure", "Physical theft / pickpocketing", "Civil instability"],
    "max_items": 14
  },
  "output": [
    {"item": "Neutral Tops (linen, silk-feel, or jersey)", "quantity": 5, "reason": "Planned midpoint laundry; 5 tops cover both trip halves."},
    {"item": "Versatile Bottoms (wide-leg pants, midi skirt, tailored shorts)", "quantity": 3, "reason": "Three covers casual, smart-casual, and athleisure contexts."},
    {"item": "Dresses (day dress + smart evening dress)", "quantity": 2, "reason": "Eliminates pairing complexity on transition days."},
    {"item": "Blazer / Lightweight Structured Jacket", "quantity": 1, "reason": "Elevates casual tops to smart-casual standard."},
    {"item": "Packable Rain Mac / Trench", "quantity": 1, "reason": "Northern European unpredictability demands a weatherproof outer layer."},
    {"item": "Underwear", "quantity": 10, "reason": "Daily change; underwear cannot be compressed or re-worn."},
    {"item": "Socks (low-cut and liner styles)", "quantity": 10, "reason": "Daily change for blister prevention on high-mileage days."},
    {"item": "Walking Sneakers (white leather or minimalist)", "quantity": 1, "reason": "Style-compatible with dresses and all smart bottoms."},
    {"item": "Dressy Mule / Low Sandal", "quantity": 1, "reason": "Cobblestone-safe evening footwear with comfort heel."},
    {"item": "Crossbody Day Bag (anti-theft zipper)", "quantity": 1, "reason": "Internal zipper prevents opportunistic pickpocketing in queues."},
    {"item": "Scarf (silk or lightweight modal)", "quantity": 1, "reason": "Heritage site shoulder coverage and evening layering."},
    {"item": "Toiletries Kit (≤100ml per item)", "quantity": 1, "reason": "European budget carrier liquid rules enforce hard constraint."},
    {"item": "Sunscreen SPF 50 (50ml)", "quantity": 1, "reason": "Mediterranean UV requires daily protection for 10 days."},
    {"item": "Phone + Charging Cable", "quantity": 1, "reason": "Navigation, translation, and digital ticketing backbone."}
  ]
}
```

---

### Scenario 7: Camping / Backpacking — 7-Day Sub-Arctic Wilderness

```json
{
  "input": {
    "intent": "Camping / Backpacking",
    "duration": 7,
    "infrastructure": "None — off-grid / wilderness",
    "climate": "Arctic / Sub-zero cold",
    "risks": ["Frostbite / hypothermia", "Avalanche risk", "Communication barriers / no signal"],
    "max_items": 16
  },
  "output": [
    {"item": "4-Season Tent (freestanding, 60+ mph wind rated)", "quantity": 1, "reason": "Tent failure in remote wilderness is a life-safety event."},
    {"item": "Sleeping Bag (-10°C comfort rating)", "quantity": 1, "reason": "Highland overnight temps approach 0°C; thermal margin essential."},
    {"item": "Inflatable Sleeping Pad (R-value ≥ 4)", "quantity": 1, "reason": "Ground cold on Arctic terrain conducts heat rapidly."},
    {"item": "Merino Wool Base Layer Sets (top + bottom)", "quantity": 2, "reason": "Two sets; one worn while second dries."},
    {"item": "Fleece Mid-Layer Jacket", "quantity": 1, "reason": "Retains thermal properties when damp; critical in sustained rain."},
    {"item": "Waterproof Hardshell Jacket (20,000mm HH)", "quantity": 1, "reason": "Primary hypothermia prevention in sustained horizontal rain."},
    {"item": "Waterproof Hardshell Pants", "quantity": 1, "reason": "Wet legs at 0°C in wind cause rapid core loss."},
    {"item": "Merino Wool Mid-Layer Tops", "quantity": 4, "reason": "N/2 rewear supported by merino's odor resistance."},
    {"item": "Merino Wool Socks", "quantity": 8, "reason": "N+1; stream-crossing saturation requires mid-day change."},
    {"item": "Waterproof Hiking Boots (Vibram sole)", "quantity": 1, "reason": "Ankle support and waterproofing on lava and tundra terrain."},
    {"item": "Wool Beanie", "quantity": 2, "reason": "Two allow wet-and-dry rotation; wind loss is plausible."},
    {"item": "Waterproof Gloves (with liner)", "quantity": 1, "reason": "Cold dexterity loss prevents tent setup and stove operation."},
    {"item": "Camp Stove + Fuel Canisters (220g isobutane/propane)", "quantity": 4, "reason": "All cooking energy carried in zero-infrastructure wilderness."},
    {"item": "Water Filter / Purification Tablets", "quantity": 1, "reason": "Glacial streams may carry agricultural runoff and giardia."},
    {"item": "Navigation (offline GPS + paper topo + compass)", "quantity": 1, "reason": "No mobile signal; paper backup essential when battery fails cold."},
    {"item": "Portable Power Banks (10,000 mAh each)", "quantity": 2, "reason": "Cold reduces battery output; two banks in rotation."}
  ]
}
```

---

### Scenario 8: Wildlife Safari — 10-Day East Africa

```json
{
  "input": {
    "intent": "Wildlife safari",
    "duration": 10,
    "infrastructure": "Basic — rural / remote village",
    "climate": "Tropical rain (high humidity)",
    "risks": ["Vector-borne disease (mosquitoes / ticks)", "High UV exposure", "Poor water quality"],
    "max_items": 15
  },
  "output": [
    {"item": "Safari Shirts (neutral: khaki, tan, olive)", "quantity": 5, "reason": "N/2; camp laundry offered every two days."},
    {"item": "Long-Sleeved Shirts (neutral, lightweight)", "quantity": 3, "reason": "Physical barrier during dawn and dusk malaria-transmission windows."},
    {"item": "Convertible Safari Pants (zip-off)", "quantity": 2, "reason": "Zip-off doubles as pants and shorts in one weight."},
    {"item": "Fleece Jacket / Warm Sweater", "quantity": 2, "reason": "Morning drives 10-15°C; one worn, one dry at camp."},
    {"item": "Moisture-Wicking Underwear", "quantity": 10, "reason": "Daily change in tropical heat prevents fungal infection."},
    {"item": "Bug-Repellent Socks (permethrin-treated)", "quantity": 3, "reason": "Permethrin provides secondary ankle protection against vectors."},
    {"item": "Regular Hiking Socks", "quantity": 5, "reason": "N/2 rotation; 2-day wear cycle per pair."},
    {"item": "Wide-Brim Sun Hat", "quantity": 1, "reason": "Equatorial UV during 3-6 hour open-vehicle game sessions."},
    {"item": "Polarized Sunglasses", "quantity": 1, "reason": "Glare reduction enables wildlife spotting at water sources."},
    {"item": "Soft-Sided Duffel Bag (44L)", "quantity": 1, "reason": "Hard cases prohibited on bush aircraft."},
    {"item": "DEET Insect Repellent (30%+)", "quantity": 2, "reason": "Two bottles ensure reapplication every 4-6 hours outdoors."},
    {"item": "Sunscreen SPF 50", "quantity": 2, "reason": "Reapplication every 90 minutes under equatorial UV."},
    {"item": "Water Purification Filter", "quantity": 1, "reason": "Directly mitigates poor water quality in remote areas."},
    {"item": "Travel Medical Kit (rehydration salts, antiseptic, anti-diarrheal)", "quantity": 1, "reason": "No pharmacy in remote safari zone; self-treatment essential."},
    {"item": "Portable Power Bank (20,000 mAh)", "quantity": 1, "reason": "Generators run on scheduled evening windows only."}
  ]
}
```

---

### Scenario 9: Wildlife Safari — 7-Day Remote Luxury Bush

```json
{
  "input": {
    "intent": "Wildlife safari",
    "duration": 7,
    "infrastructure": "None — off-grid / wilderness",
    "climate": "Arid desert (dry heat)",
    "risks": ["High UV exposure", "Extreme wildlife encounters", "Communication barriers / no signal"],
    "max_items": 13
  },
  "output": [
    {"item": "Breathable Cotton Safari Shirts (neutral tones)", "quantity": 4, "reason": "N/2; daily camp laundry supports 2-day rotation."},
    {"item": "Long-Sleeved Protective Shirts", "quantity": 2, "reason": "Physical barrier at dawn and dusk drive windows."},
    {"item": "Safari Pants (neutral, lightweight)", "quantity": 2, "reason": "Alternating use-and-wash cycle with daily camp laundry."},
    {"item": "Warm Layers (fleece pullover + lightweight down gilet)", "quantity": 2, "reason": "25-30°C day-to-night swing demands two distinct mid-layers."},
    {"item": "Sun Hat (wide brim)", "quantity": 1, "reason": "Equatorial UV unfiltered at altitude on open vehicles."},
    {"item": "Polarized Sunglasses", "quantity": 1, "reason": "Glare reduction for spotting wildlife on dry pans."},
    {"item": "Closed-Toe Shoes (lightweight hiking)", "quantity": 1, "reason": "Snake, scorpion, and thorn protection on bush walks."},
    {"item": "Soft-Sided Duffel Bag (≤18kg)", "quantity": 1, "reason": "Hard cases not permitted on light bush aircraft."},
    {"item": "Camera + Extra Batteries + Memory Cards", "quantity": 1, "reason": "Cold drain; spare batteries essential for game-drive photography."},
    {"item": "DEET Insect Repellent (30%+)", "quantity": 2, "reason": "Two bottles sustain reapplication protocol for 7 days."},
    {"item": "Sunscreen SPF 50", "quantity": 2, "reason": "Equatorial UV demands reapplication every 90 minutes."},
    {"item": "Medical Kit (antihistamine, antiseptic, anti-diarrheal, bite relief)", "quantity": 1, "reason": "No pharmacy within medevac range; minor conditions escalate."},
    {"item": "Portable Power Bank", "quantity": 1, "reason": "Generator windows insufficient for full device charge overnight."}
  ]
}
```
