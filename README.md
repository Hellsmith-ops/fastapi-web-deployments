# fastapi-web-deployments

FastAPI web deployment projects showcasing Python backend APIs, database integration, authentication, and production-ready deployment workflows.

## DEPLOYMENT TUTORIALS

This doc will provide guidance and step-by-step on deploying the cloud library into production.

### CREATE AN .ENV FILE FOR SECRET KEY

- Storing secret keys and API tokens directly in the source code creates a security risk. To prevent exposing sensitive credentials, we should store the secret key in a .env file and make sure that file is not pushed to GitHub.
```bash
#1. generate a strong key with:
openssl rand -hex 32
#2. create the .env file in the repo root:
nano .env
#3. paste the generated key using this format:
SECRET_KEY="replace_this_with_the_secret_key"
```
- For the initial setup, use the commands above to generate a secret key, which will be used for JWT and OAuth2 authentication.
- After generating the secret key, deploy the web server using one of the following methods:

### METHOD 1: DEPLOYMENT USING DOCKER

```bash
docker build --no-cache -t fastapi-web-deployments . #required for first time setup or adjusting the container file 
docker run --rm --env-file .env -p 8000:8000 fastapi-web-deployments #spin up the Docker container and launch FastAPI web server
```

### METHOD 2: DEPLOYMENT USING PYTHON VIRTUAL ENV

```bash
sudo apt install python3.10-venv #install virt env dependency, if not already
cd PATH/TO/FOLDER #navigate to folder
python3 -m venv .venv #create an virtual env named "venv"
source .venv/bin/activate #enable the env
python -m pip install --upgrade pip #refresh dependencies inside virtual env
pip install -r requirements.txt #install required dependencies for this repo
fastapi run main.py --host 0.0.0.0 --port 8000 #launch the FastAPI web server
```





