import re


# ============================================================
# SKILL-SPECIFIC RECOMMENDATIONS
# ============================================================

RECOMMENDATION_MAP = {

    "docker":
        "Add Docker experience if you have used it. "
        "Mention containerization or Docker-based deployment "
        "in a relevant project.",

    "aws":
        "Mention AWS or cloud deployment experience if you "
        "have used services such as EC2 or S3.",

    "fastapi":
        "Mention FastAPI experience if you have built or "
        "deployed APIs using it.",

    "rest api":
        "Highlight REST API development and mention the "
        "frameworks you used to build your APIs.",

    "machine learning":
        "Highlight your machine learning projects and include "
        "measurable results such as accuracy or F1-score.",

    "scikit-learn":
        "Mention the Scikit-learn models you have implemented "
        "and the results achieved.",

    "deep learning":
        "Highlight your deep learning projects and specify "
        "the models or architectures you implemented.",

    "tensorflow":
        "Mention TensorFlow projects and the models you "
        "developed using it.",

    "pytorch":
        "Mention PyTorch projects and the neural network "
        "models you implemented.",

    "nlp":
        "Add NLP project experience if applicable and mention "
        "specific techniques such as text classification or "
        "embeddings.",

    "computer vision":
        "Highlight computer vision projects and explain the "
        "problem, model, and measurable results.",

    "opencv":
        "Mention OpenCV-based image processing or computer "
        "vision projects if you have used it.",

    "yolo":
        "Mention your YOLO object-detection projects and "
        "include model performance where possible.",

    "postgresql":
        "Mention PostgreSQL experience if you have worked with "
        "relational databases using PostgreSQL.",

    "mysql":
        "Highlight MySQL database experience and mention the "
        "type of queries or applications you built.",

    "mongodb":
        "Mention MongoDB experience if you have used NoSQL "
        "databases in your projects.",

    "redis":
        "Mention Redis experience if you have used it for "
        "caching, sessions, or backend applications.",

    "sql":
        "Highlight SQL experience by mentioning joins, "
        "subqueries, aggregation, and database projects "
        "where applicable.",

    "ci/cd":
        "Mention CI/CD experience if you have automated "
        "testing or deployment using tools such as GitHub "
        "Actions or Jenkins.",

    "github actions":
        "Mention GitHub Actions if you have created automated "
        "build, test, or deployment workflows.",

    "jenkins":
        "Mention Jenkins experience if you have worked with "
        "automated build or deployment pipelines.",

    "kubernetes":
        "Mention Kubernetes experience if you have deployed "
        "and managed containerized applications.",

    "linux":
        "Mention Linux experience and describe relevant "
        "command-line, server, or deployment work.",

    "bash":
        "Mention Bash or shell scripting experience if you "
        "have automated development or deployment tasks.",

    "pytest":
        "Mention Pytest and include examples of unit or "
        "integration tests you have written.",

    "unit testing":
        "Highlight unit-testing experience and mention the "
        "testing frameworks you have used.",

    "integration testing":
        "Mention integration-testing experience and explain "
        "how you tested interactions between application "
        "components.",

    "data structures":
        "Highlight your knowledge of data structures and "
        "mention relevant coding problems or projects.",

    "algorithms":
        "Highlight algorithm knowledge and mention relevant "
        "problem-solving or coding practice.",

    "data structures and algorithms":
        "Highlight Data Structures and Algorithms knowledge "
        "and mention relevant coding problems, platforms, "
        "or projects.",

    "object-oriented programming":
        "Mention object-oriented programming experience and "
        "highlight projects where you applied OOP principles.",

    "debugging":
        "Mention debugging experience and describe examples "
        "where you identified and fixed software issues.",

    "problem solving":
        "Highlight problem-solving skills using specific "
        "examples from your projects or internship experience.",

    "agile":
        "Mention Agile development experience if you have "
        "worked in an Agile team or followed Agile practices.",

    "scrum":
        "Mention Scrum experience if you have participated "
        "in sprints, stand-ups, or sprint planning.",

    "graphql":
        "Mention GraphQL experience if you have designed or "
        "consumed GraphQL APIs.",

    "react":
        "Mention React projects and describe the components "
        "or applications you developed.",

    "javascript":
        "Highlight JavaScript projects and mention the type "
        "of web applications or features you developed.",

    "typescript":
        "Mention TypeScript experience and explain how you "
        "used it in web or backend projects.",

    "node.js":
        "Mention Node.js backend projects and highlight the "
        "APIs or services you developed.",

    "django":
        "Mention Django projects and describe the backend "
        "applications or APIs you built.",

    "data analysis":
        "Highlight data-analysis projects and include the "
        "datasets, techniques, and insights you produced.",

    "data visualization":
        "Mention data-visualization experience and include "
        "tools such as Matplotlib, Seaborn, Power BI, or Tableau.",

    "statistics":
        "Highlight statistical analysis experience and mention "
        "the statistical methods you have applied.",

    "power bi":
        "Mention Power BI dashboards or reports you have "
        "created and describe the insights they provided.",

    "tableau":
        "Mention Tableau dashboards or visualizations you "
        "have created if applicable.",

    "generative ai":
        "Highlight Generative AI projects and mention the "
        "models, APIs, or techniques you used.",

    "large language models":
        "Mention LLM projects and specify the models, APIs, "
        "or applications you built.",

    "prompt engineering":
        "Mention prompt-engineering work and provide examples "
        "of how you improved model outputs.",

    "rag":
        "Highlight Retrieval-Augmented Generation projects "
        "and mention document retrieval, embeddings, and "
        "vector search where applicable.",

    "langchain":
        "Mention LangChain projects and describe how you used "
        "it to build LLM or RAG applications.",

    "streamlit":
        "Mention Streamlit applications you have developed "
        "and explain the problem they solve.",

    "postman":
        "Mention Postman experience for API testing and "
        "validation if applicable.",

    "git":
        "Highlight Git experience and mention branching, "
        "commits, pull requests, or collaborative development.",

    "github":
        "Include your GitHub projects and highlight relevant "
        "repositories that demonstrate your technical skills."
}


