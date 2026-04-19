# Seed Examples: Synthetic Travel & Mission-Prep Dataset

---

### Scenario 1: General International Leisure Travel

```json
{
  "intent": "Leisure",
  "duration": 7,
  "infrastructure": "Medium",
  "risks": ["Petty Theft", "Weather Variability", "Medical Access Gap Abroad"],
  "reasoning_summary": "Urban international travel with hotel infrastructure demands a balanced kit that covers daily clothing rotation, health contingencies, and secure document management. Medium infrastructure assumes reliable grid power and pharmacy access, but not necessarily proximity to specialized medical care. Neutral footwear and a layering system handle climate variability without excess weight.",
  "items": [
    {
      "item": "T-Shirt / Casual Top",
      "quantity": 7,
      "formula": "N",
      "reason": "One top per day is the professional baseline for hygiene and comfort; eliminates dependency on laundry access during the trip window."
    },
    {
      "item": "Underwear",
      "quantity": 7,
      "formula": "N",
      "reason": "Daily change is a hygiene non-negotiable; merino or synthetic fabrics recommended for fast hand-washing if needed."
    },
    {
      "item": "Socks",
      "quantity": 8,
      "formula": "N+1",
      "reason": "The +1 buffer covers unexpected weather (wet feet) or extended travel days that require a mid-day change."
    },
    {
      "item": "Pants / Jeans",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Bottoms air-dry and can be worn multiple times; two pairs cover day/evening role separation without excess weight."
    },
    {
      "item": "Lightweight Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Handles mild cold snaps and over-air-conditioned transit environments; doubles as a mid-layer under a shell."
    },
    {
      "item": "Raincoat / Packable Shell",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Weather variability risk mitigation; a packable shell adds negligible weight but prevents itinerary disruption from rain."
    },
    {
      "item": "Walking Shoes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary footwear for urban exploration; should be broken in before departure to prevent blister-related mobility loss."
    },
    {
      "item": "Sandals or Slip-ons",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Required for hostel/hotel common areas and casual evenings; reduces wear on primary shoes."
    },
    {
      "item": "Swimsuit",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hotel pool and beach access; quick-dry fabric means it does not occupy dedicated bag volume after day one."
    },
    {
      "item": "First Aid Kit (blister patches, bandages, antiseptic)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Addresses the medical access gap risk; minor injuries during high-activity sightseeing days are common and pharmacy proximity cannot be guaranteed."
    },
    {
      "item": "Pain Reliever (ibuprofen / paracetamol)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Jet lag, headaches, and minor musculoskeletal strain are endemic to travel; OTC access may be complicated by language barriers abroad."
    },
    {
      "item": "Anti-diarrheal Medication",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Dietary exposure in new environments carries a measurable GI disruption risk; one course is standard travel-medicine protocol."
    },
    {
      "item": "Sunscreen (SPF 50)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "UV exposure increases significantly during high-activity outdoor days; prevents sunburn-related fatigue that degrades trip performance."
    },
    {
      "item": "Insect Repellent",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Included as a precaution against destination-specific vector risks; required in tropical or subtropical itineraries regardless of infrastructure level."
    },
    {
      "item": "Hand Sanitizer",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hygiene continuity in transit environments (airports, public transport) where hand-washing facilities are inconsistent."
    },
    {
      "item": "Toothbrush + Toothpaste",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Non-negotiable hygiene baseline; travel-size toothpaste complies with carry-on liquid restrictions."
    },
    {
      "item": "Deodorant",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Solid stick preferred for carry-on compliance; single unit covers full 7-day duration."
    },
    {
      "item": "Phone + Charger",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary navigation, communication, and emergency contact device; charger is a single-point-of-failure item."
    },
    {
      "item": "Universal Power Adapter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Eliminates grid incompatibility risk across international destinations; a single multi-region adapter covers most travel corridors."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Extends phone operational time during long sightseeing days when outlet access is unavailable."
    },
    {
      "item": "Travel Wallet (passport, cards, emergency info)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Centralized secure document management mitigates petty theft risk; RFID-blocking versions recommended for urban environments."
    },
    {
      "item": "Packing Cubes",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Compression and organization system reduces packing time and prevents bag disorganization during multi-city itineraries."
    },
    {
      "item": "Reusable Water Bottle",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hydration consistency across sightseeing days; eliminates single-use plastic dependency and reduces daily expenses."
    },
    {
      "item": "Travel Pillow",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Long-haul transit recovery tool; addresses jet lag risk by enabling sleep during flight without neck strain."
    },
    {
      "item": "Eye Mask + Earplugs",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Sleep quality in unfamiliar hotel environments; critical for circadian reset after long-haul flights crossing multiple time zones."
    }
  ]
}
```

---

### Scenario 2: Short-Haul Leisure (Carry-On Only)

```json
{
  "intent": "Leisure",
  "duration": 5,
  "infrastructure": "High",
  "risks": ["Baggage Loss", "Long-Haul Seat Discomfort", "Thermal Shock (Extreme A/C Environments)"],
  "reasoning_summary": "A 3–5-day carry-on-only strategy for high-infrastructure destinations (domestic US, Western Europe) where laundry access is unlikely but pharmacies and stores are accessible. The primary risk is baggage loss, making carry-on compliance critical. The kit is calibrated to cover daily basics without checked luggage, using the source's 1-pair-per-day underwear/sock protocol and 1–2-outfit guidance for dressier/casual categories.",
  "items": [
    {
      "item": "Underwear",
      "quantity": 5,
      "formula": "N",
      "reason": "Source explicitly states 1 pair daily for 3–5-day trips; daily change is a hygiene baseline that cannot be compressed further without laundry access."
    },
    {
      "item": "Socks",
      "quantity": 5,
      "formula": "N",
      "reason": "1 pair per day per source guidance; athletic or wool-blend socks recommended for all-day walking without moisture buildup."
    },
    {
      "item": "Casual T-Shirt / Top",
      "quantity": 3,
      "formula": "N-2",
      "reason": "Source recommends 1–2 casual outfits for 3–5 days; 3 tops for 5 days assumes one repeat wear on shorter days, reducing pack volume."
    },
    {
      "item": "Dress Shirt / Smart Casual Top",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source recommends 1 dressier outfit for short trips; covers restaurant dinners and any semi-formal obligations without a dedicated formal category."
    },
    {
      "item": "Pants / Jeans",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Source recommends 1–2 pairs for short trips; two bottoms cover casual days and one smarter evening look."
    },
    {
      "item": "Pajamas / Sleepwear",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies 1 pair for 3–5-day trips; a lightweight option doubles as lounge wear and does not require daily washing."
    },
    {
      "item": "Walking / Leisure Shoes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary footwear covering daily sightseeing and casual dining; source recommends 1–2 pairs for short trips."
    },
    {
      "item": "Dress Shoes or Smart Sandals",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Covers the dressier outfit pairing; versatile enough for evening outings without adding significant weight."
    },
    {
      "item": "Toiletries Kit (toothbrush, paste, deodorant, cleanser, lotion)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "All items in travel-size (≤100ml) for carry-on compliance; high-infrastructure destination means forgotten items can be purchased, reducing packing anxiety."
    },
    {
      "item": "Prescription Medications",
      "quantity": 5,
      "formula": "N",
      "reason": "Exact daily doses for trip duration; carry-on placement is mandatory to prevent total loss in a checked-bag-loss scenario."
    },
    {
      "item": "OTC Pain Reliever",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Travel fatigue and headache management; high infrastructure means pharmacies are accessible but mid-trip purchases waste time."
    },
    {
      "item": "Hand Sanitizer",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hygiene continuity in transit environments (airports, public transport) between reliable hand-washing facilities."
    },
    {
      "item": "Disinfecting Wipes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Tray table and seat surface decontamination on aircraft; standard in-flight hygiene protocol."
    },
    {
      "item": "Phone + Charger",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary navigation and communication device; charger is a single point of failure — loss renders the phone useless by day 2."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Extends device runtime during long sightseeing days; mitigates thermal shock risk by enabling temperature/weather app access throughout."
    },
    {
      "item": "Power Adapter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Required for international destinations; single multi-region adapter covers Western Europe and most high-infrastructure travel corridors."
    },
    {
      "item": "Travel Pillow",
      "quantity": 1,
      "formula": "Constant",
      "reason": "In-flight comfort for long-haul legs; directly mitigates seat discomfort risk and enables rest that preserves day-one operational capacity."
    },
    {
      "item": "Eye Mask",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Light management for in-flight sleep; paired with earplugs creates a sleep-conducive micro-environment independent of cabin conditions."
    },
    {
      "item": "Earplugs",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Noise reduction for in-flight rest; doubles as a hotel sleep aid in urban environments with street noise."
    },
    {
      "item": "Scarf / Light Wrap",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Directly counters thermal shock risk from extreme aircraft/hotel A/C; doubles as a blanket in-flight and a light layer during cooler evenings."
    },
    {
      "item": "Travel Wallet (passport, ID, cards, cash, emergency contacts)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Secure document consolidation; RFID protection recommended in high-traffic tourist areas."
    },
    {
      "item": "Change of Clothes (in carry-on)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Directly mitigates baggage loss risk; one full outfit in the personal item ensures operational continuity on arrival even if checked luggage is delayed or lost."
    }
  ]
}
```

