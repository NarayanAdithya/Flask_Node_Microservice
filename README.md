# Flask_Node_Microservice
Simple demonstration of a flask and node API containerized using docker

Docker uses run.sh to start both the servers as CMD can only invoke one server at a time.

### Flask API

Simple API with three endpoints running at 127.0.0.1:5000:

1. / - Returns details of author
2. /brands - Returns list of brands
3. /products/<brand_name> - Returns the list of products for the given complany which is actually internally fetched from the NodeJS API

### NodeJS API

Simple API with two endpoints running at 127.0.0.1:5001:

1. / - Returns details of author
2. /elements - Returns list of all details
3. /products/<element> - Returns the list of products for the given complany 


### Database

Simple JSON file
