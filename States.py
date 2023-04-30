import random

def main():
    state_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }

    # I literally could not name 4 of these capitals

    # Initialize statistics dictionary with 'correct' and 'wrong' keys for each state
    stats = {state: {'correct': 0, 'wrong': 0} for state in state_capitals.keys()}

    # Welcome message
    print("Welcome to the State Capitals Game!")
    print("You'll be prompted to guess the capital of a given state.")

    # Main game loop
    while True:
        # Shuffle the states to present them in random order
        states = list(state_capitals.keys())
        random.shuffle(states)

        # Loop through all the states
        for state in states:
            # Prompt the user for the capital, offering a hint option
            answer = input(f"What is the capital of {state}? (Type 'hint' for a hint) ")

            # If the user types 'hint', provide the first 3 letters of the capital
            if answer.strip().lower() == 'hint':
                hint = state_capitals[state][:3]
                print(f"Hint: The capital starts with '{hint}'.")
                answer = input(f"What is the capital of {state}? ")

            # Check if the user's answer is correct
            if answer.strip().title() == state_capitals[state]:
                print("Correct!")
                stats[state]['correct'] += 1
            else:
                print(f"Wrong! The correct answer is {state_capitals[state]}.")
                stats[state]['wrong'] += 1

            # Show the user's progress for the current state
            total = stats[state]['correct'] + stats[state]['wrong']
            print(f"You've answered correctly {stats[state]['correct']} out of {total} times for {state}.\n")

        # After all states have been gone through, ask if the user wants to play again
        play_again = input("You've gone through all 50 states. Would you like to play again? (yes/no) ")
        if play_again.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()