---

### Scenario 3: Long-Term Budget Volunteer Travel (Cabin-Bag Only)

```json
{
  "intent": "Volunteer",
  "duration": 8,
  "infrastructure": "Low",
  "risks": ["Hostel Theft", "Laundry Access Uncertainty", "Multi-Climate Transitions"],
  "reasoning_summary": "Rebecca's Workaway protocol is calibrated for indefinite multi-country volunteer travel using a single carry-on cabin bag — a strategy that eliminates checked-luggage fees and forces deliberate item selection. The 8-day supply (7-day target + 1 buffer) is the loadout before the first reliable laundry opportunity is expected. Low infrastructure assumes hostels and volunteer placements with inconsistent laundry access. Merino wool is the material default throughout for odor resistance and temperature range. Anti-theft hardware (padlocks) is treated as a first-class kit category.",
  "items": [
    {
      "item": "Merino Wool Socks",
      "quantity": 8,
      "formula": "N",
      "reason": "Source explicitly specifies 8 socks for an 8-day supply; merino's natural odor resistance extends rewear life but the protocol assumes daily changes for foot hygiene on high-activity volunteer days."
    },
    {
      "item": "Underwear",
      "quantity": 8,
      "formula": "N",
      "reason": "One per day for the full 8-day window; quick-dry synthetic or merino fabric recommended for overnight hand-washing in hostel sinks."
    },
    {
      "item": "Tops (vests, T-shirts, hiking shirts)",
      "quantity": 8,
      "formula": "N",
      "reason": "Source directly states '8 tops for 8 days'; the variety of styles (vest, T-shirt, hiking shirt) ensures social, casual, and physical-work contexts are all covered."
    },
    {
      "item": "Bras (including sports bra)",
      "quantity": 4,
      "formula": "N/2",
      "reason": "Source specifies 4 bras for an 8-day window; the N/2 formula reflects the practical rotation — bras are air-dried overnight rather than replaced daily."
    },
    {
      "item": "Pajamas / Sleepwear",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Single lightweight set doubles as hostel lounge wear; required for shared dormitory environments where street clothes are socially inappropriate."
    },
    {
      "item": "Swimsuit",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Multi-purpose: beach access, hostel pool, and unexpected opportunity swim; quick-dry material means it packs without dedicated dry space."
    },
    {
      "item": "Leggings / Cycle Shorts",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Athletic base layer for outdoor volunteer work and hiking days; compresses flat in packing cubes."
    },
    {
      "item": "Jeans / Durable Trousers",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Social and travel-day wear; a single pair is viable given air-drying between uses and serves as the 'smart casual' anchor of the wardrobe."
    },
    {
      "item": "Dress / Jumpsuit",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Single versatile dressy item covers cultural site visits, evenings out, and volunteer host dinners without a separate formal category."
    },
    {
      "item": "Cardigan",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Light layering piece that elevates casual tops for colder evenings or air-conditioned transit; non-negotiable for multi-climate transitions."
    },
    {
      "item": "Sweater / Fleece",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Mid-layer for cold-climate legs of a multi-country trip; fleece packs smaller than wool and dries faster after hostel washing."
    },
    {
      "item": "Packable Down Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Compresses to fist-sized volume while covering the cold end of multi-climate transitions; source specifically calls out this item by type."
    },
    {
      "item": "Waterproof Raincoat (GORE-TEX or equivalent)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly recommends GORE-TEX; the outer shell must be waterproof — not just water-resistant — because volunteer placements may require outdoor work regardless of weather."
    },
    {
      "item": "Sandals / Flip-Flops",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Required for hostel communal showers to prevent fungal infection; doubles as warm-weather casual footwear."
    },
    {
      "item": "Walking / Tennis Shoes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "All-purpose footwear for daily urban and light-trail navigation."
    },
    {
      "item": "Waterproof Hiking Boots",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Required for volunteer placements involving outdoor labor or trail-based travel; ankle support and waterproofing are critical for low-infrastructure terrain."
    },
    {
      "item": "Microfiber Travel Towel",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hostels frequently charge for towel rental or do not provide them; a microfiber towel dries in under an hour, essential under laundry access uncertainty risk."
    },
    {
      "item": "Padlocks (various shackle sizes)",
      "quantity": 4,
      "formula": "Constant",
      "reason": "Source specifies 4 locks; covers hostel dorm locker, bag zipper pulls (x2 deterrent), and luggage lock — directly mitigates the hostel theft risk."
    },
    {
      "item": "Packing Cubes",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Compression system for cabin-bag-only strategy; essential for maintaining organised access to all 8 days of clothing without unpacking."
    },
    {
      "item": "Dry Bag",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Waterproof protection for electronics and documents during water-based activities or unexpected rain; critical when bag lacks weatherproofing."
    },
    {
      "item": "Laundry Kit (bag, detergent pods, stain remover, color catchers)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Directly addresses laundry access uncertainty risk; solid detergent pods and color catchers enable reliable sink washing when laundromat access fails."
    },
    {
      "item": "Portable Battery Charger (10,000 mAh+)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Low-infrastructure placements may lack outlet access; a high-capacity power bank sustains phone and camera operations across multiple days."
    },
    {
      "item": "Universal Travel Adapter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Multi-country volunteer travel crosses multiple electrical standards; one multi-region adapter eliminates per-country adapter purchasing."
    },
    {
      "item": "Travel Wallet (passport, visa copies, vaccination printout, spare ID photos)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly specifies spare passport photos — critical for visa-on-arrival and emergency travel document replacement in low-infrastructure countries."
    },
    {
      "item": "Mirrorless Camera + SD Cards + Charging Cable",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Volunteer experience documentation; SD card redundancy (minimum 2) prevents complete loss of mission records from a single card failure."
    }
  ]
}
```

