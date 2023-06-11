GET_NODE_BY_ID = """
                    MATCH (n) 
                    WHERE elementId(n) = $node_id 
                    RETURN {id: elementId(n), labels: labels(n), properties: properties(n)} AS node
                    """
GET_NODES_BY_ID = """
                     MATCH (n)
                     WHERE elementId(n) IN $nodes_id 
                     RETURN {id: elementId(n), labels: labels(n), properties: properties(n)} AS node
                     """

data = [
    {
        "id": "4:8da76954-3af3-4496-98c0-d7fe103e0ce4:0",
        "properties": {
            "namae": "Yoritomo",
            "uji": "Minamoto",
            "force": "Bakufu",
            "class": "Shogun"
        },
        "labels": [
            "Person"
        ]
    },
    {
        "id": "4:8da76954-3af3-4496-98c0-d7fe103e0ce4:2",
        "properties": {
            "namae": "Noriyori",
            "uji": "Minamoto",
            "force": "Bakufu",
            "class": "Mikawa-no-kami"
        },
        "labels": [
            "Person"
        ]
    }
]
