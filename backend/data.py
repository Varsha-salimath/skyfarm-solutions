"""Garden data and business logic for SkyFarm Solutions."""

PLANTS = [
    {"id": "tomato", "name": "Tomato", "emoji": "🍅", "sunlight": ["full"], "seasons": ["spring", "summer"], "soil": ["loamy", "silty"], "care": "Water deeply 2–3x/week; stake for support."},
    {"id": "basil", "name": "Basil", "emoji": "🌿", "sunlight": ["full", "partial"], "seasons": ["spring", "summer"], "soil": ["loamy", "sandy"], "care": "Pinch flowers to encourage leaf growth."},
    {"id": "lettuce", "name": "Lettuce", "emoji": "🥬", "sunlight": ["partial", "shade"], "seasons": ["spring", "fall"], "soil": ["loamy", "silty"], "care": "Keep soil moist; harvest outer leaves first."},
    {"id": "carrot", "name": "Carrot", "emoji": "🥕", "sunlight": ["full", "partial"], "seasons": ["spring", "fall"], "soil": ["sandy", "loamy"], "care": "Loose, deep soil; thin seedlings early."},
    {"id": "pepper", "name": "Bell Pepper", "emoji": "🫑", "sunlight": ["full"], "seasons": ["summer"], "soil": ["loamy", "silty"], "care": "Consistent moisture; mulch to retain heat."},
    {"id": "spinach", "name": "Spinach", "emoji": "🥗", "sunlight": ["partial", "shade"], "seasons": ["spring", "fall", "winter"], "soil": ["loamy", "silty"], "care": "Cool weather crop; bolt-resistant varieties for warm areas."},
    {"id": "mint", "name": "Mint", "emoji": "🍃", "sunlight": ["partial", "shade"], "seasons": ["spring", "summer", "fall"], "soil": ["loamy", "silty"], "care": "Grow in containers to prevent spreading."},
    {"id": "lavender", "name": "Lavender", "emoji": "💜", "sunlight": ["full"], "seasons": ["spring", "summer"], "soil": ["sandy", "loamy"], "care": "Well-drained soil; avoid overwatering."},
    {"id": "cucumber", "name": "Cucumber", "emoji": "🥒", "sunlight": ["full"], "seasons": ["summer"], "soil": ["loamy", "silty"], "care": "Trellis for vertical growth; water daily in heat."},
    {"id": "strawberry", "name": "Strawberry", "emoji": "🍓", "sunlight": ["full", "partial"], "seasons": ["spring", "summer"], "soil": ["loamy", "sandy"], "care": "Mulch around plants; remove runners for bigger fruit."},
    {"id": "zucchini", "name": "Zucchini", "emoji": "🥒", "sunlight": ["full"], "seasons": ["summer"], "soil": ["loamy", "silty"], "care": "Harvest when 6–8 inches long for best flavor."},
    {"id": "kale", "name": "Kale", "emoji": "🥬", "sunlight": ["full", "partial"], "seasons": ["fall", "winter", "spring"], "soil": ["loamy", "silty"], "care": "Frost improves sweetness; pick lower leaves first."},
]

SOIL_PROFILES = {
    "tomato": {"ideal": ["loamy", "silty"], "advice": {"sandy": "Add compost and mulch to improve water retention.", "clay": "Mix in sand and organic matter for better drainage.", "silty": "Great match — maintain organic content with compost.", "loamy": "Perfect — rich, well-drained loam is ideal."}},
    "basil": {"ideal": ["loamy", "sandy"], "advice": {"clay": "Amend with perlite and compost for drainage.", "silty": "Works well; avoid waterlogged conditions.", "loamy": "Perfect — rich, well-drained loam is ideal.", "sandy": "Ideal — ensure consistent moisture."}},
    "lettuce": {"ideal": ["loamy", "silty"], "advice": {"sandy": "Add peat or compost; water more frequently.", "clay": "Raise beds and add organic matter.", "loamy": "Excellent — keep consistently moist.", "silty": "Very suitable for leafy greens."}},
    "carrot": {"ideal": ["sandy", "loamy"], "advice": {"clay": "Heavy clay causes forked roots — use raised beds with sand.", "silty": "Acceptable with good drainage.", "sandy": "Ideal for straight, long roots.", "loamy": "Excellent for healthy root development."}},
    "pepper": {"ideal": ["loamy", "silty"], "advice": {"sandy": "Add compost; peppers need steady moisture.", "clay": "Improve drainage with gypsum and organic matter.", "loamy": "Optimal — warm, fertile soil.", "silty": "Great match with good drainage."}},
    "spinach": {"ideal": ["loamy", "silty"], "advice": {"sandy": "Mulch heavily and water often.", "clay": "Add compost; ensure drainage to prevent rot.", "silty": "Very suitable for leafy greens.", "loamy": "Ideal — keep soil cool and moist."}},
    "mint": {"ideal": ["loamy", "silty"], "advice": {"sandy": "Keep moist; mint tolerates many soils.", "clay": "Can work if drainage is improved.", "loamy": "Ideal — moist, rich soil.", "silty": "Works well with regular watering."}},
    "lavender": {"ideal": ["sandy", "loamy"], "advice": {"clay": "Poor match — lavender needs dry, alkaline soil.", "silty": "Moderate; ensure excellent drainage.", "sandy": "Perfect — mimics Mediterranean conditions.", "loamy": "Good if drainage is excellent."}},
}