---

### Scenario 4: Adventure & Outdoor Travel

```json
{
  "intent": "Leisure",
  "duration": 7,
  "infrastructure": "Low",
  "risks": ["Variable Weather & Flash Conditions", "Physical Exertion & Musculoskeletal Injury", "Navigation Failure in Remote Terrain"],
  "reasoning_summary": "OutdoorGearLab's protocol targets multi-activity adventure travelers (hiking, kayaking, cycling) operating in low-infrastructure environments where resupply is unlikely. Clothing assumes quick-dry technical fabrics that tolerate physical stress and can be reworn; source recommends 5–6 tops for 7 days (N-1 to N-2), reflecting the expectation of light field-laundry on rest days. Footwear, navigation, and safety gear are treated as critical-path items with zero redundancy tolerance.",
  "items": [
    {
      "item": "Technical T-Shirts / Base Layer Tops",
      "quantity": 5,
      "formula": "N-2",
      "reason": "Source recommends 5–6 tops for a 1-week trip; the N-2 formula accounts for planned rest-day laundry and quick-dry fabric rewear, avoiding the weight of full N coverage."
    },
    {
      "item": "Underwear (moisture-wicking)",
      "quantity": 7,
      "formula": "N",
      "reason": "Source specifies 'at least one change of underclothes for every day'; moisture-wicking fabric is critical for multi-day physical exertion to prevent chafing and fungal conditions."
    },
    {
      "item": "Socks (merino or synthetic hiking)",
      "quantity": 8,
      "formula": "N+1",
      "reason": "Hiking socks require daily change to manage moisture and prevent blisters; the +1 buffer covers stream crossings or rain events that saturate footwear mid-day."
    },
    {
      "item": "Hiking / Convertible Pants",
      "quantity": 4,
      "formula": "N/2",
      "reason": "Source recommends 3–4 bottoms for a 1-week trip; 4 pairs for 7 days reflects that bottoms can be worn 2 days each with a planned wash, while convertible zip-off design doubles bottom count effectively."
    },
    {
      "item": "Fleece Sweater / Insulating Mid-Layer",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Variable weather risk mitigation; a fleece mid-layer traps warmth at elevation or during cold morning starts without the weight of a down jacket."
    },
    {
      "item": "Waterproof Rain Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hard shell is non-negotiable for variable weather in low-infrastructure terrain; hypothermia onset accelerates when wet and no shelter is accessible."
    },
    {
      "item": "Rain Pants",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Full lower-body waterproofing required for multi-day outdoor exposure; prevents the core temperature loss that rain-soaked pants cause on extended trail days."
    },
    {
      "item": "Hiking Boots (waterproof, ankle support)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Ankle support is the primary mitigation for musculoskeletal injury risk on uneven terrain; waterproofing enables crossing wet ground without stopping to change footwear."
    },
    {
      "item": "Camp Sandals / Lightweight Shoes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Boot rest at campsite prevents cumulative foot fatigue; lightweight shoes serve as backup footwear if hiking boots become saturated."
    },
    {
      "item": "Sun Hat with Brim",
      "quantity": 1,
      "formula": "Constant",
      "reason": "UV protection for extended exposed outdoor hours; wide brim provides neck and face coverage that sunscreen alone cannot sustain on multi-day trips."
    },
    {
      "item": "Sunglasses (polarized)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Mandatory for water and snowfield environments where reflected UV doubles radiation exposure; polarization reduces navigational distraction from glare."
    },
    {
      "item": "Headlamp + Spare Batteries",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Low-infrastructure terrain at night creates navigation failure and safety risk; a headlamp with spare batteries is the primary light source with zero fallback."
    },
    {
      "item": "Water Purification Bottle / Filter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Direct mitigation for waterborne disease risk in low-infrastructure areas; a filter bottle removes dependency on carried water weight for sources encountered on trail."
    },
    {
      "item": "Binoculars",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Navigation and wildlife assessment at distance; allows safe route evaluation before committing to a descent or stream crossing."
    },
    {
      "item": "Dry Bag",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Electronics and documents waterproofing during water-based activities; a failed dry-bag seal can permanently destroy navigational tools in a single crossing event."
    },
    {
      "item": "First Aid Kit (blister kit, ace bandage, antiseptic, anti-chafe balm)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Musculoskeletal injury risk requires on-trail treatment capability; blister management and joint wrapping are the most common interventions on 7-day outdoor itineraries."
    },
    {
      "item": "Sunscreen (SPF 50, reef-safe)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Multi-day alpine and coastal environments produce cumulative UV exposure that exceeds single-day urban norms; reapplication protocol requires adequate volume for N days."
    },
    {
      "item": "Insect Repellent (DEET 30%)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Low-infrastructure outdoor environments carry vector-borne disease risk (Lyme, West Nile, dengue depending on region); DEET concentration above 20% provides all-day protection."
    },
    {
      "item": "Navigation (offline maps + compass)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Directly mitigates navigation failure risk; digital offline maps and a physical compass provide redundant routing capability when phone battery fails or signal is absent."
    },
    {
      "item": "Packable Daypack (20–25L)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Separates day-use loadout from base camp gear; reduces physical exertion burden on non-technical hiking days while keeping critical items accessible."
    },
    {
      "item": "Phone + Charger",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary communication and SOS device in low-infrastructure areas; pre-loaded with offline maps, first aid guides, and emergency contact information."
    },
    {
      "item": "Portable Power Bank (20,000 mAh)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "No grid charging in low-infrastructure terrain; a high-capacity bank sustains phone and headlamp battery charging across a 7-day window without resupply."
    },
    {
      "item": "Combination Lock",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hostel or guesthouse storage security during day trips when all gear cannot be carried on trail."
    },
    {
      "item": "Laundry Kit (dry bag soap, clothesline)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Enables field-washing of technical fabrics on rest days, supporting the N-2 clothing formula without requiring laundromat access."
    }
  ]
}
```

---

### Scenario 5: Summer Europe Group Travel (Capsule Wardrobe)

