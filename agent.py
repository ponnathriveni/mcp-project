from tools import web_search, pdf_search

def research(topic):

    web_data = web_search(topic)

    pdf_data = pdf_search(topic)

    report = f"""
Research Report

Topic: {topic}

Web Findings:
{web_data}

PDF Findings:
{pdf_data}

Conclusion:
AI has significant applications in healthcare and improves efficiency.
"""

    return report