TIPS = [
    {"category": "watering", "title": "Water in the morning", "body": "Morning watering reduces evaporation and lets foliage dry before night, lowering disease risk."},
    {"category": "watering", "title": "Deep, not shallow", "body": "Water deeply 2–3 times per week rather than light daily sprinkles to encourage deep root growth."},
    {"category": "watering", "title": "Check soil moisture", "body": "Stick your finger 2 inches into soil. Water only when it feels dry at that depth."},
    {"category": "fertilizing", "title": "Compost is king", "body": "Add 2–3 inches of compost annually. It improves soil structure and provides slow-release nutrients."},
    {"category": "fertilizing", "title": "N-P-K basics", "body": "Nitrogen for leaves, phosphorus for roots/flowers, potassium for overall health. Match fertilizer to growth stage."},
    {"category": "fertilizing", "title": "Don't over-fertilize", "body": "Too much nitrogen produces lush foliage but fewer fruits. Follow package directions carefully."},
    {"category": "care", "title": "Mulch your beds", "body": "A 2–3 inch layer of straw, wood chips, or leaves suppresses weeds and retains soil moisture."},
    {"category": "care", "title": "Rotate crops yearly", "body": "Moving plant families to new beds each season prevents soil depletion and reduces pest buildup."},
    {"category": "care", "title": "Prune for airflow", "body": "Remove crowded or diseased growth to improve air circulation and reduce fungal problems."},
    {"category": "seasonal", "title": "Spring prep", "body": "Test soil pH, clear debris, and start seeds indoors 6–8 weeks before last frost."},
    {"category": "seasonal", "title": "Summer heat protection", "body": "Use shade cloth during heat waves and water early. Mulch heavily to keep roots cool."},
    {"category": "seasonal", "title": "Fall cleanup", "body": "Remove spent plants, add compost, and plant cover crops like clover to enrich soil over winter."},
]


def get_all_plants():
    return PLANTS


def recommend_plants(sunlight, season, soil):
    return [
        p for p in PLANTS
        if sunlight in p["sunlight"] and season in p["seasons"] and soil in p["soil"]
    ]


def calculate_space(length, width, layout):
    area = length * width

    if layout == "rows":
        row_width = 2
        rows = max(1, int(width // row_width))
        plants_estimate = rows * max(1, int(length // 1.5))
        suggestions = [
            f"Create {rows} planting rows with 2 ft paths between them.",
            f"Fit roughly {plants_estimate} medium plants (tomatoes, peppers) at 1.5 ft spacing.",
            "Orient rows north–south for even sunlight exposure.",
            "Reserve one corner for herbs in a 3×3 ft section.",
        ]
    elif layout == "grid":
        squares = max(1, int(area))
        plants_estimate = squares
        suggestions = [
            f"Divide into {squares} one-foot square planting zones.",
            "Ideal for intensive urban gardens and raised beds.",
            "Mix fast growers (lettuce, radish) with slow crops (tomatoes).",
            "Use vertical trellises on north side to save ground space.",
        ]
    else:
        plants_estimate = max(1, int(area // 4))
        suggestions = [
            f"Room for about {plants_estimate} containers (2×2 ft each).",
            "Perfect for balconies, patios, and rooftop gardens.",
            "Use 5-gallon buckets for tomatoes; 12-inch pots for herbs.",
            "Group containers by water needs for easier maintenance.",
        ]

    return {
        "summary": f"Your {length}×{width} ft garden ({area} sq ft) can support approximately {plants_estimate} plants.",
        "area": area,
        "plants_estimate": plants_estimate,
        "suggestions": suggestions,
    }


def check_soil(plant_id, soil):
    profile = SOIL_PROFILES.get(plant_id)
    plant = next((p for p in PLANTS if p["id"] == plant_id), None)

    if not profile or not plant:
        return None

    plant_name = plant["name"]
    soil_label = soil.capitalize()

    if soil in profile["ideal"]:
        return {
            "verdict": f"✓ {soil_label} soil is excellent for {plant_name}!",
            "status": "good",
            "advice": profile["advice"].get(soil, "Maintain soil health with annual compost top-dressing."),
        }

    if soil in profile["advice"]:
        return {
            "verdict": f"△ {soil_label} soil can work for {plant_name} with amendments.",
            "status": "fair",
            "advice": profile["advice"][soil],
        }

    ideal = " or ".join(profile["ideal"])
    return {
        "verdict": f"✗ {soil_label} soil is not ideal for {plant_name}.",
        "status": "poor",
        "advice": f"Consider raised beds with {ideal} soil mix, or choose plants better suited to {soil} soil.",
    }


def get_tips(category=None):
    if not category or category == "all":
        return TIPS
    return [t for t in TIPS if t["category"] == category]
