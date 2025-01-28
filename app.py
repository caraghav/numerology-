import streamlit as st
import json

# Load predictions from JSON file
@st.cache_data
def load_data():
    with open("numerology_dbgit.json", "r") as file:
        return json.load(file)

# Function to calculate the Life Path Number (Destiny Number)
def calculate_life_path(dob):
    digits = [int(d) for d in dob if d.isdigit()]
    while len(digits) > 1:
        digits = [int(digit) for digit in str(sum(digits))]
    return digits[0]

# Function to calculate the Birth Number (Day Number)
def calculate_birth_number(day):
    while day > 9:
        day = sum(int(digit) for digit in str(day))
    return day

# Main Streamlit app
def main():
    st.title("Numerology Bot")
    st.write("Enter your date of birth to discover your numerology insights.")
    
    # Load data from JSON
    numerology_data = load_data()

    # Input: Date of Birth
    dob = st.text_input("Enter your Date of Birth (DD-MM-YYYY):", "")

    if dob:
        try:
            day, month, year = map(int, dob.split("-"))
            
            # Calculate Birth Number and Destiny Number
            birth_number = calculate_birth_number(day)
            life_path_number = calculate_life_path(dob)

            # Display Results
            st.subheader("Numerology Results")
            st.write(f"**Birth Number:** {birth_number}")
            st.write(f"**Destiny Number (Life Path):** {life_path_number}")
            
            # Fetch Predictions from JSON
            birth_prediction = numerology_data["birth_number"].get(str(birth_number), "No prediction available.")
            destiny_prediction = numerology_data["destiny_number"].get(str(life_path_number), "No prediction available.")
            combination_key = f"{birth_number}-{life_path_number}"
            combination_prediction = numerology_data["combination"].get(combination_key, "No combination prediction available.")

            # Display Predictions
            st.subheader("Detailed Predictions")
            st.write(f"**Birth Number Prediction:** {birth_prediction}")
            st.write(f"**Destiny Number Prediction:** {destiny_prediction}")
            st.write(f"**Combination Prediction (Birth-Destiny):** {combination_prediction}")

        except ValueError:
            st.error("Invalid date format. Please enter the date in DD-MM-YYYY format.")

# Run the app
if __name__ == "__main__":
    main()
