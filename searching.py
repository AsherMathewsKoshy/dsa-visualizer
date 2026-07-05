from rich.console import Console
import time

console = Console()

def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        console.print(f"\nLow : {low}")
        console.print(f"High: {high}")
        console.print(f"Mid : {mid}")
        console.print(f"Checking {arr[mid]}")

        time.sleep(0.5)

        if arr[mid] == target:
            console.print("[bold green]Target Found![/bold green]")
            return

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    console.print("[bold red]Target Not Found[/bold red]")