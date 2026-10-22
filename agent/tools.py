"""CampusPilot AI tools — synthetic campus knowledge base for an Indian engineering college.

All tools are READ-ONLY. The agent provides information and guidance only; it never performs
official actions, submits requests, or modifies any record. Clearly labelled as DEMO DATA.

Replace the in-memory data with real college API calls for production use.
"""

from __future__ import annotations

from strands import tool

# ---------------------------------------------------------------------------
# DEMO DATA — fictional Indian engineering college (not official policy)
# ---------------------------------------------------------------------------

KNOWLEDGE_BASE = {
    "exam_schedule": [
        {"subject": "Advanced Algorithms",       "code": "CS601", "date": "2026-11-10", "time": "10:00", "room": "Block A, Hall 3"},
        {"subject": "Machine Learning",          "code": "CS602", "date": "2026-11-10", "time": "10:00", "room": "Block B, Hall 1"},
        {"subject": "Computer Networks",         "code": "CS603", "date": "2026-11-12", "time": "14:00", "room": "Block A, Hall 2"},
        {"subject": "Database Systems",          "code": "CS604", "date": "2026-11-14", "time": "10:00", "room": "Block C, Hall 4"},
        {"subject": "Software Engineering",      "code": "CS605", "date": "2026-11-17", "time": "14:00", "room": "Block B, Hall 3"},
        {"subject": "Operating Systems",         "code": "CS606", "date": "2026-11-19", "time": "10:00", "room": "Block A, Hall 1"},
    ],
    "timetable": {
        "Monday":    ["Advanced Algorithms (CS601) 09:00", "Machine Learning Lab (CS602L) 14:00"],
        "Tuesday":   ["Computer Networks (CS603) 09:00",  "Database Systems (CS604) 11:00"],
        "Wednesday": ["Software Engineering (CS605) 09:00","Advanced Algorithms (CS601) 14:00"],
        "Thursday":  ["Machine Learning (CS602) 09:00",   "Operating Systems (CS606) 14:00"],
        "Friday":    ["Database Systems (CS604) 09:00",   "Computer Networks Lab (CS603L) 14:00"],
    },
    "faqs": [
        {"q": "How do I apply for a hall ticket?",
         "a": "Log in to the student portal (portal.srcollege.edu.in), go to Examinations → Hall Ticket, and download it after paying the exam fee. Hall tickets are available 10 days before exams."},
        {"q": "What is the attendance requirement?",
         "a": "A minimum of 75% attendance is required in each subject to be eligible to appear for the semester examination. Students below 65% are detained. Condonation up to 65% may be granted by the HOD for medical reasons with supporting documents."},
        {"q": "How are internal marks calculated?",
         "a": "Internal assessment is 40 marks: two cycle tests (10+10), one model exam (15), and assignment/attendance (5). The best score of the two cycle tests is taken."},
        {"q": "What is the arrear policy?",
         "a": "Students with arrears can register for supplementary exams held in April/May and November/December. A maximum of 3 attempts are permitted per subject before additional approvals are required."},
        {"q": "How do I change my elective subject?",
         "a": "Submit an elective change request to the Academic Section within the first two weeks of the semester. It is subject to seat availability and HOD approval."},
        {"q": "What is the grading system?",
         "a": "The college uses a 10-point CGPA system. O (Outstanding) = 10, A+ = 9, A = 8, B+ = 7, B = 6, C = 5. Passing minimum is C grade (50 marks out of 100)."},
    ],
    "placement_resources": {
        "Python": {
            "topics": ["Data structures", "OOP concepts", "File I/O", "Decorators and generators",
                       "Standard library (collections, itertools)", "NumPy and Pandas basics",
                       "Writing clean Pythonic code"],
            "practice": ["HackerRank Python track", "LeetCode easy/medium problems in Python",
                         "Build a small CLI project"],
            "mock_questions": [
                "Explain the difference between a list and a tuple.",
                "What is a Python decorator? Write an example.",
                "How does Python manage memory? Explain garbage collection.",
                "Write a function to find all duplicates in a list.",
                "What is the difference between __str__ and __repr__?",
                "Explain list comprehensions vs generator expressions.",
                "What are *args and **kwargs?",
            ],
        },
        "Data Structures": {
            "topics": ["Arrays and strings", "Linked lists", "Stacks and queues",
                       "Trees (BST, AVL)", "Graphs (BFS, DFS)", "Dynamic programming",
                       "Sorting algorithms"],
            "practice": ["LeetCode Top 100 Liked", "GeeksForGeeks practice", "Codeforces Div 3"],
        },
        "System Design": {
            "topics": ["Scalability basics", "Load balancing", "Caching", "Database design",
                       "REST API design", "Microservices overview"],
        },
        "Aptitude": {
            "topics": ["Quantitative aptitude", "Logical reasoning", "Verbal ability"],
            "practice": ["IndiaBIX", "PrepInsta", "Fresherworld"],
        },
    },
    "contacts": {
        "timetable_conflict":   {"role": "Academic Section / Examination Cell",   "email": "academics@srcollege.edu.in",  "office": "Admin Block, Room 105"},
        "medical_leave":        {"role": "Head of Department (HOD)",              "email": "hod.cse@srcollege.edu.in",    "office": "CSE Dept, Room 201"},
        "grade_dispute":        {"role": "Controller of Examinations",            "email": "coe@srcollege.edu.in",        "office": "Admin Block, Room 110"},
        "financial_aid":        {"role": "Student Welfare Officer",               "email": "welfare@srcollege.edu.in",    "office": "Admin Block, Room 108"},
        "placement":            {"role": "Training and Placement Officer",        "email": "placements@srcollege.edu.in", "office": "Placement Block, Room 301"},
        "general_admin":        {"role": "Student Services Desk",                 "email": "studentservices@srcollege.edu.in", "office": "Admin Block, Ground Floor"},
    },
}


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@tool
def search_knowledge_base(query: str) -> dict:
    """Search the campus FAQ and policy knowledge base for answers to academic questions."""
    q = query.lower()
    matches = [
        {"question": item["q"], "answer": item["a"]}
        for item in KNOWLEDGE_BASE["faqs"]
        if any(word in item["q"].lower() or word in item["a"].lower()
               for word in q.split() if len(word) > 3)
    ]
    if matches:
        return {"source": "DEMO DATA — fictional college policy", "results": matches[:3]}
    return {"source": "DEMO DATA — fictional college policy",
            "results": [],
            "note": "No direct match found. Try rephrasing or contact the Student Services Desk."}


