# Makefile

# Variables (adjust these as needed)
OPENAPI_YAML      = ari-openapi.yaml
GENERATOR_CLI     = openapi-generator-cli.jar
GENERATOR_CLI_URL = https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.11.0/openapi-generator-cli-7.11.0.jar

# Names for the generated packages
ASYNC_PACKAGE = ari_async_sdk
SYNC_PACKAGE  = ari_sync_sdk

# Output directories
ASYNC_OUTPUT = ./output/ari-async
SYNC_OUTPUT  = ./output/ari-sync

.PHONY: all async sync clean

# Rule to download the generator CLI jar only if it is not present
$(GENERATOR_CLI):
	wget $(GENERATOR_CLI_URL) -O $(GENERATOR_CLI)

all: async sync

async: $(GENERATOR_CLI)
	@echo "Generating asynchronous Python SDK with type hints (client only)..."
	java -jar $(GENERATOR_CLI) generate \
	    -i $(OPENAPI_YAML) \
	    -g python-aiohttp \
	    --package-name $(ASYNC_PACKAGE) \
	    --additional-properties=\
projectName=$(ASYNC_PACKAGE),\
packageName=$(ASYNC_PACKAGE),\
async=true,\
withTypeHints=true,\
server=false \
	    -o $(ASYNC_OUTPUT)
	@echo "Async SDK generated in $(ASYNC_OUTPUT)"

sync: $(GENERATOR_CLI)
	@echo "Generating synchronous Python SDK with type hints (client only)..."
	java -jar $(GENERATOR_CLI) generate \
	    -i $(OPENAPI_YAML) \
	    -g python \
	    --package-name $(SYNC_PACKAGE) \
	    --additional-properties=\
projectName=$(SYNC_PACKAGE),\
packageName=$(SYNC_PACKAGE),\
async=false,\
withTypeHints=true,\
server=false \
	    -o $(SYNC_OUTPUT)
	@echo "Sync SDK generated in $(SYNC_OUTPUT)"

clean:
	@echo "Cleaning generated SDKs and generator jar..."
	rm -rf $(ASYNC_OUTPUT) $(SYNC_OUTPUT) $(GENERATOR_CLI)
