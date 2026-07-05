from rich.console import Console

console = Console()

def print_array(arr):
    console.print("\n[bold yellow]Current Array[/bold yellow]")
    console.print(" → ".join(map(str, arr)))