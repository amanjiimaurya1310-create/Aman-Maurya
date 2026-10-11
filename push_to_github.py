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
        print("=" * 65)
        print(" GitHub Authentication")
        print("=" * 65)
        print("Aapke browser me Token page open ho chuka hai.")
        print("Page ke neeche 'Generate token' click karke token copy karein.")
        print("=" * 65)
        try:
            token = input("Yahan apna GitHub Token paste karein (ghp_...): ").strip()
        except EOFError:
            token = ""
        
    if not token:
        print("\n[ERROR] Koi token provide nahi kiya gaya. Push cancel ho gaya.")
        sys.exit(1)
        
    remote_url = f"https://x-access-token:{token}@github.com/amanjiimaurya1310-create/Aman-Maurya.git"
    print("\nPushing changes to GitHub repository (branch: main)...")
    try:
        dp.push(repo_dir, remote_url, refspecs=b"refs/heads/main:refs/heads/main")
        print("\n" + "=" * 65)
        print("[SUCCESS] Badhai ho! Code successfully GitHub par push ho chuka hai!")
        print("Repository Link: https://github.com/amanjiimaurya1310-create/Aman-Maurya")
        print("=" * 65)
        
        # Save credentials for future use
        cred_file = os.path.expanduser("~/.git-credentials")
        with open(cred_file, "a", encoding="utf-8") as f:
            f.write(f"https://amanjiimaurya1310-create:{token}@github.com\n")
            
    except Exception as e:
        print(f"\n[ERROR] Failed to push: {e}")
        print("\nTips:")
        print("1. Check karein ki token me 'repo' permission select ki gayi thi.")
        print("2. Token sahi se copy hua ho.")
        sys.exit(1)

if __name__ == "__main__":
    main()
