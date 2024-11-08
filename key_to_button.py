button_mapping = {
    # 1: {"push": "E", "pull": "G"},
    # 2: {"push": "G", "pull": "B"},
    3: {"push": "C", "pull": "D"},
    4: {"push": "E", "pull": "F"},
    5: {"push": "G", "pull": "A"},
    6: {"push": "C", "pull": "B"}, # the funny one
    7: {"push": "E", "pull": "D"},
    8: {"push": "G", "pull": "F"},
    9: {"pull": "A"},              # "push": "C",
    # 10: {"push": "E", "pull": "B"}
}

note_to_button: dict[tuple[str, str], list[int]] = {}
for button, notes in button_mapping.items():
    for action, note in notes.items():
        if (note, action) not in note_to_button:
            note_to_button[(note, action)] = []
        note_to_button[(note, action)].append(button)

def get_button_sequences(notes, mode="both"):
    sequences = {"verbose": [], "simple": []}
    for note in notes:
        options = []
        for action in ["push", "pull"]:
            buttons = note_to_button.get((note, action), [])
            for button in buttons:
                notation = f"{button}'" if action == "pull" else f"{button}"
                if mode in ["verbose", "both"]:
                    options.append(f"Button {button} - {action.capitalize()}")
                if mode in ["simple", "both"]:
                    options.append(notation)
                    
        # Only add the first option per note in simple mode
        if mode in ["verbose", "both"]:
            sequences["verbose"].append(options)
        if mode in ["simple", "both"]:
            sequences["simple"].append([options[0]])  # Only the first option in simple mode
    return sequences

def display_sequences(sequences, mode="simple"):
    if mode == "simple":
        simple_lines = [" | ".join(options) for options in sequences["simple"]]
        return " | ".join(simple_lines)
    elif mode == "verbose":
        verbose_lines = [" / ".join(options) for options in sequences["verbose"]]
        return "\n".join(verbose_lines)

def test_get_button_sequences():
    notes = ["C", "D", "F", "G", "A", "G", "F"]
    expected_simple_output = "3 | 3' | 4' | 5 | 5' | 5 | 4'"
    expected_verbose_output = (
        "Button 3 - Push / Button 6 - Push\n"
        "Button 3 - Pull / Button 7 - Pull\n"
        "Button 4 - Pull / Button 8 - Pull\n"
        "Button 5 - Push / Button 8 - Push\n"
        "Button 5 - Pull / Button 9 - Pull\n"
        "Button 5 - Push / Button 8 - Push\n"
        "Button 4 - Pull / Button 8 - Pull"
    )
    
    # Test simple mode
    sequences_simple = get_button_sequences(notes, mode="simple")
    output_simple = display_sequences(sequences_simple, mode="simple")
    assert output_simple == expected_simple_output, f"Simple mode test failed: expected '{expected_simple_output}' but got '{output_simple}'"
    
    # Test verbose mode
    sequences_verbose = get_button_sequences(notes, mode="verbose")
    output_verbose = display_sequences(sequences_verbose, mode="verbose")
    assert output_verbose == expected_verbose_output, f"Verbose mode test failed: expected '{expected_verbose_output}' but got '{output_verbose}'"
    
    print("All tests passed!")

# Run the tests
test_get_button_sequences()
