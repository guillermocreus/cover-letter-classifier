# NLP API

## Instructions

Steps to run the script

### Running the script for the first time
This section shows how to create a virtual environment, which is needed to run the scripts from this project

1. Open the root folder from the terminal
```bash
cd <root_folder_of_project>/
```
2. Create a virtual env
```bash
python3 -m venv venv/
```
3. Open the virtual env created
```bash
source venv/bin/activate
```
4. Install the required dependencies
```bash
pip3 install -r requirements.txt
```
One can check if dependencies were installed by running the following command
```bash
pip3 list
```

If successful, one can close virtual env
```bash
deactivate
```

### Execute scripts

1. Open the virtual env
```bash
source venv/bin/activate
```
2. Running the script
	```bash
	cd src
	```

	2.1. For **Zero shot classifiaction** execute
	```bash
	python3 demo.py input.json
	```

    The file `input.json` will include the input data fed to the model. It will have the following format:

    ```json
        {
            "text": "one day I will see the world.",
            "labels": ["travel", "cooking", "dancing"]
        }
    ```

3. Close the virtual env
```bash
deactivate
```