@tool
def get_exam_schedule(subject_filter: str = "") -> dict:
    """Look up the upcoming exam schedule, optionally filtered by subject name or code."""
    exams = KNOWLEDGE_BASE["exam_schedule"]
    if subject_filter:
        f = subject_filter.lower()
        exams = [e for e in exams if f in e["subject"].lower() or f in e["code"].lower()]
    return {
        "source": "DEMO DATA — fictional exam schedule",
        "note": "This is synthetic data. Verify dates on the official student portal.",
        "exams": exams,
    }


@tool
def get_timetable(day: str = "") -> dict:
    """Get the weekly class timetable, optionally for a specific day (e.g. Monday, Tuesday)."""
    tt = KNOWLEDGE_BASE["timetable"]
    if day:
        d = day.strip().capitalize()
        if d in tt:
            return {"source": "DEMO DATA — fictional timetable", "day": d, "classes": tt[d]}
        return {"source": "DEMO DATA — fictional timetable",
                "error": f"Day '{day}' not recognised. Use Monday–Friday."}
    return {"source": "DEMO DATA — fictional timetable", "timetable": tt}


@tool
def get_placement_resources(topic: str) -> dict:
    """Get study resources, practice links and mock questions for a placement or interview topic."""
    resources = KNOWLEDGE_BASE["placement_resources"]
    t = topic.strip()
    # exact match first
    if t in resources:
        return {"topic": t, "resources": resources[t]}
    # case-insensitive partial match
    for key, val in resources.items():
        if t.lower() in key.lower() or key.lower() in t.lower():
            return {"topic": key, "resources": val}
    available = list(resources.keys())
    return {
        "error": f"No resources found for '{topic}'.",
        "available_topics": available,
        "suggestion": f"Try one of: {', '.join(available)}",
    }


@tool
def get_escalation_contact(issue_type: str) -> dict:
    """Get the correct college authority to contact for a sensitive or official request.

    issue_type must be one of: timetable_conflict, medical_leave, grade_dispute,
    financial_aid, placement, general_admin.
    """
    contacts = KNOWLEDGE_BASE["contacts"]
    key = issue_type.strip().lower().replace(" ", "_")
    if key in contacts:
        c = contacts[key]
        return {
            "source": "DEMO DATA — fictional contact details",
            "issue_type": key,
            "contact": c,
            "note": (
                "CampusPilot AI cannot submit requests or approvals on your behalf. "
                "Please contact the authority listed above directly."
            ),
        }
    return {
        "error": f"Unknown issue type '{issue_type}'.",
        "valid_types": list(contacts.keys()),
    }


TOOLS = [
    search_knowledge_base,
    get_exam_schedule,
    get_timetable,
    get_placement_resources,
    get_escalation_contact,
]
