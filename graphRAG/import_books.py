import pandas as pd
from tigergraph_connection import conn

df = pd.read_csv("books.csv")

print("TigerGraph Connected!")

for _, row in df.iterrows():

    title = str(row["title"]).strip()
    author = str(row["author"]).strip()
    genre = str(row["genre"]).strip()
    context = str(row["context"]).strip()
    summary = str(row["summary"]).strip()

    # -------------------------
    # BOOK VERTEX
    # -------------------------

    conn.upsertVertex(
        "Book",
        title,
        {
            "summary": summary
        }
    )

    # -------------------------
    # AUTHOR VERTEX
    # -------------------------

    conn.upsertVertex(
        "Author",
        author,
        {}
    )

    conn.upsertEdge(
        "Book",
        title,
        "WRITTEN_BY",
        "Author",
        author,
        {}
    )

    # -------------------------
    # GENRES
    # -------------------------

    genres = genre.split(",")

    for g in genres:

        g = g.strip()

        conn.upsertVertex(
            "Genre",
            g,
            {}
        )

        conn.upsertEdge(
            "Book",
            title,
            "HAS_GENRE",
            "Genre",
            g,
            {}
        )

    # -------------------------
    # CONTEXTS
    # -------------------------

    contexts = context.split(",")

    for c in contexts:

        c = c.strip()

        conn.upsertVertex(
            "Context",
            c,
            {}
        )

        conn.upsertEdge(
            "Book",
            title,
            "HAS_CONTEXT",
            "Context",
            c,
            {}
        )

    print(f"Imported: {title}")
        # -------------------------
    # CHARACTERS
    # -------------------------

    if pd.notna(row["character arcs"]):

        character_data = str(row["character arcs"])

        character_entries = character_data.split("\n")

        for entry in character_entries:

            if "-" in entry:

                parts = entry.split("-", 1)

                character_name = parts[0].strip()

                character_arc = parts[1].strip()

                if character_name:

                    # Create Character Vertex
                    conn.upsertVertex(
                        "Characters",
                        character_name,
                        {
                            "arc": character_arc
                        }
                    )

                    # Create Edge
                    conn.upsertEdge(
                        "Book",
                        title,
                        "HAS_CHARACTERS",
                        "Characters",
                        character_name,
                        {}
                    )

print("\nBooks Imported Successfully!")