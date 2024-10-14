# AMMP Coding Challenge - MQTT Data Pipeline

## Overview
This project is a Python-based data acquisition pipeline designed to handle renewable energy system data from an MQTT broker. 

## Project Structure
```
├── Dockerfile                         # Instructions to build the Docker image for the pipeline
├── ECS-deployment-architecture.png    # ECS Deployment Architecture diagram
├── README.md                          # Project documentation
├── ammp_coding_challenge.md           # Coding challenge prompt and requirements
├── architecture.md                    # Detailed architecture of the solution
├── ca-stage.crt                       # SSL certificate for secure communication
├── cfn.yaml                           # CloudFormation template for infrastructure provisioning
├── main.py                            # Main entry point of the application
├── modules/                           # Modules for specific functionality
│   ├── ca_cert_downloader.py          # Downloads CA certificate for secure MQTT communication
│   ├── mqtt_handler.py                # Handles MQTT subscriptions and data ingestion
│   ├── payload_processor.py           # Processes incoming data payloads
│   └── stub.py                        # Placeholder for future functionalities
├── requirements.txt                   # Python dependencies
├── solution-1(a).md                   # Explanation of solution 1(a)
├── tests/                             # Unit tests for modules
│   ├── conftest.py                    # Test configuration
│   ├── test_ca_cert_downloader.py     # Unit tests for CA certificate downloader
│   ├── test_mqtt_handler.py           # Unit tests for MQTT handler
│   └── test_payload_processor.py      # Unit tests for payload processor
└── venv/                              # Python virtual environment
```

## Requirements
- Python 3.12+
- AWS CLI (configured with appropriate credentials)
- Docker (to build and run the application locally)
- Other dependencies stored in `requirements.txt`

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ogasege/data-acq
   cd https://github.com/ogasege/data-acq
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   Install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the Docker Image:**
   To build the image for ECS deployment:
   ```bash
   docker build -t data-acq .
   ```

5. **Run Tests:**
   The project uses `pytest` and `ruff` for testing and linting, respectively.

   To run the tests:
   ```bash
   pytest
   ```

   To check for linting issues:
   ```bash
   ruff check .
   ```

## Running the Application

### Locally
You can run the application locally by executing:
```bash
python main.py
```
This will connect to the MQTT broker and start processing messages as defined in the `modules/mqtt_handler.py`.

You can run a container from the built docker image locally by executing:
```bash
docker run --env-file .env -it --rm data-acq:latest
```

### On AWS ECS
Deploy the infrastructure using the provided CloudFormation template:

1. **Deploy the CloudFormation stack:**
   ```bash
   aws cloudformation deploy --template-file cfn.yaml --stack-name mqtt-data-acq
   ```

2. **Push the Docker image to Docker Hub** and update the ECS task definition.

## Key Modules

- **ca_cert_downloader.py:** Downloads the required CA certificate for secure communication with the MQTT broker.
- **mqtt_handler.py:** Handles the subscription and ingestion of data from the MQTT broker.
- **payload_processor.py:** Processes the incoming payloads from the MQTT broker.

## Testing
Unit tests are available under the `tests/` directory. To run the tests:
```bash
pytest
```

## Security

- **SSL/TLS:** Secure communication with the MQTT broker using CA certificates.
- **IAM Policies:** Ensure that the IAM roles used by the ECS tasks have the correct permissions for secure communication with AWS resources.


