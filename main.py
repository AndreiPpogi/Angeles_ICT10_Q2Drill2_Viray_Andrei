import html
from pyscript import document

grade7  = {"Jared Silvestre", "Lucas Gonzales", "Leeroy Torres"}
grade8  = {"David Tecson", "Ryle Benipayo", "Mark Herington"}
grade9  = {"Hans Lee", "Hana Montana", "Ivan Recabar"}
grade10 = {"Carlos Aguas", "Kevin Jo", "Andrei Viray"}

added_members = set()


def render():
    master = grade7 | grade8 | grade9 | grade10 | added_members

    document.getElementById("output").innerHTML = f"""
        <p class="total">Total members: {len(master)}</p>
        <p>All members:</p>
        <ul><li>{"</li><li>".join(sorted(master))}</li></ul>
    """


def add_member(event):
    global added_members

    first = document.getElementById("first-name").value.strip()
    last = document.getElementById("last-name").value.strip()

    full_name = html.escape((first and last) and f"{first} {last}".title())

    new_member = {full_name} - {""}

    added_members |= new_member

    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""
    render()


render()
