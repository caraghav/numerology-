import datetime
import json
import streamlit as st

# Load Numerology Database
with open("numerology_db.json") as f:
    numerology_db = json.load(f)

# Helper function to reduce a number
def reduce_number(n, allow_master=True):
    if n in [11, 22, 33] and allow_master:
        return n
    while n > 9:
        n = sum(map(int, str(n)))
    return n

# Function to calculate Karmic Debt (dummy implementation)
def get_karmic_debt(dob):
    # Add your Karmic Debt logic here
    return [13, 14]  # Example output

# Function to generate the Numerology Report
def generate_report(dob):
    challenge1 = abs(dob.month - dob.day)
    challenge2 = abs(dob.day - reduce_number(dob.year))
    report = {
        "Challenges": [challenge1, challenge2],
        "Karmic Debt": get_karmic_debt(dob),
    }
    return report

# Streamlit App UI
st.title("🔮 Numerology Bot")
dob = st.date_input("Enter your birthdate:", max_value=datetime.date.today())

if st.button("Generate Report"):
    report = generate_report(dob)
    st.subheader(f"Numerology Report for {dob.strftime('%d-%b-%Y')}")

    # Display challenges
    for i, challenge in enumerate(report["Challenges"], start=1):
        try:
            challenge_description = numerology_db["Challenges"][str(challenge)]
        except KeyError:
            challenge_description = "Description not found in the database."
        st.write(f"**Challenge {i} ({challenge})**: {challenge_description}")

    # Display Karmic Debt
    st.subheader("Karmic Debt")
    for debt in report["Karmic Debt"]:
        try:
            debt_description = numerology_db["Karmic Debt"][str(debt)]
        except KeyError:
            debt_description = "Description not found in the database."
        st.write(f"**Karmic Debt {debt}**: {debt_description}")
