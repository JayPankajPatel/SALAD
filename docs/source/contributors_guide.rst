==================
Contributers Guide
==================

Pyenv Installation
------------------
.. note:: All of the following information comes from here_

.. _here: https://github.com/pyenv/pyenv#installation

``pyenv`` is for python version management as ``poetry`` does not have any way of doing so. Open a terminal and paste the following

For ``Linux`` and ``WSL``::

  curl https://pyenv.run | bash

For ``macOS`` install with ``homebrew``

.. code-block:: console

   brew update
   brew install pyenv

Shell Environment for Pyenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bash
~~~~

For ``bash`` open a terminal and paste the following:

.. code-block:: console

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc

Then add the following to your ``~/.profile`` and ``~/.bash_profile``

.. note::

  If ``~./bash_profile`` does not exist, just put the following in ``~/.profile``

.. code-block:: console

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
  echo 'eval "$(pyenv init -)"' >> ~/.profile

Finally, add the following to your ``~/.bash_profile``

.. code-block:: console

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

Zsh
~~~

For ``Zsh`` paste the following in a terminal.

.. code-block:: console

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init -)"' >> ~/.zshrc

Fish
~~~~~

If you have Fish 3.2.0 or newer, execute this interactively:

.. code-block:: console

  set -Ux PYENV_ROOT $HOME/.pyenv
  fish_add_path $PYENV_ROOT/bin

Otherwise, execute the snippet below:

.. code-block:: console

  set -Ux PYENV_ROOT $HOME/.pyenv
  set -U fish_user_paths $PYENV_ROOT/bin $fish_user_paths

Now, add this to ~/.config/fish/config.fish::

  pyenv init - | source

Restart your shell
~~~~~~~~~~~~~~~~~~

For the environment variables changes to take effect, restart your shell with the following::

  exec "$SHELL"

For convenience here are the commands together so you can just copy and paste them.

Bash::

  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
  echo 'eval "$(pyenv init -)"' >> ~/.profile
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
  exec "$SHELL"

Zsh::

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init -)"' >> ~/.zshrc
  exec "$SHELL"

Fish::

  set -Ux PYENV_ROOT $HOME/.pyenv
  fish_add_path $PYENV_ROOT/bin
  pyenv init - | source
  exec "$SHELL"

Usage
~~~~~
Install ``python3.10.10`` with pyenv as this is the version we are using::

  pyenv install 3.10.10

In SALAD repository, there is a .python-version file that will automatically set your python version
if you navigate to the repository::

  cd </path/to/SALAD>

And then type::

  #pyenv local .python-version, however in this version of the software it is 3.10.10 but it could change
  pyenv local 3.10.10

When python is used in this directory, it will be whatever the ``.python-version`` is set to.

Poetry Installation
-------------------
SALAD uses a tool called Poetry for its packaging and dependency managament.

To install ``poetry``, on ``Linux``, ``macOS``, and ``WSL``

on the user level run the following:

.. code-block:: console

  curl -sSL https://install.python-poetry.org | python3 -

.. note:: For more information on usage visit their website_

.. _website: https://python-poetry.org/docs/basic-usage/

Cloning the Repo
----------------
With SSH::

  git@github.com:JayPankajPatel/SALAD.git

With HTTPS::

  https://github.com/JayPankajPatel/SALAD.git

Install The Project
-------------------
Navigate to SALAD::

  cd <path/to/SALAD>

Activate the poetry env::

  poetry shell

.. note::

   Be sure to have the virtual env always activate when contributing to this project.

Download the dependencies, including the development dependencies with::

  poetry install --dev

Poetry Usage
------------
After ``poetry shell`` has been called and your virtual env is activated.

Run scripts with poetry by using the following::

  poetry run python <your_script>.py

To add dependencies use the following::

  poetry add <your-package-name>

Example::

  poetry add requests

.. tip::

  To add a specific version do the following::

    poetry add <your-package-name>==<version number>

To remove a dependency use the following::

  poetry remove <your-package-name>

Pre-commit hooks
----------------
This project has pre-commit hooks for formatting, style, import order, and linting.
This is to ensure that the code base looks the same even if 100s of people contribute.
Make sure to go over PEP8 style guides and use opinionated static analysis tools.

New Feature Guide
-----------------
Make branches from the issues page on github to ensure consistent naming of feature branches.
Fill out the pull request template (when I make it).
Finally, make a pull request for code review.

Bug, Issues, Ideas
------------------
If there are any thoughts, concerns or ideas with this project leave them on the issues_ tab on github and discussions on the discussions_ tab on github.

.. _issues: https://github.com/JayPankajPatel/SALAD/issues

.. _discussions: https://github.com/JayPankajPatel/SALAD/discussions
