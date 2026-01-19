import time
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.live import Live

console = Console()

def generate_table():
    """Make a new table."""
    table = Table(title="OPSight: Optimism Node Status (Simulation)")

    table.add_column("Service", style="cyan", no_wrap=True)
    table.add_column("Status", style="green")
    table.add_column("Latency (ms)", justify="right", style="magenta")
    table.add_column("Peers", justify="right", style="yellow")

    # Mock Data - Gerçek veri gelene kadar placeholder
    table.add_row("OP-Geth L2", "✅ SYNCED", "42 ms", "25/50")
    table.add_row("OP-Node", "✅ HEALTHY", "12 ms", "18/30")
    table.add_row("L1 Geth (Eth)", "✅ SYNCED", "85 ms", "N/A")
    table.add_row("Batcher", "⚠️ LAGGING", "1200 ms", "-")

    return table

def main():
    console.print("[bold red]OPSight CLI v0.1.0[/bold red] - Initializing metrics...", style="bold white")
    time.sleep(1)
    
    # Live update simulation
    with Live(generate_table(), refresh_per_second=4) as live:
        for _ in range(10):  # Simulate 10 updates
            time.sleep(0.5)
            live.update(generate_table())
    
    console.print("\n[bold green]System check complete. Waiting for user input...[/bold green]")

if __name__ == "__main__":
    main()
