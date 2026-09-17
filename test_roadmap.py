from roadmap_generator import generate_roadmap


# Example missing skills
missing_skills = [
    "Data Structures",
    "Algorithms",
    "REST API",
    "Git"
]


roadmap = generate_roadmap(missing_skills)


print("\n========== LEARNING ROADMAP ==========\n")

for item in roadmap:

    print(f"Skill: {item['skill']}")
    print(f"Recommendation: {item['recommendation']}")
    print("-" * 50)