```json
{
  "intent": "Leisure",
  "duration": 14,
  "infrastructure": "High",
  "risks": ["Pickpocketing & Tourist-Targeted Theft", "Heat Exhaustion (Mediterranean Summer)", "Dress Code Denial at Cultural Sites"],
  "reasoning_summary": "Under30Experiences targets group leisure travelers doing a multi-city European summer circuit. High infrastructure (hotels, Airbnb, laundromats in every city) allows a structured capsule wardrobe approach using the 5-4-3-2-1 method, where clothing is constant (not duration-scaled) because laundry is planned weekly. The primary operational risks are petty theft in tourist areas, heat exhaustion during peak Mediterranean summer, and cultural site dress code non-compliance. Safety accessories (crossbody bag, door lock, portable alarm) are treated as mission-critical items.",
  "items": [
    {
      "item": "Tops (lightweight, breathable — shirts, blouses, tank tops)",
      "quantity": 5,
      "formula": "Constant",
      "reason": "Source's 5-4-3-2-1 capsule method specifies 5 tops for 14 days; with weekly laundry access, this covers the full trip across multiple outfit combinations without re-wearing the same look consecutively."
    },
    {
      "item": "Bottoms (pants, skirts, shorts — neutral palette)",
      "quantity": 4,
      "formula": "Constant",
      "reason": "Source specifies 4 bottoms in the capsule system; neutral colors (linen, khaki) maximize cross-pairing with tops while managing heat exhaustion risk through breathable fabrics."
    },
    {
      "item": "Dresses",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Source specifies 2 dresses; doubles as both casual sightseeing and evening dining wear, reducing the need for dedicated 'going out' items."
    },
    {
      "item": "Shoes (walking sneakers, dressy sandals, flip-flops)",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Source specifies 3 pairs; sneakers for high-mileage sightseeing days (15,000+ steps is typical on European city itineraries), sandals for evenings, flip-flops for hostel/pool use."
    },
    {
      "item": "Accessories Set (jewelry, belt, hair ties)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies 1 accessory set; a curated minimal set transforms the same tops across multiple outfit contexts without added weight."
    },
    {
      "item": "Underwear",
      "quantity": 14,
      "formula": "N",
      "reason": "Even with capsule wardrobe compression applied to all other categories, underwear requires a daily change — 14 pairs for 14 days is the hygienic baseline."
    },
    {
      "item": "Socks",
      "quantity": 14,
      "formula": "N",
      "reason": "Daily change required for high-step-count sightseeing days; foot health maintenance is critical for a 14-day itinerary where blister onset would compromise mobility."
    },
    {
      "item": "Lightweight Sweater / Cardigan",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Evening temperatures in Mediterranean Europe drop 10–15°C from the daytime peak; a layering piece prevents heat exhaustion recovery from being interrupted by cold."
    },
    {
      "item": "Packable Rain Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Northern European legs (Paris, Amsterdam, London) carry high precipitation probability even in summer; a packable shell adds minimal weight and prevents full-day itinerary disruption."
    },
    {
      "item": "Scarf / Pashmina",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Directly mitigates dress code denial risk; required for Vatican, mosques, and many cathedral entries where bare shoulders are prohibited — the most frequently missed access requirement by leisure travelers."
    },
    {
      "item": "Compact Crossbody Bag (with internal zipper pocket)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies internal zipper pockets as a mandatory feature; directly mitigates pickpocketing risk by keeping valuables inaccessible during high-density tourist crowd navigation."
    },
    {
      "item": "Waterproof Daypack (20L)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Day-trip loadout bag for museum visits and excursions; waterproofing protects electronics from unexpected rain events."
    },
    {
      "item": "Portable Door Lock",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly recommends; Airbnb and budget hotel door security is inconsistent — a portable lock adds a physical barrier independent of the room's native hardware."
    },
    {
      "item": "Sunscreen (SPF 50)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Heat exhaustion risk requires aggressive UV management; two bottles for 14 days ensures sufficient reapplication volume for full-day outdoor exposure in Mediterranean latitudes."
    },
    {
      "item": "Electrolyte Packets",
      "quantity": 7,
      "formula": "N/2",
      "reason": "Directly mitigates heat exhaustion risk; electrolyte replacement is recommended on high-exertion sightseeing days (>15,000 steps) in temperatures above 30°C."
    },
    {
      "item": "Hand Sanitizer",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hygiene continuity across high-traffic tourist environments and street food consumption; reduces GI disruption risk."
    },
    {
      "item": "OTC Medications Kit (ibuprofen, antihistamine, anti-diarrheal, band-aids)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "High infrastructure allows pharmacy access but language barriers and holiday closures can delay procurement; a self-contained OTC kit eliminates dependency."
    },
    {
      "item": "Phone + Charger",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary navigation, translation, and emergency contact device; app-based ticketing for European museums and transit is increasingly mandatory."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Long sightseeing days without outlet access deplete phone batteries; navigation and translation apps are battery-intensive."
    },
    {
      "item": "Universal Power Adapter (EU standard + USB-A/C)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Multi-country Europe circuit crosses Type C, F, G, and L socket standards; a single universal adapter eliminates per-country purchasing."
    },
    {
      "item": "Passport + Copies + Travel Insurance Docs",
      "quantity": 1,
      "formula": "Constant",
      "reason": "EU Schengen area entry requirements and ETA approvals (UK post-Brexit) require physical and digital documentation; copies stored separately from originals mitigate total document loss."
    },
    {
      "item": "AirTag (for checked luggage)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifically calls out luggage tracking; provides real-time location visibility during multi-city rail and flight legs where checked bag misdirection is most common."
    }
  ]
}
```

---

### Scenario 6: European Fashion Leisure Trip (Versatile Capsule)

