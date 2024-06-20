#!/usr/bin/env bash

set -e

echo "📖 This script will help you running the qualification-register-api for the first time. It will try to setup everything"
echo "with default values so you can run it directly."

# Check if we already are configured
if [ -e .autopilot ] ; then
    echo "⚠️ It seems that you already ran this script. If you want to run it again, please remove the .autopilot file."
    exit;
fi

# Generate TLS certificates (they are not used in the default configuration)
echo "➡️ Generating TLS certificates"
if [ -e secrets/ssl/server.key ] && [ -e secrets/ssl/server.cert ]; then
    echo "⚠️ TLS certificates already exist. Skipping."
else
    ./tools/generate_certs.sh
fi

# Create the configuration file
echo "➡️ Creating the configuration file"
if [ -e app.conf ]; then
    echo "⚠️ Configuration file already exists. Skipping."
else
    cp app.conf.autopilot app.conf
fi

# Build the application docker container
echo "➡️ Building the application docker container"
make container-build

# Run the container
echo "➡️ Running the application docker container"
docker compose up app -d

# Create the .autopilot file
touch .autopilot

echo "🏁 Autopilot completed. You should be able to go to your web browser and access the application at http://localhost:8507/docs."
