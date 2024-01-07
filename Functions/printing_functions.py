def print_models(unprinted_models, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_models:
        current_model = unprinted_models.pop()
        # Simulate creating a 3D print from the design.
        print(f"Printing model: {current_model}")
        completed_models.append(current_model)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nCompleted models:")
    for completed_model in completed_models:
        print(completed_model)
