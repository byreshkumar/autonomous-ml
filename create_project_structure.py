import os

# Define the project structure
structure = {
    "ml-autonomous-car": [
        "MODULE.bazel",
        "BUILD.bazel",
        "requirements.txt",
        "README.md",
        ".bazelrc",
        ".devcontainer/devcontainer.json",
        ".devcontainer/Dockerfile",
        "src/data.py",
        "src/model.py",
        "src/train.py",
        "src/infer.py",
        "docker/Dockerfile.app",
        "docker/Dockerfile.train",
        "charts/steering-service/Chart.yaml",
        "charts/steering-service/values.yaml",
        "charts/steering-service/templates/deployment.yaml",
        "charts/steering-service/templates/service.yaml",
        "k8s/argo/rbac.yaml",
        "k8s/argo/workflow.yaml",
        "argocd/application.yaml",
        "tests/test_data.py",
        "notebooks/exploration.ipynb",
    ]
}

def create_structure(base_path="."):
    for root, files in structure.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(root_path, file)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # create empty file
                print(f"Created: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\n✅ Project structure generated. Now run:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Initial ML autonomous car project structure'")
    print("   git branch -M main")
    print("   git remote add origin <your-github-repo-url>")
    print("   git push -u origin main")