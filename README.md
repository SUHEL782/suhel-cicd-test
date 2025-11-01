# 🧩 Terraform CI/CD Dynamic Template Generation Test

## 📘 Overview
You are provided with a **JSON structure** that defines **AWS services (nodes)** and their **relationships (edges)**.

- Each **node** represents an AWS service.
- Each **edge** represents an **operation or interaction** between two services.

Your task is to share approach how you can **dynamically generate Terraform templates** (`.tf` files) for each service, including only the **required permissions** based on the defined operations.

---

## 🎯 Objective

Build a solution that can:
- Read a JSON input describing AWS services and their relationships.
- Dynamically generate Terraform configuration files for each service.
- Apply the **least privilege principle** when assigning permissions.

---

## ⚙️ Requirements

### 1. Dynamic Generation
- The solution must handle any number of nodes and edges and extenable.
- Each node (AWS service) must generate a separate Terraform file named: <serviceid>_<id>.tf


**Example:** `86_awss3-0.tf`

### 2. Permissions
- Permissions and IAM roles must be derived dynamically from the **edge operations**.
- Apply the **least privilege** principle — include only what’s needed for the operation.

#### Example Operations
| Operation | Meaning | Required Permission Example |
|------------|----------|-----------------------------|
| `events` | S3 triggers Lambda | S3 → Lambda invoke permissions |
| `read` | EC2 reads from S3 | `s3:GetObject` permissions for EC2 |

### 3. Terraform Templates
- Use only **mandatory or essential fields** for each resource.
- Dummy values are acceptable for resource names (e.g., `"my-bucket"`, `"my-function"`).
- Each generated file should contain:
    - The AWS service resource definition.
    - Required IAM roles and policies.
    - Event or trigger configurations (if applicable).
    - Ensure the generated Terraform code is **syntactically valid**.

---

## 🧾 Input Examples

### Example 1: Single Target Service
```json
{
"nodes": [
  {
    "id": "awss3-0",
    "service": {
      "serviceid": 86,
      "servicename": "Amazon S3",
      "serviceshortname": "awss3",
      "servicecategory": "Storage",
      "genericservicetype": "Storage",
      "serviceproviderid": 1,
      "serviceprovidername": "aws",
      "attachAs": "target"
    },
    "position": { "x": 0, "y": 0 }
  },
  {
    "id": "awslambda-1",
    "service": {
      "serviceid": 48,
      "servicename": "AWS Lambda",
      "serviceshortname": "awslambda",
      "servicecategory": "Compute",
      "genericservicetype": "Compute",
      "serviceproviderid": 1,
      "serviceprovidername": "aws",
      "attachAs": "target"
    },
    "groups": []
  }
],
"edges": [
  {
    "id": "e-qRJT",
    "position": "right",
    "sourceId": "awss3-0",
    "targetId": "awslambda-1",
    "operation": ["events"]
  }
]
}

Example 2: Multiple Target Services

{
  "nodes": [
    {
      "id": "awss3-0",
      "service": {
        "serviceid": 86,
        "servicename": "Amazon S3",
        "serviceshortname": "awss3",
        "servicecategory": "Storage",
        "genericservicetype": "Storage",
        "serviceproviderid": 1,
        "serviceprovidername": "aws",
        "attachAs": "target"
      },
      "position": { "x": 0, "y": 0 }
    },
    {
      "id": "awslambda-1",
      "service": {
        "serviceid": 48,
        "servicename": "AWS Lambda",
        "serviceshortname": "awslambda",
        "servicecategory": "Compute",
        "genericservicetype": "Compute",
        "serviceproviderid": 1,
        "serviceprovidername": "aws"
      },
      "position": { "x": 300, "y": 0 }
    },
    {
      "id": "awsec2-G4s8",
      "service": {
        "serviceid": 36,
        "servicename": "Amazon EC2",
        "serviceshortname": "awsec2",
        "servicecategory": "Compute",
        "genericservicetype": "Compute",
        "serviceproviderid": 1,
        "serviceprovidername": "aws"
      }
    }
  ],
  "edges": [
    {
      "id": "e-qRJT",
      "position": "right",
      "sourceId": "awss3-0",
      "targetId": "awslambda-1",
      "operation": ["events"]
    },
    {
      "id": "e-di0K",
      "position": "right",
      "sourceId": "awss3-0",
      "targetId": "awsec2-G4s8",
      "operation": ["read"]
    }
  ]
}
```

🧠 What We Expect

We want to understand your approach to solving this problem:
How would you interpret the JSON structure?
How will you map operations to Terraform permissions?
How will you dynamically generate .tf files for each service?


🧮 Evaluation Criteria

| Category           | Description                                                         |
|-------------------|---------------------------------------------------------------------|
| Approach & Logic   | Clear explanation of your logic for parsing and generation          |
| Dynamic Design     | Handles multiple nodes, edges, and new operations gracefully       |
| Terraform Accuracy | Generated .tf files are valid and follow best practices             |
| Least Privilege    | Permissions are minimal and specific                                |
| Completeness       | One .tf file per service with proper dependencies                   |



📦 Deliverables

- Detailed steps in `README.md` explaining how you will approach this problem
- sample `.tf` files for each service with essential fields
- Any mapping files you will use to handle this scenario
- Create a public repo in your github account with the name: yourfirstname-cicd-test, upload the files and share the link

Note: Please reply to the mail. If you have any Questions