```json
{
  "intent": "Leisure",
  "duration": 10,
  "infrastructure": "High",
  "risks": ["Airline Carry-On Weight Limits", "Dress Code Non-Compliance at Heritage Sites", "Unexpected Weather Shifts"],
  "reasoning_summary": "A 10-day fashion-conscious Europe trip strategy optimized for neutral-palette capsule dressing where every item cross-pairs with at least two others. The primary operational constraint is airline carry-on weight limits (typically 7–10kg on European budget carriers), which forces a hard ceiling on total item count. Clothing quantities are driven by a laundry-at-midpoint assumption (day 5), so tops use N/2 while underwear follows full N. Footwear follows the three-function rule: walk, walk-and-look-smart, and recover.",
  "items": [
    {
      "item": "Neutral Tops (linen, silk-feel, or jersey)",
      "quantity": 5,
      "formula": "N/2",
      "reason": "10-day trip with planned midpoint laundry; 5 tops covers days 1–5 and repeats washed items for days 6–10 — neutral palette ensures all tops cross-pair with all bottoms."
    },
    {
      "item": "Versatile Bottoms (wide-leg pants, midi skirt, tailored shorts)",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Three bottoms — one casual, one smart-casual, one athleisure — cover the full spectrum from heritage site visits to evening restaurants; re-wear is planned and neutral palette minimizes visual repetition."
    },
    {
      "item": "Dresses (day dress + smart evening dress)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Two dresses eliminate the need for outfit pairing on transition days; a lightweight day dress doubles as a beach cover-up and a smart dress replaces the need for a separate formal outfit."
    },
    {
      "item": "Blazer / Lightweight Structured Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Elevates casual tops to smart-casual standard for fine dining and cultural institution visits; mitigates dress code risk as an alternative to carrying a separate formal outfit."
    },
    {
      "item": "Packable Rain Mac / Trench",
      "quantity": 1,
      "formula": "Constant",
      "reason": "European weather unpredictability (particularly UK, Northern France, Low Countries) demands a weatherproof outer layer that still satisfies the trip's aesthetic criteria."
    },
    {
      "item": "Underwear",
      "quantity": 10,
      "formula": "N",
      "reason": "Daily change is non-negotiable for a 10-day trip; underwear does not benefit from the capsule/re-wear model applied to outer clothing."
    },
    {
      "item": "Socks (low-cut and liner styles)",
      "quantity": 10,
      "formula": "N",
      "reason": "Daily change required for blister prevention on high-mileage sightseeing days; invisible liner socks allow sandals and loafers to be worn sockless-looking without foot hygiene compromise."
    },
    {
      "item": "Walking Sneakers (white leather or minimalist)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary footwear for the majority of day hours; must be style-compatible with dresses and smart bottoms to avoid a dedicated 'city' shoe category."
    },
    {
      "item": "Dressy Mule / Low Sandal",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Evening and restaurant footwear; closed heel and low block heel provide comfort for cobblestone navigation without sacrificing the smart-casual look."
    },
    {
      "item": "Crossbody Day Bag (anti-theft zipper)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Security-forward bag design for high-density tourist environments; internal zipper pockets required to prevent opportunistic pickpocketing in queues and public transit."
    },
    {
      "item": "Foldable Tote Bag",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Carry-on overflow and market shopping bag; compresses to pocket-sized when empty, adding utility without dedicated packing volume."
    },
    {
      "item": "Scarf (silk or lightweight modal)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Dual function: heritage site dress code compliance (shoulder and head coverage) and evening layering; a scarf is the most weight-efficient multi-use item in the European travel kit."
    },
    {
      "item": "Toiletries Kit (travel-size, ≤100ml each)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "European budget carrier liquid restrictions (1L bag, ≤100ml per item) enforce a hard constraint; all liquids must be decanted to travel sizes before departure."
    },
    {
      "item": "Sunscreen (SPF 50, 50ml)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Mediterranean itinerary legs require daily UV protection; 50ml tube complies with liquid rules and provides sufficient volume for a 10-day trip."
    },
    {
      "item": "Prescription Medications",
      "quantity": 10,
      "formula": "N",
      "reason": "Full supply for trip duration kept in carry-on; European pharmacy access is reliable but prescription equivalences vary by country — importing a full supply eliminates interruption risk."
    },
    {
      "item": "Phone + Charging Cable",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Navigation, translation, and digital ticketing backbone of the trip; cable loss renders the phone operationally impaired by day 2."
    },
    {
      "item": "EU Power Adapter (Type C/F)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Mandatory for UK-to-Europe or non-EU traveler; a single dual-type (C+F) adapter covers the majority of continental destinations."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Navigation and photography workload on 10+ hour sightseeing days drains phone batteries faster than standard use; outlet access at museums and transit hubs is unreliable."
    },
    {
      "item": "Passport Wallet (with RFID block)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Centralized secure document storage with RFID shielding against electronic pickpocketing; essential in high-density tourist zones across major European capitals."
    }
  ]
}
```

---

### Scenario 7: Sub-Arctic Wilderness Camping

```json
{
  "intent": "Leisure",
  "duration": 7,
  "infrastructure": "Zero",
  "risks": ["Hypothermia & Rapid Weather Deterioration", "Glacial River Crossing Hazard", "Midge Swarms & UV Overexposure (Midnight Sun)"],
  "reasoning_summary": "Iceland camping operates in a zero-infrastructure framework despite being a developed country — designated campsites provide minimal facilities but wilderness zones have no shelter, no potable water, and no rescue proximity. Weather can shift from calm to horizontal rain and 60 mph winds in under 15 minutes, making layered waterproof systems non-negotiable. The midnight sun disrupts circadian rhythm and produces prolonged UV exposure requiring UV management at unusual hours. Merino wool is the default fabric across all clothing categories for moisture management at sub-zero wet-bulb temperatures. All cooking energy must be carried in.",
  "items": [
    {
      "item": "4-Season Tent (freestanding, rated to 60+ mph wind)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Icelandic wind speeds routinely exceed the rating threshold of 3-season tents; a 4-season geodesic structure is mandatory — tent failure in a remote zone is a life safety event."
    },
    {
      "item": "Sleeping Bag (-10°C comfort rating)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Even in summer, Icelandic overnight temperatures can approach 0°C in highland areas; a -10°C rated bag with a liner provides adequate thermal margin without being over-specified."
    },
    {
      "item": "Inflatable Sleeping Pad (R-value ≥ 4)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Ground cold in Iceland's lava field and glacial terrain conducts heat away from the body rapidly; an R-value 4+ pad is the primary insulation layer beneath the sleeping bag."
    },
    {
      "item": "Sleeping Bag Liner (silk or fleece)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Adds 5–8°C of effective warmth and acts as a moisture barrier protecting the sleeping bag from body oils; extends bag washing interval across a 7-day trip."
    },
    {
      "item": "Merino Wool Base Layer Sets (top + bottom)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Two sets allow one to be worn while the other dries; merino's thermal regulation at the wet-bulb temperatures common in Icelandic rain is superior to all synthetic alternatives."
    },
    {
      "item": "Merino Wool Mid-Layer Tops",
      "quantity": 4,
      "formula": "N/2",
      "reason": "4 tops for 7 days reflects a rewear protocol supported by merino's natural odor resistance; the N/2 formula avoids full N coverage that would be excessive for a technical camping kit."
    },
    {
      "item": "Fleece Mid-Layer Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Insulating mid-layer for the primary layering system; fleece retains thermal properties when damp — a critical property when rain saturation of outer layers occurs."
    },
    {
      "item": "Insulated Down Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Top insulation layer for camp use and glacier walks; packable to fist-size when not deployed. Must be worn under (not over) the hardshell in precipitation to prevent loft saturation."
    },
    {
      "item": "Waterproof Hardshell Jacket (3-layer, minimum 20,000mm HH)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hypothermia prevention primary asset; a 20,000mm hydrostatic head rating withstands Iceland's sustained horizontal rain — lower-rated jackets fail within hours in these conditions."
    },
    {
      "item": "Waterproof Hardshell Pants",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Full lower-body waterproofing is required for stream crossings and exposed highland plateau walking; wet legs in wind at 0°C produce rapid core temperature loss."
    },
    {
      "item": "Merino Wool Socks",
      "quantity": 8,
      "formula": "N+1",
      "reason": "Daily sock change is critical for foot health on 8–12 hour hiking days; the +1 buffer covers a stream-crossing saturation event requiring a mid-day change."
    },
    {
      "item": "Waterproof Hiking Boots (ankle height, Vibram sole)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Iceland's terrain — lava fields, volcanic ash, wet tussock grass, and glacial outwash plains — demands ankle support and waterproofing in a single platform."
    },
    {
      "item": "Wool Beanie",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Head covers 30% of body heat loss surface; two beanies allow rotation of wet and dry — losing the only beanie to wind is a plausible field incident in Iceland."
    },
    {
      "item": "Balaclava",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Full face coverage in wind-driven rain prevents the wind-chill exposure that accelerates hypothermia onset; fits under a hood as a secondary facial protection layer."
    },
    {
      "item": "Waterproof Gloves (with liner gloves)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hand dexterity loss from cold prevents tent setup and stove operation — activities that are critical for survival in deteriorating conditions. Liner gloves add fine-motor function in cold with reduced bulk."
    },
    {
      "item": "Gaiters",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Essential for glacial river and volcanic ash navigation; prevent ingress of water and debris into boots on the terrain types that dominate Icelandic highland routes."
    },
    {
      "item": "Trekking Poles (collapsible)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Glacial river crossing stability is a primary safety function, not a comfort feature; poles extend reach and test depth before committing bodyweight to a crossing."
    },
    {
      "item": "Camp Stove + Fuel Canisters (220g isobutane/propane)",
      "quantity": 4,
      "formula": "N/2",
      "reason": "All cooking energy must be carried in zero-infrastructure environments; 1 canister per ~2 days is the conservative estimate for boiling water (hydration and cooking combined) across 7 days."
    },
    {
      "item": "Cookset (pot, cup, spork, lighter)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Self-sufficient cooking system for the full 7-day kit; titanium construction minimizes weight without sacrificing durability on lava rock surfaces."
    },
    {
      "item": "Water Filter / Purification Tablets",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Iceland's glacial streams appear pristine but carry agricultural runoff and giardia in lowland areas; a filter provides operational water independence from carried supply."
    },
    {
      "item": "Headlamp + Spare Batteries",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Required for tent tasks (reading maps, first aid) even during midnight sun periods when a psychological assumption of no darkness can lead to unpreparedness on late-season trips."
    },
    {
      "item": "Navigation (offline GPS + paper topographic map + compass)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Highland Iceland has no mobile signal; offline GPS serves as primary navigation and paper topo + compass is the mandatory backup when battery fails in cold (batteries lose 30–40% capacity at 0°C)."
    },
    {
      "item": "Emergency Whistle + Signal Mirror",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Search and rescue signaling in Iceland's featureless highland plateaus; a whistle carries to SAR teams when visual contact is obscured by fog or terrain."
    },
    {
      "item": "First Aid Kit (emergency foil blanket, chemical heat packs, wound care)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Hypothermia treatment is the primary first aid scenario in Iceland; emergency foil blankets and chemical heat packs are the field-stabilization tools before evacuation."
    },
    {
      "item": "Sunscreen (SPF 50)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Midnight sun creates continuous UV exposure for 20+ hours per day in June–July; glacial and snow-covered terrain reflects UV from below, producing combined top-and-bottom exposure that standard sunscreen timing norms do not account for."
    },
    {
      "item": "Midge Head Net",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Icelandic midges emerge in large swarms in summer near water sources; a head net prevents the constant harassment that impairs navigation focus and camp setup efficiency."
    },
    {
      "item": "Portable Power Banks (10,000 mAh each)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Zero grid infrastructure for 7 days with cold-weather battery drain requires two banks in rotation; cold reduces lithium battery output — keeping one bank inside the sleeping bag at night maintains charge capacity."
    }
  ]
}
```

