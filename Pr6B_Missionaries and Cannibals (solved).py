def print_state(state):
    missionaries_left, cannibals_left, boat_position = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    print(
        f"Left: {missionaries_left}M {cannibals_left}C | Right: {missionaries_right}M {cannibals_right}C",
        end="",
    )
    if boat_position == "left":
        print(" <- Boat")
    else:
        print(" Boat ->")
def is_valid_state(state):
    missionaries_left, cannibals_left, _ = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if (
        missionaries_left < 0
        or missionaries_right < 0
        or cannibals_left < 0
        or cannibals_right < 0
        or (missionaries_left > 0 and cannibals_left > missionaries_left)
        or (missionaries_right > 0 and cannibals_right > missionaries_right)
    ):
        return False
    return True
def is_final_state(state):
    return state == (0, 0, "right")

def generate_next_states(current_state):
    missionaries, cannibals, boat = current_state
    next_states = []
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:  # The boat can only carry 1 or 2 people
                if boat == "left":
                    new_state = (missionaries - m, cannibals - c, "right")
                else:
                    new_state = (missionaries + m, cannibals + c, "left")

                if is_valid_state(new_state):
                    next_states.append(new_state)
    return next_states
def solve_missionaries_and_cannibals():
    initial_state = (3, 3, "left")
    goal_state = (0, 0, "right")
    visited = set()
    queue = [(initial_state, [])]
    while queue:
        current_state, path = queue.pop(0)
        if current_state in visited:
            continue
        visited.add(current_state)
        if is_final_state(current_state):
            return path + [current_state]
        next_states = generate_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None

def main():
    print("Missionaries and Cannibals Problem Solver")
    print("=======================================")
    solution = solve_missionaries_and_cannibals()
    if solution:
        print("Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}: ", end="")
            print_state(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
