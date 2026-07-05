from utils import print_array
from rich.console import Console
import time
console = Console()

def bubble_sort(arr):
    n = len(arr)

    comparisons = 0
    swaps = 0

    for i in range(n):

        console.print(f"\n[bold cyan]Pass {i+1}[/bold cyan]")

        for j in range(n-i-1):

            comparisons += 1

            console.print(f"\n🟡 Comparing {arr[j]} and {arr[j+1]}")

            time.sleep(1)

            if arr[j] > arr[j+1]:

                console.print("[bold red]🔄 Swapping[/bold red]")

                arr[j], arr[j+1] = arr[j+1], arr[j]

                swaps += 1

                print_array(arr)

            else:

                console.print("[green]✅ No Swap[/green]")

    console.print("\n[bold green]Finished![/bold green]")
    print_array(arr)

    console.print(f"\nComparisons : {comparisons}")
    console.print(f"Swaps       : {swaps}")
    console.print("Time Complexity : O(n²)")
    console.print("Space Complexity: O(1)")