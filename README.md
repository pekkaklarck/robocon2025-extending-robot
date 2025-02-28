# Extending Robot Framework workshop

This repository contains training material related to the Extending Robot Framework
workshop organized as part of [RoboCon](https://robocon.io/) on February 12, 2025.

The repository initially contained materials needed to get started, but the current
state represents what was done during the workshop.

## Installations

- Python 3.10 or newer. Python 3.8 or 3.9 will work if you cannot upgrade.
- Robot Framework 7.2. Robot Framework 7.0 or 7.1 will work, but you cannot
  run all examples.
- Editor or IDE that supports Python and Robot Framework. VSCode or PyCharm with
  the [RobotCode plugin](https://github.com/robotcodedev/robotcode) is recommended.
- Suitable admin rights to install additional Python modules if needed.

## Materials

The first step is getting the initial material from this repository. The
recommended approach is cloning the repository using `git`, but you can
also [download the content as a zip file](
https://github.com/pekkaklarck/robocon2025-extending-robot/archive/refs/heads/main.zip).

During the day I'll push my changes to the `main` branch. If you cloned the
repository, you can then easily pull the changes to your local repository
if needed.  If you want to work in the same local repository, it is a good idea
to  create a branch for your work by running `git checkout -b <branchname>`.
If you also want to push your changes to GitHub, you need to first fork this
repository and clone that.

## Topics

Covered topics are listed below. Each topic has a dedicated directory with
a README file containing more information.

- [Libraries](Libraries)
- [Listeners](Listeners)
- [Data and result modifiers](Modifiers)
- [Parsing API](Parsing)
