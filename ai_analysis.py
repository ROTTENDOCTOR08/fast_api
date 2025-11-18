import google.generativeai as genai

genai.configure(api_key="your_own_key")

def generate_ai_report(sector: str, news_list):

    prompt = f"""
    Generate a trade opportunity report.

    SECTOR: {sector}

    LATEST NEWS:
    {news_list}

    REQUIRED SECTIONS:
    ## Market Overview
    ## Trade Opportunities
    ## Major Companies
    ## Government Policies
    ## Risk Factors
    ## Final Verdict (BUY / HOLD / WAIT)

    KEEP IT INDIA-FOCUSED
    """

    try:
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(prompt)
        return response.text


    except Exception as e:
        raise RuntimeError(f"AI report generation error: {e}")