---

### Scenario 8: East & Southern Africa Safari

```json
{
  "intent": "Leisure",
  "duration": 10,
  "infrastructure": "Low",
  "risks": ["Malaria & Vector-Borne Disease", "Dust & UV Radiation Exposure", "Weight & Size Restrictions on Bush Aircraft"],
  "reasoning_summary": "East and Southern Africa safari operations are constrained by small bush aircraft weight limits (33–44 lbs total luggage) that force a hard ceiling on kit volume. Clothing must be neutral-toned (khaki, tan, green, brown) — bright colors and camouflage are prohibited at most camps and border posts respectively. Low infrastructure means unreliable grid power, no pharmacy access, and limited laundry (typically every 2 days at camps). The malaria prophylaxis protocol extends beyond the trip duration, and DEET-concentration repellent must be maintained throughout daylight and dusk hours. Soft-sided luggage is mandatory — hard cases cannot fit in bush aircraft holds.",
  "items": [
    {
      "item": "Safari Shirts (neutral: khaki, tan, olive)",
      "quantity": 5,
      "formula": "N/2",
      "reason": "5 shirts for 10 days reflects the camp laundry protocol (typically offered every 2 days); quick-dry synthetic-cotton blends enable overnight drying so the same shirt can be used on day 3."
    },
    {
      "item": "Long-Sleeved Shirts (neutral, lightweight)",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Long sleeves are the primary physical barrier against mosquito bites during dawn and dusk game drives — the highest malaria transmission windows; 3 covers a rotation without exceeding weight limits."
    },
    {
      "item": "Convertible Safari Pants (zip-off)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Zip-off design effectively doubles as 2 garments (pants and shorts) within a single weight footprint; SPF-rated fabric provides UV protection during open-vehicle game viewing."
    },
    {
      "item": "Fleece Jacket / Warm Sweater",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Early morning game drives on the African bush plateau can be 10–15°C despite afternoon temperatures of 35°C+; one fleece wears during drives, one remains dry at camp."
    },
    {
      "item": "Moisture-Wicking Underwear",
      "quantity": 10,
      "formula": "N",
      "reason": "Daily change is a hygiene non-negotiable in tropical heat and humidity; moisture-wicking fabric prevents the maceration that elevates fungal infection risk in sustained heat exposure."
    },
    {
      "item": "Bug-Repellent Socks (permethrin-treated)",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Permethrin-treated socks provide secondary ankle and lower-leg protection during walks at camp and bush walks; source specifically calls out this item as a malaria mitigation layer."
    },
    {
      "item": "Regular Hiking Socks",
      "quantity": 5,
      "formula": "N/2",
      "reason": "Paired with camp laundry availability; 5 pairs for 10 days assumes a 2-day wear cycle per pair for walking use."
    },
    {
      "item": "Wide-Brim Sun Hat",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Open-vehicle game drives expose passengers to direct equatorial UV for 3–6 hours per session; a wide brim covers neck and facial zones that sunscreen alone cannot maintain at this UV intensity."
    },
    {
      "item": "Polarized Sunglasses",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Glare reduction during open-vehicle drives enables wildlife spotting at distance; polarization filters the reflective haze over water sources where most wildlife congregates."
    },
    {
      "item": "Buff Wrap / Neck Gaiter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Dust protection for nose and mouth during dry-season game drives on unpaved tracks; doubles as additional UV neck coverage."
    },
    {
      "item": "Swimsuit",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Most permanent tented camps and lodges have plunge pools; post-drive swim is a standard recovery protocol and the swimsuit serves no other function."
    },
    {
      "item": "Closed-Toe Walking Shoes",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Bush walks require covered footwear for snake and thorn protection; ankle coverage is recommended by most professional guides."
    },
    {
      "item": "Camp Sandals",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Rest footwear at camp reduces cumulative foot fatigue; keeps primary walking shoes dry during afternoon lodge downtime."
    },
    {
      "item": "Soft-Sided Duffel Bag (44L, ≤44 lbs total)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly states hard suitcases are prohibited on bush aircraft due to cargo hold dimensions; soft duffel compresses into irregular spaces that rigid cases cannot occupy."
    },
    {
      "item": "Daypack (20L, packable)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Carries game-drive essentials (water, camera, repellent, sunscreen) during vehicle-based and walking bush sessions without burdening the main duffel."
    },
    {
      "item": "Binoculars (8×42)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies 8×42 as the optimal aperture for wildlife identification at the distances typical of African bush environments; 8× magnification provides stability without image shake from vehicle vibration."
    },
    {
      "item": "Camera + Spare Batteries + Memory Cards (64GB x3)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Wildlife photography generates 500–1000 images per day during active game drives; three memory cards prevent mid-drive capacity loss and spare batteries eliminate dependence on camp charging."
    },
    {
      "item": "Malaria Prophylaxis (full prescribed course)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Destination-specific anti-malarial must be prescribed before departure; course begins 1–2 days pre-trip and extends 7 days post-return depending on the medication — a single course covers the full protocol."
    },
    {
      "item": "DEET Insect Repellent (30%+), 100ml bottles",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Two bottles for 10 days ensures reapplication every 4–6 hours during active outdoor windows (dawn, dusk) without rationing; DEET concentration above 20% is the WHO-recommended floor for malaria-endemic zones."
    },
    {
      "item": "Sunscreen (SPF 50), 100ml",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Equatorial UV on open vehicles requires full reapplication every 90 minutes; two bottles provides adequate volume for a 10-day rotation of daily long-exposure sessions."
    },
    {
      "item": "Travel Medical Kit (antihistamine, anti-diarrheal, rehydration salts, antiseptic, painkillers, bandages)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "No pharmacy access in low-infrastructure safari zones; rehydration salts are critical for managing GI disruption that dietary transition and heat stress can produce."
    },
    {
      "item": "Portable Power Bank (20,000 mAh)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Camp generators typically operate on scheduled windows (6–10pm); a high-capacity power bank sustains camera battery charging, phone, and communication device throughout non-generator hours."
    },
    {
      "item": "Multi-Region Power Adapter (Type G/M/D)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "East and Southern Africa use Type G (Kenya, Tanzania) and Type M/D (South Africa, Botswana, Zambia) — a multi-region adapter covers itineraries that cross both zones."
    },
    {
      "item": "Packing Cubes (compression type)",
      "quantity": 3,
      "formula": "Constant",
      "reason": "Compression cubes maximize the usable volume of a 44L soft duffel; organization by category (clothing / gear / medical) enables rapid access in the pre-dawn 4:30am game drive departure windows."
    }
  ]
}
```

