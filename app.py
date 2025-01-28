import datetime
import json
import streamlit as st

# Load Numerology Database
with open("numerology_db.json") as f:
    numerology_db = json.load(f)

def reduce_number(n, allow_master=True):
    if n in [11, 22, 33] and allow_master:
        return n
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def calculate_life_path(dob):
    day = reduce_number(dob.day, allow_master=False)
    month = reduce_number(dob.month, allow_master=False)
    year = reduce_number(dob.year, allow_master=False)
    total = day + month + year
    return reduce_number(total)

def get_karmic_debt(dob):
    debts = []
    day, month, year = dob.day, dob.month, dob.year
    if day in [13, 14, 16, 19]: debts.append(f"Day {day}")
    if month in [13, 14, 16, 19]: debts.append(f"Month {month}")
    if year in [13, 14, 16, 19]: debts.append(f"Year {year}")
    return debts

def generate_report(dob):
    report = {}
    # Core Numbers
    report["Life Path"] = calculate_life_path(dob)
    report["Birthday"] = reduce_number(dob.day, allow_master=False)
    report["Universal Year"] = reduce_number(datetime.datetime.now().year)
    # Challenges
    challenge1 = abs(dob.month - dob.day)
    challenge2 = abs(dob.day - reduce_number(dob.year))
    report["Challenges"] = [challenge1, challenge2]
    # Karmic Debt
    report["Karmic Debt"] = get_karmic_debt(dob)
    return report

# Streamlit App
st.title("🔮 Numerology Bot")
dob = st.date_input("Enter your birthdate:", max_value=datetime.date.today())

if st.button("Generate Report"):
    report = generate_report(dob)
    st.subheader(f"Numerology Report for {dob.strftime('%d-%b-%Y')}")
    
    # Life Path
    life_path = report["Life Path"]
    st.write(f"### Life Path Number: {life_path}")
    st.write(numerology_db["Life Path"][str(life_path)])
    
    # Birthday
    birthday = report["Birthday"]
    st.write(f"### Birthday Number: {birthday}")
    st.write(numerology_db["Birthday"][str(birthday)])
    
    # Challenges
    st.write("### Life Challenges")
    for i, challenge in enumerate(report["Challenges"], 1):
        st.write(f"**Challenge {i} ({challenge})**: {numerology_db['Challenges'][str(challenge)]}")
    
if report["Karmic Debt"]:
    st.write("### Karmic Debt")
    for debt in report["Karmic Debt"]:
        st.write(f"- {numerology_db['Karmic Debt'][debt.split()[1]]}")
else:
    st.write("No Karmic Debt found.")
    
    # Number Combinations
    st.write("### Powerful Combinations")
    combo_key = f"{report['Life Path']}-{report['Birthday']}"
    st.write(numerology_db["Combinations"].get(combo_key, "No major combinations found."))