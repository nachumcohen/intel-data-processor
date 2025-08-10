from mission_processor import load_mission_data

def main():
    print("=== ARMY INTELLIGENCE DATA PROCESSOR ===")
    missions = load_mission_data()
    print(f"Loaded {len(missions)} missions")

if __name__ == "__main__":
    main()
