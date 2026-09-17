# Learning roadmap for missing skills

SKILL_ROADMAP = {

    "Python": "Learn Python fundamentals, OOP, functions, modules, and problem solving.",

    "Java": "Learn Java fundamentals, OOP, collections, exception handling, and basic problem solving.",

    "C": "Learn C fundamentals, pointers, arrays, functions, structures, and memory management.",

    "SQL": "Learn SQL queries, joins, subqueries, aggregate functions, and database design.",

    "MySQL": "Practice MySQL databases, table design, joins, indexing, and CRUD operations.",

    "Git": "Learn Git commands, branching, merging, commits, and collaborative workflows.",

    "GitHub": "Practice GitHub repositories, pull requests, issues, and collaboration workflows.",

    "Data Structures": "Study arrays, linked lists, stacks, queues, trees, hash tables, and graphs.",

    "Algorithms": "Study sorting, searching, recursion, greedy algorithms, and basic dynamic programming.",

    "REST API": "Learn HTTP methods, REST principles, JSON, API development, and API testing.",

    "Spring Boot": "Learn Spring Boot fundamentals, REST controllers, services, repositories, and database integration.",

    "HTML": "Learn HTML structure, semantic elements, forms, tables, and accessibility basics.",

    "CSS": "Learn CSS selectors, box model, Flexbox, Grid, responsive design, and layouts.",

    "JavaScript": "Learn JavaScript fundamentals, DOM manipulation, events, ES6, and asynchronous programming.",

    "NumPy": "Learn NumPy arrays, indexing, mathematical operations, and numerical computing.",

    "Pandas": "Practice DataFrames, data cleaning, filtering, grouping, merging, and analysis.",

    "Excel": "Learn formulas, pivot tables, charts, filtering, and data analysis in Excel.",

    "Statistics": "Study descriptive statistics, probability, distributions, correlation, and hypothesis testing.",

    "Data Visualization": "Learn how to create meaningful charts using Matplotlib, Seaborn, or Plotly.",

    "Scikit-learn": "Practice preprocessing, feature engineering, classification, regression, clustering, and model evaluation.",

    "Machine Learning": "Learn supervised and unsupervised learning, model training, evaluation, and feature engineering.",

    "Deep Learning": "Learn neural networks, backpropagation, CNNs, RNNs, and modern deep learning workflows.",

    "NLP": "Learn text preprocessing, embeddings, text classification, named entity recognition, and transformers.",

    "LLM": "Learn large language model concepts, prompting, embeddings, model APIs, and LLM application development.",

    "Generative AI": "Learn generative AI concepts, foundation models, prompting, RAG, and AI application development.",

    "RAG": "Learn document retrieval, embeddings, vector databases, chunking, and retrieval-augmented generation.",

    "PyTorch": "Learn tensors, datasets, neural networks, training loops, and model evaluation using PyTorch.",

    "AWS": "Learn AWS fundamentals including EC2, S3, IAM, databases, and basic cloud deployment."
}


def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        recommendation = SKILL_ROADMAP.get(
            skill,
            f"Learn the fundamentals and practice projects related to {skill}."
        )

        roadmap.append({
            "skill": skill,
            "recommendation": recommendation
        })

    return roadmap