import os

import pytest

from github_utils.github import GitHubAPI


@pytest.fixture
def github_api():
     # Get access token from environment variable
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    if not access_token:
        print("Error: GITHUB_ACCESS_TOKEN environment variable not set.")
        exit(1)
    return GitHubAPI(access_token)

def test_get_user(github_api):
    user_data = github_api.get_user("shivampatil5606")
    assert user_data['login'] == "shivampatil5606"

def test_create_issue(github_api):
    # This test assumes you have a repository you can use for testing
    issue_data = github_api.create_issue("shivampatil5606", "dockerfiles", "Test Issue", "This is a test issue.")
    assert "title" in issue_data
    assert "body" in issue_data
