#ex4
actions = []

def perform_action(action):
    print(f"Performing action {action}")
    actions.append(action)

def undo():
        if actions:
            last_action = actions.pop()
            print(f"Undoing: {last_action}")
        else:
            print("No actions to undo.")
perform_action("Add invoice")
perform_action("Delete expense")
undo()
undo()
undo()