"""
Should be able to integrate with kit-tool
"""
import click
import git
import gitmap
import json
import logging
logging.basicConfig(level=logging.CRITICAL)


@click.command()
def cli():
	click.echo("Running")
	scan_dir()

import os
github_dir="/Users/korsimoro/k/kisia-gitmap/github"

def scan_dir():
	for github_root in os.listdir(github_dir):
		root_path = os.path.join(github_dir,github_root)
		for repo_name in os.listdir(root_path):
			repo_path = os.path.join(root_path,repo_name)
			repo = git.Repo(repo_path)
			print(github_root,repo_name,repo.active_branch)
			gitmap.ModelRepo.encounterGitHubRepo(github_root,repo_name,repo)

		print(json.dumps(gitmap.ModelObject._root_model,indent=4,sort_keys=True,default=lambda x: x.__dict__))
		break
