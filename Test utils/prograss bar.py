from tqdm import tqdm

# Set the maximum value
max_value = 100

# Set the initial value
value = 0

# Create a progress bar with a range of 0 to 100
with tqdm(total=100, desc="Progress:") as pbar:
    while value < max_value:
        # Do some task here
        # ...

        # Update the value
        value += 1

        # Calculate the progress percentage
        progress = value / max_value * 100

        # Update the progress bar
        pbar.update(progress - pbar.n)