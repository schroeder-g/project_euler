import subprocess
import sys
import fire


class run_git_diff(object):

    def __init__(self, repo=None, main=False, latest=False, commits=None, file=None):
        self.repo = repo
        self.main = main
        self.latest = latest
        self.commits = commits
        self.file = file
        self.cmd = ["git", "diff"]
        self.subprocess_args = {
            "text": True,
            "check": True,
        }

        # print(f"cwd: {repo} main: {main} latest: {latest} commits: {commits} file: {file}", file=sys.stderr)

        if not repo:
            print(
                "Error: Please provide a path to the git repository.",
                file=sys.stderr,
            )
            # sys.exit(1)
        else:
            print(f"Repo: {repo}", file=sys.stderr)
            self.subprocess_args["cwd"] = repo

        if self.main:
            self.get_main_diff()
        elif self.latest:
            print("TODO")
        else:
            self.compare_commits(commits)

        self.check_diff()

    def get_main_diff(self):
        current_branch = self._get_current_branch()
        main_diff_cmd = ["--merge-base", "main", current_branch]

        self._print(f"Main CMD: {main_diff_cmd}")

        self.cmd += main_diff_cmd

    def compare_commits(self, commits):
        if not commits or len(commits) != 2:
            self._print("Error: Two commits are required for diff without any flags.")
            sys.exit(1)

        commit_comparison_cmd = ["HEAD", *commits]

        if self.file:
            commit_comparison_cmd += ["--", file]

        self.cmd += commit_comparison_cmd

    def check_diff(self):
        result = self._run(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result, type(result), self.cmd, "\n\n\n", file=sys.stderr)
        print(
            subprocess.run(
                ["echo"],
                input=result.stdout,
                stdout=subprocess.PIPE,
                **self.subprocess_args,
            ).stdout
        )

    ##################
    # H E L P E R S #
    #################

    def _get_current_branch(self):
        return subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            **self.subprocess_args,
        ).stdout.strip()

    def _run(self, cmd, **kwargs):
        result = subprocess.run(cmd, **self.subprocess_args, **kwargs)
        if result.stderr:
            print("Git error:", result.stderr, self._print(result.stdout))
        elif result.stdout is not None:
            return result

    def _print(self, *args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)


if __name__ == "__main__":
    fire.Fire(run_git_diff)
