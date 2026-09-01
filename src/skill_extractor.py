import re


# ============================================================
# SKILL DATABASE
# ============================================================

SKILL_DATABASE = {

    # Programming
    "Python": ["python", "python3", "python 3"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript", "ts"],
    "C": ["c programming"],
    "C++": ["c++", "cpp"],
    "C#": ["c#", "c sharp"],
    "Go": ["golang", "go language"],
    "R": ["r programming", "r language"],

    # Web / Backend
    "HTML": ["html", "html5"],
    "CSS": ["css", "css3"],
    "Bootstrap": ["bootstrap"],
    "React": ["react", "react.js", "reactjs"],
    "Angular": ["angular", "angularjs"],
    "Vue": ["vue", "vue.js", "vuejs"],
    "Node.js": ["node.js", "nodejs"],
    "Flask": ["flask"],
    "Django": ["django"],
    "FastAPI": ["fastapi", "fast api"],
    "REST API": [
        "rest api",
        "restful api",
        "rest apis",
        "restful apis"
    ],
    "GraphQL": ["graphql"],
    "HTTP": ["http", "https"],
    "API Development": [
        "api development",
        "api design",
        "backend api"
    ],

    # Databases
    "SQL": ["sql", "sql queries", "sql query"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo db"],
    "SQLite": ["sqlite"],
    "Redis": ["redis"],
    "Database Design": [
        "database design",
        "database schema",
        "schema design"
    ],
    "Relational Databases": [
        "relational database",
        "relational databases"
    ],

    # Data Science
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"],
    "SciPy": ["scipy"],
    "Jupyter": [
        "jupyter",
        "jupyter notebook",
        "jupyter notebooks"
    ],
    "Data Analysis": [
        "data analysis",
        "data analytics",
        "data analyst"
    ],
    "Data Visualization": [
        "data visualization",
        "data visualisation"
    ],
    "Statistics": [
        "statistics",
        "statistical analysis"
    ],

    # Machine Learning
    "Machine Learning": [
        "machine learning",
        "machine-learning",
        "ml"
    ],
    "Scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],
    "Supervised Learning": ["supervised learning"],
    "Unsupervised Learning": ["unsupervised learning"],
    "Regression": [
        "regression",
        "linear regression",
        "logistic regression"
    ],
    "Classification": [
        "classification",
        "classification algorithms"
    ],
    "Clustering": [
        "clustering",
        "cluster analysis"
    ],
    "Feature Engineering": [
        "feature engineering",
        "feature selection"
    ],
    "Model Evaluation": [
        "model evaluation",
        "model validation",
        "cross validation",
        "cross-validation"
    ],
    "Predictive Modeling": [
        "predictive modeling",
        "predictive modelling"
    ],

    # Deep Learning
    "Deep Learning": ["deep learning"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Keras": ["keras"],
    "Neural Networks": [
        "neural network",
        "neural networks"
    ],
    "CNN": [
        "cnn",
        "convolutional neural network",
        "convolutional neural networks"
    ],
    "RNN": [
        "rnn",
        "recurrent neural network",
        "recurrent neural networks"
    ],
    "Transformers": ["transformer", "transformers"],

    # NLP
    "NLP": [
        "nlp",
        "natural language processing"
    ],
    "Sentence Transformers": [
        "sentence transformers",
        "sentence-transformers"
    ],
    "BERT": ["bert"],
    "Text Classification": ["text classification"],
    "Text Embeddings": [
        "text embeddings",
        "text embedding"
    ],
    "Semantic Similarity": ["semantic similarity"],

    # Computer Vision
    "Computer Vision": ["computer vision"],
    "OpenCV": ["opencv", "open cv"],
    "YOLO": [
        "yolo",
        "yolov5",
        "yolov7",
        "yolov8",
        "yolov9",
        "yolov10",
        "yolov11"
    ],
    "Object Detection": ["object detection"],
    "Image Classification": ["image classification"],
    "Image Processing": ["image processing"],

    # Generative AI
    "Artificial Intelligence": [
        "artificial intelligence",
        "ai"
    ],
    "Generative AI": [
        "generative ai",
        "genai",
        "gen ai"
    ],
    "Large Language Models": [
        "large language model",
        "large language models",
        "llm",
        "llms"
    ],
    "Prompt Engineering": ["prompt engineering"],
    "RAG": [
        "rag",
        "retrieval augmented generation",
        "retrieval-augmented generation"
    ],
    "LangChain": ["langchain"],
    "LlamaIndex": [
        "llamaindex",
        "llama index"
    ],

    # Cloud
    "AWS": [
        "aws",
        "amazon web services"
    ],
    "Microsoft Azure": [
        "azure",
        "microsoft azure"
    ],
    "Google Cloud": [
        "google cloud",
        "gcp",
        "google cloud platform"
    ],
    "Cloud Computing": [
        "cloud computing",
        "cloud deployment",
        "cloud services"
    ],
    "AWS EC2": ["ec2", "aws ec2"],
    "AWS S3": ["s3", "aws s3"],

    # DevOps
    "Docker": [
        "docker",
        "docker containers",
        "containerization",
        "containerisation"
    ],
    "Kubernetes": ["kubernetes", "k8s"],
    "CI/CD": [
        "ci/cd",
        "ci cd",
        "continuous integration",
        "continuous deployment",
        "continuous delivery"
    ],
    "GitHub Actions": ["github actions"],
    "Jenkins": ["jenkins"],
    "Linux": ["linux", "ubuntu"],
    "Bash": [
        "bash",
        "shell scripting"
    ],

    # Version Control
    "Git": [
        "git",
        "git version control",
        "version control"
    ],
    "GitHub": ["github"],
    "GitLab": ["gitlab"],

    # Testing
    "Pytest": ["pytest", "py.test"],
    "Unit Testing": [
        "unit testing",
        "unit tests"
    ],
    "Integration Testing": [
        "integration testing",
        "integration tests"
    ],
    "Test Automation": [
        "test automation",
        "automated testing"
    ],

    # Software Engineering
    "Data Structures": ["data structures"],
    "Algorithms": [
        "algorithms",
        "algorithm design"
    ],
    "Data Structures and Algorithms": [
        "data structures and algorithms",
        "data structures & algorithms",
        "dsa"
    ],
    "Object-Oriented Programming": [
        "object oriented programming",
        "object-oriented programming",
        "oop"
    ],
    "Software Development": [
        "software development",
        "software engineering"
    ],
    "Debugging": [
        "debugging",
        "debug"
    ],
    "Problem Solving": [
        "problem solving",
        "problem-solving"
    ],
    "Agile": [
        "agile",
        "agile methodology"
    ],
    "Scrum": ["scrum"],

    # Tools
    "Streamlit": ["streamlit"],
    "VS Code": [
        "vs code",
        "visual studio code"
    ],
    "Postman": ["postman"],
    "Jira": ["jira"],
    "Excel": [
        "excel",
        "microsoft excel"
    ],
    "Power BI": [
        "power bi",
        "powerbi"
    ],
    "Tableau": ["tableau"]
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):

    if not text:
        return ""

    text = str(text).lower()

    text = text.replace("–", "-")
    text = text.replace("—", "-")

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# SKILL SEARCH
# ============================================================

def skill_exists(text, keyword):

    keyword = normalize_text(keyword)

    if not keyword:
        return False

    pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"

    return re.search(
        pattern,
        text,
        flags=re.IGNORECASE
    ) is not None


# ============================================================
# EXTRACT SKILLS
# ============================================================

def extract_skills(text):

    normalized_text = normalize_text(text)

    if not normalized_text:
        return []

    detected_skills = []

    for skill_name, keywords in SKILL_DATABASE.items():

        for keyword in keywords:

            if skill_exists(
                normalized_text,
                keyword
            ):

                detected_skills.append(
                    skill_name
                )

                break

    return list(
        dict.fromkeys(
            detected_skills
        )
    )


# ============================================================
# EXTRACT SKILL DETAILS
# ============================================================

def extract_skill_details(text):

    normalized_text = normalize_text(text)

    results = {}

    if not normalized_text:
        return results

    for skill_name, keywords in SKILL_DATABASE.items():

        for keyword in keywords:

            if skill_exists(
                normalized_text,
                keyword
            ):

                results[skill_name] = keyword

                break

    return results


# ============================================================
# FIND SKILL EVIDENCE
# ============================================================

def find_skill_evidence(
    text,
    skill_name
):
    """
    Find the original sentence/line containing a skill.

    Returns:
        Evidence sentence or None.
    """

    if not text:
        return None

    # --------------------------------------------------------
    # Get possible keywords
    # --------------------------------------------------------

    keywords = SKILL_DATABASE.get(
        skill_name,
        [skill_name]
    )

    # --------------------------------------------------------
    # Split resume into useful pieces.
    #
    # First try line-by-line because resumes usually have
    # bullet points.
    # --------------------------------------------------------

    lines = re.split(
        r"[\r\n]+",
        str(text)
    )


    # --------------------------------------------------------
    # Search individual lines
    # --------------------------------------------------------

    for line in lines:

        line = line.strip()

        if not line:
            continue

        normalized_line = normalize_text(
            line
        )

        for keyword in keywords:

            if skill_exists(
                normalized_line,
                keyword
            ):

                return line


    # --------------------------------------------------------
    # If no line was found, split into sentences
    # --------------------------------------------------------

    sentences = re.split(
        r"(?<=[.!?])\s+",
        str(text)
    )


    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        normalized_sentence = normalize_text(
            sentence
        )

        for keyword in keywords:

            if skill_exists(
                normalized_sentence,
                keyword
            ):

                return sentence


    return None


# ============================================================
# EXTRACT SKILL EVIDENCE FOR MULTIPLE SKILLS
# ============================================================

def extract_skill_evidence(
    text,
    skills
):
    """
    Return a dictionary:

        {
            "Python": "...resume evidence...",
            "Flask": "...resume evidence..."
        }
    """

    evidence = {}

    for skill in skills:

        evidence[skill] = find_skill_evidence(
            text,
            skill
        )

    return evidence


# ============================================================
# SKILL GROUPS
# ============================================================

SKILL_GROUPS = {

    "Data Structures and Algorithms": {
        "data structures",
        "algorithms",
        "data structures and algorithms"
    },

    "SQL / Databases": {
        "sql",
        "relational databases",
        "database design"
    },

    "Testing": {
        "pytest",
        "unit testing",
        "integration testing",
        "test automation"
    },

    "Cloud / AWS": {
        "aws",
        "aws ec2",
        "aws s3",
        "cloud computing",
        "cloud deployment",
        "cloud services"
    },

    "Version Control": {
        "git",
        "github",
        "gitlab"
    },

    "API Development": {
        "rest api",
        "api development",
        "graphql"
    },

    "Machine Learning": {
        "machine learning",
        "scikit-learn",
        "supervised learning",
        "unsupervised learning",
        "regression",
        "classification",
        "clustering"
    }
}


# ============================================================
# NORMALIZE RELATED SKILLS
# ============================================================

def normalize_skills(skills):

    if not skills:
        return []

    normalized = set()

    skill_set = {
        str(skill).strip().lower()
        for skill in skills
    }

    grouped_members = set()

    for group_name, group_members in SKILL_GROUPS.items():

        grouped_members.update(
            group_members
        )

        if skill_set.intersection(
            group_members
        ):

            normalized.add(
                group_name
            )

    for skill in skills:

        skill_lower = (
            str(skill)
            .strip()
            .lower()
        )

        if skill_lower not in grouped_members:

            normalized.add(
                skill
            )

    return sorted(
        normalized
    )