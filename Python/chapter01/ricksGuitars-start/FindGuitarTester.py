from Guitar import Guitar
from Inventory import Inventory


def main():
    # Set up Rick's guitar inventory
    inventory = Inventory()
    initialize_inventory(inventory)

    what_erin_likes = Guitar("", 0, "fender", "Stratocastor", "electric", "Alder", "Alder")

    guitar = inventory.search(what_erin_likes)
    if guitar != None:
        print("Erin you might like this",
                guitar.builder, guitar.model,
                guitar.type, "guitar:\n",
                guitar.back_wood, "back and sides,\n",
                guitar.top_wood, "top.\n You can have it for only $",
                guitar.price, "!")
    else:
        print("Sorry, Erin, we have nothing for you.")


def initialize_inventory(inventory):
    inventory.add_guitar("11277", 3999.95, "Collings", "CJ", "acoustic",
            "Indian Rosewood", "Sitka")
    inventory.add_guitar("V95693", 1499.95, "Fender", "Stratocastor", "electric",
            "Alder", "Alder")
    inventory.add_guitar("V9512", 1549.95, "Fender", "Stratocastor", "electric",
            "Alder", "Alder")
    inventory.add_guitar("122784", 5495.95, "Martin", "D-18", "acoustic",
            "Mahogany", "Adirondack")
    inventory.add_guitar("76531", 6295.95, "Mredartin", "OM-28", "acoustic",
            "Brazilian Rosewood", "Adriondack")
    inventory.add_guitar("70108276", 2295.95, "Gibson", "Les Paul", "electric",
            "Mahogany", "Maple")
    inventory.add_guitar("82765501", 1890.95, "Gibson", "SG '61 Reissue",
            "electric", "Mahogany", "Mahogany")
    inventory.add_guitar("77023", 6275.95, "Martin", "D-28", "acoustic",
            "Brazilian Rosewood", "Adirondack")
    inventory.add_guitar("1092", 12995.95, "Olson", "SJ", "acoustic",
            "Indian Rosewood", "Cedar")
    inventory.add_guitar("566-62", 8999.95, "Ryan", "Cathedral", "acoustic",
            "Cocobolo", "Cedar")
    inventory.add_guitar("6 29584", 2100.95, "PRS", "Dave Navarro Signature",
            "electric", "Mahogany", "Maple")


if __name__ == "__main__":
    main()
