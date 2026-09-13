import pandas as pd

class DataCleaningAgent:

    def clean_data(self, input_file, output_file):

        # Read the input CSV
        data = pd.read_csv(input_file)

        # Remove duplicate records using the data columns
        data = data.drop_duplicates(
            subset=["Name", "Age", "City", "Salary", "Email"]
        )

        # Remove extra spaces from text columns
        data["Name"] = data["Name"].astype("string").str.strip()
        data["City"] = data["City"].astype("string").str.strip()
        data["Email"] = data["Email"].astype("string").str.strip()

        # Standardize Name and City
        data["Name"] = data["Name"].str.title()
        data["City"] = data["City"].str.title()

        # Convert Age and Salary to numbers
        data["Age"] = pd.to_numeric(
            data["Age"], errors="coerce"
        )
        data["Salary"] = pd.to_numeric(
            data["Salary"], errors="coerce"
        )

        # Fill missing Age with the median
        data["Age"] = data["Age"].fillna(
            data["Age"].median()
        )

        # Fill missing Salary with the median
        data["Salary"] = data["Salary"].fillna(
            data["Salary"].median()
        )

        # Fill missing City with the most common value
        data["City"] = data["City"].fillna(
            data["City"].mode()[0]
        )

        # Fill missing Email with the most common value
        data["Email"] = data["Email"].fillna(
            data["Email"].mode()[0]
        )

        # Save the cleaned dataset
        data.to_csv(output_file, index=False)

        return data


# Create the agent
agent = DataCleaningAgent()

# Run the cleaning process
cleaned_data = agent.clean_data(
    "sample_input.csv",
    "cleaned_output.csv"
)

print("DATA CLEANING AI AGENT")
print("Cleaning completed successfully!")
print("Output file: cleaned_output.csv")
print(cleaned_data.to_string(index=False))
