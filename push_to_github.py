"""
Push Employee Attrition Prediction System to GitHub
Remote: https://github.com/amanjiimaurya1310-create/Aman-Maurya.git
"""
import os
import sys
import dulwich.porcelain as dp

def main():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    token = os.environ.get("GITHUB_TOKEN")
    if not token and len(sys.argv) > 1:
        token = sys.argv[1].strip()
    
    if not token:
        print("=" * 60)
        print("GitHub Authentication Required")
        print("To push to GitHub, a Personal Access Token (PAT) is required.")
        print("Create one at: https://github.com/settings/tokens (Scope: repo)")
        print("=" * 60)
        token = input("Enter your GitHub Token (PAT): ").strip()
        
    if not token:
        print("Error: No token provided. Push aborted.")
        sys.exit(1)
        
    remote_url = f"https://x-access-token:{token}@github.com/amanjiimaurya1310-create/Aman-Maurya.git"
    print("\nPushing changes to GitHub repository (branch: main)...")
    try:
        dp.push(repo_dir, remote_url, refspecs=b"refs/heads/main:refs/heads/main")
        print("\n[SUCCESS] Code successfully pushed to:")
        print("https://github.com/amanjiimaurya1310-create/Aman-Maurya")
    except Exception as e:
        print(f"\n[ERROR] Failed to push: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
