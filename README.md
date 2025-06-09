# Jupyter on Replit

Jupyter Notebook is a simplified notebook authoring application, and is a part of Project Jupyter, a large umbrella project centered around the goal of providing tools (and standards) for interactive computing with computational notebooks.

## Running Jupyter Notebook

Simply fork this template and click "Run", logging in with the default password `replit`.

## Setting up Virtual Environment with uv

To use a virtual environment created with `uv` in your Jupyter notebooks:

1. Create a virtual environment using uv:
   ```
   uv venv
   ```

2. Activate the virtual environment and install ipykernel:
   ```
   source .venv/bin/activate && pip install ipykernel
   ```

3. Register the virtual environment as a Jupyter kernel:
   ```
   source .venv/bin/activate && python -m ipykernel install --user --name=uv-venv --display-name="Python (uv-venv)"
   ```

4. In your Jupyter notebook, click on the kernel name (usually "Python 3") in the top right corner and select "Python (uv-venv)" to use your virtual environment.

5. Install packages in your virtual environment either via shell:
   ```
   source .venv/bin/activate && pip install package_name
   ```
   
   Or directly in a notebook cell:
   ```
   !source ../.venv/bin/activate && pip install package_name
   ```

## Changing the password

1. In a Shell pane inside your fork, run `jupyter notebook password`.
2. At the `password:` prompt, enter your password, hit enter, then confirm it.
3. Run the following command in the Shell and copy the output:
   ```
   nix-shell -p jq --command 'jq -r .IdentityProvider.hashed_password' < /home/runner/.jupyter/jupyter_server_config.json
   ```
5. Open the Secrets pane in your Repl
6. Set the value of `NOTEBOOK_PASSWORD_HASH` to the output of the previous command
7. The next time you click `Run`, your new password will be used