# ============================================================
# GENERIC RECOMMENDATION
# ============================================================

def create_generic_recommendation(skill):

    return (
        f"Consider adding {skill} to your resume if you have "
        f"practical experience with it. Include a project, "
        f"internship, or measurable result demonstrating "
        f"how you used the skill."
    )


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

def generate_recommendations(missing_skills):

    if not missing_skills:

        return [
            "Your resume covers the major skills detected "
            "in the job description."
        ]


    # --------------------------------------------------------
    # Important technical skills
    #
    # These are the skills we want to prioritize in the
    # Suggested Improvements section.
    # --------------------------------------------------------

    IMPORTANT_SKILLS = {

        "aws",
        "docker",
        "fastapi",
        "postgresql",
        "redis",
        "ci/cd",
        "pytest",
        "tensorflow",
        "pytorch",
        "machine learning",
        "scikit-learn",
        "computer vision",
        "opencv",
        "yolo",
        "langchain",
        "rag",
        "kubernetes",
        "mongodb",
        "power bi",
        "tableau",
        "react",
        "javascript",
        "typescript",
        "node.js",
        "django",
        "flask",
        "graphql",
        "github actions",
        "jenkins",
        "linux"
    }


    recommendations = []

    seen = set()


    for skill in missing_skills:

        skill_text = str(skill).strip()

        if not skill_text:
            continue


        skill_key = skill_text.lower()


        # Ignore generic concepts for recommendations
        if skill_key not in IMPORTANT_SKILLS:
            continue


        # Prevent duplicate recommendations
        if skill_key in seen:
            continue


        seen.add(skill_key)


        # ----------------------------------------------------
        # Use specific recommendation when available
        # ----------------------------------------------------

        if skill_key in RECOMMENDATION_MAP:

            recommendation = RECOMMENDATION_MAP[
                skill_key
            ]

        else:

            recommendation = (
                create_generic_recommendation(
                    skill_text
                )
            )


        recommendations.append(
            recommendation
        )


    # --------------------------------------------------------
    # If only generic concepts were missing
    # --------------------------------------------------------

    if not recommendations:

        recommendations.append(
            "Your resume already covers most of the "
            "important technical skills for this role."
        )


    return recommendations


# ============================================================
# EXPERIENCE MATCH
# ============================================================

def calculate_experience_match(
    resume_text,
    job_description
):

    resume_text = resume_text.lower()
    job_description = job_description.lower()


    # --------------------------------------------------------
    # Detect explicit experience requirement
    # --------------------------------------------------------

    required_min_years = None
    required_max_years = None


    range_match = re.search(
        r"(\d+)\s*(?:-|–|to)\s*(\d+)\s*years?",
        job_description
    )


    if range_match:

        required_min_years = int(
            range_match.group(1)
        )

        required_max_years = int(
            range_match.group(2)
        )


    else:

        plus_match = re.search(
            r"(\d+)\+?\s*years?\s*(?:of\s*)?experience",
            job_description
        )


        if plus_match:

            required_min_years = int(
                plus_match.group(1)
            )


    # --------------------------------------------------------
    # Entry-level detection
    # --------------------------------------------------------

    entry_level_terms = [

        "entry level",
        "entry-level",
        "fresher",
        "fresh graduate",
        "recent graduate",
        "graduate",
        "0-2 years",
        "0–2 years",
        "0 to 2 years",
        "1-2 years",
        "1–2 years",
        "1 to 2 years"
    ]


    is_entry_level = any(
        term in job_description
        for term in entry_level_terms
    )


    # --------------------------------------------------------
    # Detect years in resume
    # --------------------------------------------------------

    resume_year_matches = re.findall(
        r"(\d+(?:\.\d+)?)\+?\s*years?",
        resume_text
    )


    resume_years = 0.0


    if resume_year_matches:

        resume_years = max(
            float(year)
            for year in resume_year_matches
        )


    # --------------------------------------------------------
    # Detect practical experience
    # --------------------------------------------------------

    experience_keywords = [

        "internship",
        "intern",
        "work experience",
        "professional experience",
        "software engineer",
        "software developer",
        "developer",
        "engineer",
        "employment"
    ]


    experience_count = sum(
        keyword in resume_text
        for keyword in experience_keywords
    )


    # --------------------------------------------------------
    # Entry-level position
    # --------------------------------------------------------

    if is_entry_level:

        if experience_count >= 1:
            return "Good"

        return "Moderate"


    # --------------------------------------------------------
    # Explicit experience requirement
    # --------------------------------------------------------

    if required_min_years is not None:

        if resume_years >= required_min_years:

            return "Good"

        elif resume_years >= (
            required_min_years * 0.5
        ):

            return "Moderate"

        else:

            return "Low"


    # --------------------------------------------------------
    # No explicit experience requirement
    # --------------------------------------------------------

    if experience_count >= 2:

        return "Good"

    elif experience_count >= 1:

        return "Moderate"

    else:

        return "Low"