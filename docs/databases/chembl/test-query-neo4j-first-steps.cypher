// See a drug with all its connections
MATCH (d:Drug {chembl_id: 'CHEMBL2'})
OPTIONAL MATCH (d)-[:HAS_MECHANISM]->(m)-[:ACTS_ON]->(t)
OPTIONAL MATCH (d)-[:INDICATED_FOR]->(ta)
RETURN d.name, m.action_type, t.name AS target, collect(DISTINCT ta.name)[0..5] AS areas

// Visual graph - see 10 drugs and their relationships
MATCH (d:Drug)-[r]->(n)
WHERE d.chembl_id IS NOT NULL
RETURN d, r, n
LIMIT 50