---

### Scenario 9: Remote Luxury Safari (Multi-Country)

```json
{
  "intent": "Leisure",
  "duration": 7,
  "infrastructure": "Low",
  "risks": ["Malaria Transmission Zone", "Extreme Temperature Swing (Day/Night Delta 25–30°C)", "Limited Medevac Access in Remote Bush"],
  "reasoning_summary": "African Bush Camps properties sit in remote wilderness areas with scheduled generator power, no commercial pharmacy access, and medical evacuation measured in hours. The temperature swing between midday (35–40°C) and pre-dawn game drive (8–12°C) is 25–30°C on the same day, requiring a complete layering system within a single light-aircraft-compatible soft bag. Laundry service is available daily at most bush camps, supporting a compressed clothing formula. Malaria documentation (prophylaxis prescription) is required for camp entry in some territories. Single-use plastics and excessive jewelry are prohibited at most properties.",
  "items": [
    {
      "item": "Breathable Cotton Safari Shirts (neutral tones)",
      "quantity": 4,
      "formula": "N/2",
      "reason": "Daily laundry service at bush camps supports a 2-day rotation; 4 shirts for 7 days accounts for one extra in case laundry turnaround extends past a day due to rain or power schedule changes."
    },
    {
      "item": "Long-Sleeved Protective Shirts",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Mandatory physical barrier for dawn and dusk drives in malaria-transmission zones; a dedicated long-sleeve rotation prevents full reliance on chemical repellent alone."
    },
    {
      "item": "Safari Pants (neutral, lightweight)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Two pairs cover the alternating use-and-wash cycle supported by daily camp laundry; neutrals (tan, khaki) comply with camp and border-crossing requirements."
    },
    {
      "item": "Warm Layers (fleece pullover + lightweight down gilet)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "The 25–30°C day-to-night temperature swing is the primary thermal management challenge; two distinct mid-layer garments allow adaptation across the full diurnal range without a heavy outer jacket."
    },
    {
      "item": "Waterproof Jacket",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Green season bush camps experience afternoon thunder storms; a packable waterproof jacket prevents hypothermia onset that wet mid-layers can cause during sudden evening temperature drops."
    },
    {
      "item": "Casual Camp Wear Sets (lightweight shirt + linen trousers)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Separate camp clothing prevents cross-contamination of field-use items with bush dust and insect repellent; light linen is the standard evening social standard at bush camp dinners."
    },
    {
      "item": "Swimsuit",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Plunge pools are a standard amenity at African Bush Camps properties; afternoon swim is the primary recovery activity between morning and evening game drives."
    },
    {
      "item": "Sun Hat (wide brim)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Equatorial UV on open-vehicle game drives is unfiltered at altitude; neck and facial coverage from a wide brim reduces cumulative UV exposure that sunscreen alone cannot manage."
    },
    {
      "item": "Polarized Sunglasses",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Glare reduction on open water sources and dry pans is essential for wildlife spotting at the distances typical of bush vehicle positioning."
    },
    {
      "item": "Lightweight Scarf / Bandanna",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Dust and fine particulate on unpaved game drive tracks require nose and mouth protection; the scarf doubles as a neck UV shield and an improvised cold layer for pre-dawn drives."
    },
    {
      "item": "Closed-Toe Shoes (lightweight hiking)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Bush walks and camp perimeter areas require covered footwear for snake, scorpion, and thorn risk; professional guides enforce closed-toe policy compliance for all guests."
    },
    {
      "item": "Camp Sandals",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Recovery footwear for lodge common areas; reduces total shoe weight below the threshold that a second boot pair would add."
    },
    {
      "item": "Soft-Sided Duffel Bag (≤18kg / 40 lbs)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly states hard cases are not permitted on bush aircraft; soft construction compresses to the irregular hold dimensions of light twin-engine safari planes."
    },
    {
      "item": "Camera + Extra Batteries + Memory Cards",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifically calls out extra batteries; generator charge windows are short (typically 6–10pm) and camera batteries drain in 200–400 shots — two spare batteries eliminate a mid-game-drive power failure."
    },
    {
      "item": "Lightweight Binoculars (8×32 or 8×42)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Wildlife identification at 200–400m range is the primary visual task during bush drives; a quality compact binocular extends effective viewing distance without telescope-level weight."
    },
    {
      "item": "Headlamp",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Bush camps have no perimeter lighting to prevent wildlife intrusion; a headlamp is mandatory for safe navigation between tent and main lodge areas after dark."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Generator windows are insufficient to fully charge all devices; a power bank bridges the gap and enables communication device function overnight for emergency contact capability."
    },
    {
      "item": "Electronics Adapters (Type M + Type G)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Multi-country Southern/Eastern Africa itineraries cross Type M (Zambia, Zimbabwe, Botswana) and Type G (Tanzania, Kenya) socket standards; a dual-type adapter covers the full corridor."
    },
    {
      "item": "Malaria Prophylaxis (full prescribed course + prescription documentation)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly requires prescription documentation for some camp entries in malarial zones; the full course (pre-, during-, and post-trip) is a single medical event, not a per-day calculation."
    },
    {
      "item": "DEET Insect Repellent (30%+)",
      "quantity": 2,
      "formula": "Constant",
      "reason": "Two bottles for 7 days at the reapplication frequency required (every 4–6 hours during active transmission windows) prevents rationing that would undermine the malaria mitigation protocol."
    },
    {
      "item": "Medical Kit (painkillers, antihistamine, antiseptic cream, bite relief, anti-diarrheal)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "No commercial pharmacy within medevac range; limited medevac access makes self-treatment of minor conditions essential — every untreated minor condition is a potential escalation point in remote bush."
    },
    {
      "item": "Passport (6+ months validity) + Copies + Vaccination Certificate",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies 6-month passport validity as a camp and border entry requirement; vaccination certificate (yellow fever for some corridors) must accompany the passport as a standalone document."
    },
    {
      "item": "Travel Insurance Policy + Emergency Contact Card",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Limited medevac access requires an insurance policy with specific air-evacuation coverage; the emergency contact card must be physically present in the camp for use in the event the guest is incapacitated."
    },
    {
      "item": "Regional Bird / Wildlife Guide",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly recommends a Southern African bird guide; enhances the observational value of each game drive and is considered standard preparation etiquette by professional guides."
    }
  ]
}
```

