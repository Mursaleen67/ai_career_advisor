import requests

def analyze_skills(skills):

    prompt = f"""
A person has these skills: {skills}

Suggest:
1. Three career paths with explanation
2. Additional skills to learn

Format the response exactly like this:

CAREERS:
1. Career Name - Explanation
2. Career Name - Explanation
3. Career Name - Explanation

SKILLS:
- Skill
- Skill
- Skill
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    text = data.get("response", "")

    careers = []
    additional_skills = []

    section = None

    for line in text.split("\n"):

        line = line.strip()

        if "CAREERS" in line:
            section = "career"
            continue

        if "SKILLS" in line:
            section = "skills"
            continue

        if not line:
            continue

        if section == "career":
            careers.append(line)

        elif section == "skills":
            if line.startswith("-"):
                additional_skills.append(line.replace("-", "").strip())

    return {
        "careers": careers,
        "skills": additional_skills
    }