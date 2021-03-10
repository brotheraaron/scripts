# Create unique directory :
lbkeysdir="keys123"

mkdir -p $HOME/$lbkeysdir
# cp "$(readlink -f $0)" "$HOME/$lbkeysdir" 2>/dev/null
cd $HOME/$lbkeysdir 2>/dev/null

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

echo '' > $HOME/$lbkeysdir/printKeys.sh

printKeys="ZWNobyAiU1NMIENlcnQ6ICIKY2F0IGxvYWRiYWxhbmNlci5jcnQKcHJpbnRmICJcbiIKZWNobyAi
Q0EgQ2VydGlmaWNhdGU6ICIKY2F0IGNhLmNydApwcmludGYgIlxuIgplY2hvICJQcml2YXRlIEtl
eTogIgpjYXQgbG9hZGJhbGFuY2VyLmtleQoKY2QgJGtleXNEaXI="

echo $printKeys | base64 -di >> $HOME/$lbkeysdir/printKeys.sh
chmod +x $HOME/$lbkeysdir/printKeys.sh

echo '' > $HOME/$lbkeysdir/README

README="WW91IG9ubHkgbmVlZCB0byBydW4gdGhlIHNjcmlwdCB0aGF0IGNyZWF0ZXMgdGhlIGNlcnRzIG9u
ZSB0aW1lLgoKQWZ0ZXIgeW91IHJ1biB0aGUgc2NyaXB0IHRvIGNyZWF0ZSB0aGUgY2VydHMsIHlv
dSBjYW4gcnVuIHRoZSBwcmludCBzY3JpcHQgYXMgbWFueSB0aW1lcyBhcyB5b3UgbmVlZCB0bwpv
ciBqdXN0IGNhdCB0aGUga2V5cyBpbiB0aGUgZGlyZWN0b3J5IHRvIGNvcHkgYW5kIHBhc3RlIHRo
ZSBrZXlzLgoK"

echo $README | base64 -di >> README


printf "\nCopy this script to $HOME/$lbkeysdir, that's where your selfsigned keys are saved.\n"

