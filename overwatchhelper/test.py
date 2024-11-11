from rich.console import Console
from rich.table import Table
tanks = [
    "T1 = Dva",
    "T2 = Doomfist",
    "T3 = JunkerQueen",
    "T4 = Mauga",
    "T5 = Ramatra",
    "T6 = Reinhardt",
    "T7 = Roadhog",
    "T8 = Sigma",
    "T9 = Winston",
    "T10 = WreckingBall",
    "T11 = Zarya",
    "T12 = Orisa",
    "","","","","","", ""
]
damage = [
    "A1 = Ashe",
    "A2 = Bastion",
    "A3 = Cassidy",
    "A4 = Echo",
    "A5 = Genji",
    "A6 = Hanzo",
    "A7 = Junkrat",
    "A8 = Mei",
    "A9 = Pharah",
    "A10 = Reaper",
    "A11 = Sojourn",
    "A12 = Soldier76",
    "A13 = Sombra",
    "A14 = Symmetra",
    "A15 = Tobjorn",
    "A16 = Tracer",
    "A17 = Venture",
    "A18 = Widowmaker",
]

support = [
    "S1 = Ana",
    "S2 = Baptiste",
    "S3 = Brigitte",
    "S4 = Illari",
    "S5 = Juno",
    "S6 = Kiriko",
    "S7 = Lifeweaver",
    "S8 = Lucio",
    "S9 = Mercy",
    "S10 = Moira",
    "S11 = Zenyatta",
    "","","","","","", " "
]

table = Table(show_header= True)

# table.add_column("Tanks")
# table.add_column("Damage")
# table.add_column("Support")
table.add_column("tanks", justify="left", style="cyan", no_wrap=True)
table.add_column("damage", style="red")
table.add_column("support", justify="right", style="green")

for tank, dam, sup in zip(tanks, damage, support):
    table.add_row(tank, dam[0:12], sup)

console = Console()
console.print(table)