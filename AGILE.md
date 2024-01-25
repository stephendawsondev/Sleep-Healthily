# Agile Methodology

[Click here to go back to the README.md file](README.md)

## Overview

For my project, I am using a Github Project board. I'm utilising Github's milestones to track my progress, as well as their `.yml` issue templates for creating templates for Bugs, User stories and Epics. I have also set up simple workflows that will automatically move issues to the appropriate columns as they are created and closed.

## Agile Tools

### Project Board

The project board is split into 4 columns:

- Backlog
- To Do
- In Progress
- Done

The backlog column is where I store all of my issues that I have created. I then move them into the To Do column when I am ready to start working on them. Once I have started working on them, I will move them into the In Progress column. Once I have completed the issue, I will move it into the Done column.

### Milestones

I decided to break down the project into milestones. I have created 5 milestones, which are:

- Sprint 1 (One week)
- Sprint 2 (One week)
- Sprint 3 (One week)
- Sprint 4 (5 days)
- Testing and Development Phase (5 days)

### Issues

I created three issue templates, which are:

- Bug
- User Story
- Epic

I created the templates as `.yml` files so that it takes advantage of Github's [issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) feature. One great advantage of `.yml` templates is that you can automatically add the issue to a project board, which isn't possible with `.md` templates.

###  Labels

I utilised some existing labels and created a few labels to help me organise my issues. The labels I used are:

- `bug` (existing) - Used to identify bugs
- `duplicate` (existing) - Used to identify duplicate issues
- `enhancement` (existing) - Used to identify enhancements
- `user story` (custom) - Used to identify user stories
- `epic` (custom) - Used to identify epics
- `must have` (custom) - Used to identify must have issues
- `should have` (custom) - Used to identify should have issues
- `could have` (custom) - Used to identify could have issues
- `won't have` (custom) - Used to identify won't have issues
- `pull request` (custom) - Used to more easily identify pull requests on the project board

### Workflows

I enabled three of the set workflows on the project (two were already enabled):

- [Automatically add project cards to the backlog column](./documentation/workflows/workflow1.png)

- [Automatically move project cards to the done column when issues are closed](./documentation/workflows/workflow2.png)

- [Automatically add any reopened issues to the Todo column](./documentation/workflows/workflow3.png)

## Sprints - Notes and learnings

### Sprint 1 notes

> "Sprint 1 will be where the first must haves are tackled. It will involve tackling the most important tasks, which are marked as must have and potentially should have."

<!-- Screenshot of sprint 1 here -->

### Sprint 2 notes

> "This task also focuses on doing the must have tasks, as well as also taking on some should have tasks if possible."

<!-- Screenshot of sprint 2 here -->

### Sprint 3 notes

> "Sprint 3 will focus on coding, but it will be used to finishing up and must haves or should haves from previous sprints, while also tackling could haves if time allows."

<!-- Screenshot of sprint 3 here -->

### Sprint 4 notes

> Sprint 4 focuses on ensuring any final must have and should have issues are completed, or marked as won't have. If they are completed, this will also be used as the opportunity to work on a could have issue.

<!-- Screenshot of sprint 4 here -->

### Testing and Documentation phase notes

> While testing and documenting should be done throughout the project, this phase focuses on carrying out final manual tests and fixing up the documentation.

<!-- Screenshot of testing and dev phase here -->
