import json
import os

def run_setup():
    """Interactive setup wizard for LinkedIn Automator."""
    print("--- LinkedIn Automator Setup Wizard ---")

    config = {}

    print("\n--- Your Profile ---")
    config["name"] = input("What is your full name? ")
    config["company"] = input("What is your company name? ")
    config["role"] = input("What is your job title? ")
    config["bio"] = input("Provide a brief, one-sentence bio: ")

    print("\n--- Ideal Customer Profile (ICP) ---")
    config["icp"] = {}
    config["icp"]["titles"] = input("Enter target job titles (comma-separated): ").split(",")
    config["icp"]["industries"] = input("Enter target industries (comma-separated): ").split(",")
    config["icp"]["company_sizes"] = input("Enter target company sizes (e.g., 11-50, 51-200, comma-separated): ").split(",")
    config["icp"]["keywords"] = input("Enter keywords to look for in profiles (comma-separated): ").split(",")

    print("\n--- Communication Style ---")
    config["voice"] = input("Describe your desired communication style (e.g., casual and direct, formal and insightful): ")

    # Create directories
    if not os.path.exists("/home/ubuntu/linkedin-automator/tracking"):
        os.makedirs("/home/ubuntu/linkedin-automator/tracking")

    # Save config
    config_path = "/home/ubuntu/linkedin-automator/config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

    print(f"\nConfiguration saved to {config_path}")
    print("Setup complete. You can now use the other LinkedIn Automator functions.")

if __name__ == "__main__":
    run_setup()
