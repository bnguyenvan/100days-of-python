#!/bin/bash
echo "# 100days-of-python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:bnguyenvan/100days-of-python.git
git push -u origin main