---

### Scenario 10: Essential Wild Camping (Minimalist Backcountry)

```json
{
  "intent": "Leisure",
  "duration": 5,
  "infrastructure": "Zero",
  "risks": ["Hypothermia from Wet-Cold Exposure", "Navigation Error & Disorientation", "Tick-Borne Disease (Lyme, TBE)"],
  "reasoning_summary": "Van Dillen's minimalist wild camping philosophy strips the kit to its irreducible functional core — every item must justify its weight against direct operational necessity. Zero infrastructure means no facilities, no resupply, and no grid power across the full 5-day window. The sleep system is the primary survival asset: a layered combination of sleeping mat R-value, bag comfort rating, and liner creates a thermal safety margin against the wet-cold conditions common in European temperate wilderness. Cooking energy (fuel canisters) is the only consumable that scales with duration. Hygiene wipes replace running water entirely.",
  "items": [
    {
      "item": "Tent or Bivouac",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Primary shelter asset; source offers both options (tent for comfort, bivouac for ultralight) — selection is terrain-dependent. A freestanding 3-season tent is the default for group wild camping on European terrain."
    },
    {
      "item": "Sleeping Bag (0°C comfort rating, down)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies 0°C comfort rated down bag; European temperate zones with overnight temperatures of 5–10°C in spring/autumn require a 0°C rating to maintain safe core temperature throughout a 5-day window."
    },
    {
      "item": "Sleeping Mat (4-inch inflatable, three-season)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies a 4-inch inflatable three-season mat; ground insulation is the first line of defense against conductive heat loss, which the sleeping bag alone cannot prevent."
    },
    {
      "item": "Sleeping Bag Liner",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly calls this out for temperature fluctuation management; adds 5–8°C of effective warmth and protects the down bag from moisture absorption — a saturated down bag loses most of its insulation value."
    },
    {
      "item": "Merino Wool Base Layer — Long-Sleeve Top + Leggings",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies merino for the base layer; worn as the sleep layer and packed under the rain gear for cold-morning transitions — merino's temperature regulation makes a single set functional across a wide thermal range."
    },
    {
      "item": "Liner Gloves (rated to -10°C)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies liner gloves rated to -10°C; hand dexterity at temperatures that exceed the insulation range of base gloves is critical for stove operation and navigation tasks in a zero-infrastructure environment."
    },
    {
      "item": "Rain Jacket + Rain Pants (waterproof shell set)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly includes both jacket and pants as a paired shell set; full-body waterproofing is the primary hypothermia prevention layer — wet base layers in wind initiate hypothermia within 30–60 minutes in temperate conditions."
    },
    {
      "item": "Down Jacket (packable)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies a down jacket for cooling evenings; camp temperature management at rest (sitting still, eating, navigating at camp) drops core temperature faster than active hiking — a camp insulation layer is essential."
    },
    {
      "item": "Camp Gas Burner",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies gas burner as primary cooking tool; a single burner unit covers all cooking and water-boiling functions for the trip."
    },
    {
      "item": "Fuel Canisters (220g isobutane/propane)",
      "quantity": 3,
      "formula": "N/2",
      "reason": "1 canister per ~2 days is the conservative estimate for boiling water (for hydration, cooking, and hot drinks) across 5 days; 3 canisters (N/2 rounded up) provides a one-canister safety margin."
    },
    {
      "item": "Matches + Backup Lighter",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies matches or lighter as ignition; dual-redundancy (matches and lighter) ensures fire-starting capability even if one source is wet or depleted — fire loss in wet conditions eliminates cooking and warmth options."
    },
    {
      "item": "Cookset (pot, mug, spork, plate, pocket knife)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifies all five components as a single cookset unit; titanium or hard-anodized aluminum construction provides the strength-to-weight ratio appropriate for multi-day backcountry use."
    },
    {
      "item": "Percolator (camp coffee maker)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly calls out a percolator; beyond comfort, hot beverage availability at dawn supports the core temperature recovery that is critical on cold-start mornings before the day's exertion begins."
    },
    {
      "item": "First Aid Kit (plasters, disinfectant, bandages, tick removal tool, painkiller)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source specifically names tick removal as a first aid component — directly addressing tick-borne disease risk; a tick removal tool (not fingers) is the clinically recommended extraction method that reduces disease transmission probability."
    },
    {
      "item": "Headlamp",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Zero-infrastructure night operation requires hands-free lighting for tent setup, cooking, and navigating camp; source specifies this as one of only two safety-critical visibility tools."
    },
    {
      "item": "Hygiene Wipes",
      "quantity": 5,
      "formula": "N",
      "reason": "Source relies on hygiene wipes as the primary body-cleaning method in the absence of running water; one pack per day maintains the minimum hygiene standard to prevent skin degradation over a 5-day field window."
    },
    {
      "item": "Toothbrush + Toothpaste",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Dental hygiene maintenance across 5 days; travel-size toothpaste reduces pack weight without compromising the twice-daily brushing protocol."
    },
    {
      "item": "Phone (with offline navigation apps pre-loaded)",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Navigation error risk mitigation; offline maps (OS, Komoot, or AllTrails) downloaded before departure provide full route guidance without mobile signal dependency in zero-infrastructure terrain."
    },
    {
      "item": "Portable Power Bank",
      "quantity": 1,
      "formula": "Constant",
      "reason": "No grid charging for 5 days; a 10,000 mAh bank provides approximately 3 full phone charges — sufficient for navigation, photography, and emergency communication across the full trip window."
    },
    {
      "item": "Diary / Notebook + Pen",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source explicitly includes diary and pen; functions as a field log for route notes, emergency location records, and the reflective documentation of the outdoor experience that justifies the kit."
    },
    {
      "item": "Bank Card + Emergency Cash",
      "quantity": 1,
      "formula": "Constant",
      "reason": "Source lists bankcard and cash as personal items; required for trailhead parking, permit purchase, and emergency resupply or evacuation — the only points where zero-infrastructure wild camping intersects with the commercial system."
    }
  ]
}
```
