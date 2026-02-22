import sys
import pandas as pd

def enrich_and_filter(input_file):
    """Enriches and filters a CSV of local businesses."""
    df = pd.read_csv(input_file)
    
    # Mock enrichment for demonstration purposes
    # In a real implementation, this would use oc-goplaces and browser tools
    df["website"] = "www.example.com"
    df["reviews"] = 4.5
    df["owner_name"] = "John Doe"
    df["owner_email"] = "john.doe@example.com"
    
    # Filter the DataFrame
    qualified_df = df[(df["reviews"] >= 4.0) & (df["website"].notna())]
    
    # Save the qualified leads to a new CSV
    qualified_df.to_csv("qualified_leads.csv", index=False)
    print(f"Successfully enriched and filtered {len(qualified_df)} leads.")
    print("Saved to qualified_leads.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enrich_and_filter.py <input_file.csv>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    enrich_and_filter(input_file)
