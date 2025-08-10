from mission_processor import load_mission_data, filter_by_status, count_by_priority
from personnel_analyzer import load_personnel_data, filter_by_clearance, group_by_unit
from report_generator import generate_mission_summary, generate_personnel_report


def show_menu() -> None:
    print("=== ARMY INTELLIGENCE DATA PROCESSOR ===\n")
    print("1. Mission Summary")
    print("2. Personnel Report")
    print("3. Filter Active Missions")
    print("4. Show Top Secret Personnel")
    print("5. Exit")


def handle_choice(choice: str, missions, personnel) -> bool:
    """
    Returns False to exit, True to continue.
    """
    if choice == "1":
        # Summary of missions (consider using count_by_priority inside your generator)
        print()
        print(generate_mission_summary(missions))
        print()
    elif choice == "2":
        # Personnel report (you can enhance this to group_by_unit if desired)
        print()
        print(generate_personnel_report(personnel))
        print()
    elif choice == "3":
        # List active missions
        print()
        active = filter_by_status(missions, "Active")
        if not active:
            print("No active missions found.")
        else:
            for m in active:
                print(f"Mission {m.get('id', 'N/A')}: {m.get('location', 'Unknown')}")
        print()
    elif choice == "4":
        # List Top Secret personnel
        print()
        cleared = filter_by_clearance(personnel, "Top Secret")
        if not cleared:
            print("No Top Secret personnel found.")
        else:
            for p in cleared:
                rank = p.get("rank", "Rank?")
                name = p.get("name", "Name?")
                unit = p.get("unit", "Unit?")
                print(f"{rank} {name} — Unit {unit}")
        print()
    elif choice == "5":
        print("\nSession terminated.")
        return False
    else:
        print("\nInvalid selection. Please choose 1–5.\n")
    return True


def main() -> None:
    try:
        missions = load_mission_data()
    except Exception as e:
        print(f"Failed to load missions: {e}")
        return

    try:
        personnel = load_personnel_data()
    except Exception as e:
        print(f"Failed to load personnel: {e}")
        return

    try:
        while True:
            show_menu()
            choice = input("\nSelect option (1–5): ").strip()
            if not handle_choice(choice, missions, personnel):
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nSession terminated.")


if __name__ == "__main__":
    main()
