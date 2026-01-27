# Neo4j Database Credentials

Local development database credentials for the OSPF Ayurveda Knowledge Graph.

## Connection Details

| Property | Value |
|----------|-------|
| Username | neo4j |
| Password | neo4jneo4j |
| Bolt URI | bolt://localhost:7687 | <<<-- USE THIS ONE
| HTTP URI | http://localhost:7474 |

## Raw Credentials

```
username: neo4j
password: neo4jneo4j
```

## Usage

### Neo4j Browser
1. Open http://localhost:7474
2. Enter username: `neo4j`
3. Enter password: `neo4jneo4j`

### Python (neo4j driver)
```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4jneo4j")
)
```

### Cypher Shell
```bash
cypher-shell -u neo4j -p neo4jneo4j
```
