Exact tasks for today

Go to your project:

Bashcd ~/projects/devops
git status
git log --oneline -5

Practice important Git commands:

Bash# Create a new branch
git branch
git checkout -b feature/python-practice

# Make a small change
echo "# Python Practice Branch" >> README.md
git add README.md
git commit -m "Added note in feature branch"

# Switch back to main
git checkout main

# Merge the branch
git merge feature/python-practice

# Delete the branch
git branch -d feature/python-practice

Useful Git commands you must know:

Bashgit status
git log --oneline --graph --all
git diff
git stash
git stash list
git stash pop
git remote -v
git branch -a

Practice stashing:

Bashecho "temporary change" >> README.md
git stash
git status
git stash pop
