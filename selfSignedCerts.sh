# Create the CA private key :
openssl genrsa -out ca.key 2048 2>/dev/null

# Create the Certificate Signing request:
openssl req -new -key ca.key -out ca.csr -subj "/C=GB/ST=Yorks/L=York/O=MyCompany Ltd./OU=IT/CN=mysubdomain.mydomain.com" 2>/dev/null

# Create the CA SIGN certificate that will be used to sign the new certificates
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt 2>/dev/null

# Create the Private Key for the  LoadBalancer:
openssl genrsa -out loadbalancer.key 2048 2>/dev/null

# Create the Certificate Signing request for the Loadbalancer
openssl req -new -key loadbalancer.key -out loadbalancer.csr -subj "/C=GB/ST=Yorks/L=York/O=MyCompany Ltd./OU=IT/CN=mysubdomain.mydomain.com" 2>/dev/null

# Sign the certificate with our CA certificate :
openssl x509 -req -in loadbalancer.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out loadbalancer.crt -days 50000 2>/dev/null

### Uncomment to see validation steps ###
# Check now the certificate is signed by our CA :
# openssl x509 -in loadbalancer.crt -text
# The certificate that will be need it for the LB are :  ca.crt   loadbalancer.crt  and loadbalancer.key
# cat loadbalancer.crt
# cat ca.crt
# cat loadbalancer.key
### End validation steps ###

echo "SSL Cert: "
cat loadbalancer.crt
printf "\n"
echo "CA Certificate: "
cat ca.crt
printf "\n"
echo "Private Key: "
cat loadbalancer.key
