from searching import binary_search
from sorting import bubble_sort
from rich.console import Console

console = Console()

while True:
    console.print("\n[bold cyan]========= DSA Visualizer =========[/bold cyan]")
    console.print("1. Bubble Sort")
    console.print("2. Binary Search")
    console.print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
        bubble_sort(numbers)

    elif choice == "2":
        numbers = list(map(int, input("Enter sorted numbers: ").split()))
        target = int(input("Target: "))
        binary_search(numbers, target)

    elif choice == "3":
        console.print("[green]Goodbye![/green]")
        break

    else:
        console.print("[red]Invalid Choice[/red]")