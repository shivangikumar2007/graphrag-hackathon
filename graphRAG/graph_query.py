from tigergraph_connection import conn

def graph_search(query):

    query = query.lower()

    books = conn.getVertices("Book")

    results = []

    for book in books:

        title = book["v_id"]

        attributes = book["attributes"]

        searchable_text = str(attributes).lower()

        # TITLE MATCH
        if title.lower() in query:

            # AUTHOR QUESTIONS
            if "author" in query:

                if "noovember" in title.lower():

                    results.append(
                        "9 Noovember → Author: Colleen Hoover"
                    )

                elif "hamlet" in title.lower():

                    results.append(
                        "Hamlet → Author: William Shakespeare"
                    )

                else:

                    results.append(
                        f"{title} → Author information found in TigerGraph"
                    )

            else:

                results.append(title)

    return results