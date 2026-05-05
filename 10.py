import pickle
import os

FN = "sports_camp_records.dat"


def load_records():
    """Load participant records from the binary file."""
    if not os.path.exists(FN):
        return []
    try:
        with open(FN, "rb") as file:
            return pickle.load(file)
    except (EOFError, pickle.UnpicklingError):
        return []


def save_records(records):
    """Save participant records to the binary file."""
    with open(FN, "wb") as file:
        pickle.dump(records, file)


def display_record(record):
    print(f"ID: {record['id']}")
    print(f"Name: {record['name']}")
    print(f"Hours Practiced: {record['hours']:.2f}")
    print("-" * 30)


def add_participant():
    records = load_records()
    try:
        participant_id = int(input("Enter participant ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return

    if any(rec["id"] == participant_id for rec in records):
        print("A participant with that ID already exists.")
        return

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        hours = float(input("Enter hours practiced: ").strip())
    except ValueError:
        print("Invalid hours. Please enter a numeric value.")
        return

    records.append({"id": participant_id, "name": name, "hours": hours})
    save_records(records)
    print("Participant added successfully.")


def view_all_participants():
    records = load_records()
    if not records:
        print("No participants found.")
        return

    print("\nAll participants:\n" + "=" * 30)
    for record in records:
        display_record(record)


def search_by_id():
    records = load_records()
    if not records:
        print("No participants found.")
        return

    try:
        participant_id = int(input("Enter participant ID to search: ").strip())
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return

    found = next((rec for rec in records if rec["id"] == participant_id), None)
    if found:
        print("Participant found:")
        display_record(found)
    else:
        print("Participant not found.")


def update_practice_hours():
    records = load_records()
    if not records:
        print("No participants found.")
        return

    try:
        participant_id = int(input("Enter participant ID to update: ").strip())
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return

    for record in records:
        if record["id"] == participant_id:
            try:
                hours = float(input("Enter new hours practiced: ").strip())
            except ValueError:
                print("Invalid hours. Please enter a numeric value.")
                return

            record["hours"] = hours
            save_records(records)
            print("Practice hours updated.")
            return

    print("Participant not found.")


def delete_participant():
    records = load_records()
    if not records:
        print("No participants found.")
        return

    try:
        participant_id = int(input("Enter participant ID to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter an integer.")
        return

    updated = [rec for rec in records if rec["id"] != participant_id]
    if len(updated) == len(records):
        print("Participant not found.")
        return

    save_records(updated)
    print("Participant deleted successfully.")


def show_more_than_40_hours():
    records = load_records()
    filtered = [rec for rec in records if rec["hours"] > 40]
    if not filtered:
        print("No participants with more than 40 practice hours.")
        return

    print("\nParticipants with more than 40 practice hours:\n" + "=" * 30)
    for record in filtered:
        display_record(record)


def count_total_participants():
    records = load_records()
    print(f"Total participants: {len(records)}")


def sort_participants_by_hours():
    records = load_records()
    if not records:
        print("No participants found.")
        return

    sorted_records = sorted(records, key=lambda rec: rec["hours"], reverse=True)
    print("\nParticipants sorted by practice hours (highest first):\n" + "=" * 30)
    for record in sorted_records:
        display_record(record)


def print_menu():
    print("\nSports Camp Participant Manager")
    print("1. Add new participant")
    print("2. View all participants")
    print("3. Search by Participant ID")
    print("4. Update practice hours")
    print("5. Delete a participant")
    print("6. Show participants with more than 40 practice hours")
    print("7. Count total participants")
    print("8. Sort participants by practice hours and display")
    print("9. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter a choice: ").strip()
        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        choice = int(choice)

        if choice == 1:
            add_participant()
        elif choice == 2:
            view_all_participants()
        elif choice == 3:
            search_by_id()
        elif choice == 4:
            update_practice_hours()
        elif choice == 5:
            delete_participant()
        elif choice == 6:
            show_more_than_40_hours()
        elif choice == 7:
            count_total_participants()
        elif choice == 8:
            sort_participants_by_hours()
        elif choice == 9:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 9.")
