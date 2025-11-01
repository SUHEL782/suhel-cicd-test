## 🧠 Approach & How to Run

### 1. Problem Understanding
The goal was to dynamically generate Terraform configuration files based on a JSON structure describing AWS services (nodes) and their relationships (edges).  
Each node represents a service (e.g., S3, Lambda, EC2), and each edge defines how those services interact (e.g., “events” or “read”).

The generator implements **least privilege principle** — permissions are added only for operations that exist in the edges.

---

### 2. Approach
- **Input Parsing:**  
  The script (`generator.py`) reads `input.json` which contains nodes and edges.
- **Operation Mapping:**  
  Each operation type (like `events`, `read`, etc.) is defined in `mappings.json` — this file maps an operation to required permissions and descriptions.
- **Dynamic File Generation:**  
  For each node, a Terraform file is generated in the `.tf/` folder using the naming pattern `<serviceid>_<id>.tf`.  
  Each `.tf` file includes:
  - A resource block for the AWS service.
  - Comments describing which operations affect it.
  - The IAM permissions or relationships derived from `mappings.json`.

---

### 3. How to Run
```bash
# Run the generator with input.json
python generator.py input.json
