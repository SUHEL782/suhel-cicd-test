import json
from pathlib import Path

def main():
    # Load mappings....................
    with open("mappings.json") as f:
        mappings = json.load(f)

    # Load input JSON..................
    with open("input.json") as f:
        data = json.load(f)

    nodes = {node["id"]: node for node in data["nodes"]}
    edges = data["edges"]

    # Output directory (.tf folder).................
    out_dir = Path(".tf")
    out_dir.mkdir(exist_ok=True)

    # Process each node.....................
    for node_id, node in nodes.items():
        sid = node["service"]["serviceid"]
        shortname = node["service"]["serviceshortname"]
        tf_filename = out_dir / f"{sid}_{node_id}.tf"

        content = f'# Terraform config for {node["service"]["servicename"]}\n'
        content += f'resource "{shortname}" "{node_id}" {{\n'
        content += f'  name = "Suhel-{node_id}"\n}}\n\n'

        # find edges where this node is involved.............
        for edge in edges:
            if edge["sourceId"] == node_id or edge["targetId"] == node_id:
                ops = edge["operation"]
                for op in ops:
                    if op in mappings:
                        content += f'# Operation: {op} ({mappings[op]["description"]})\n'

        with open(tf_filename, "w") as tf_file:
            tf_file.write(content)
        print(f"Wrote {tf_filename}")

if __name__ == "__main__":
    main()
