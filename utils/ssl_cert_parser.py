import ssl
import socket
from datetime import datetime

ocsp = ''
serial = ''

def get_ssl_certificate_info(hostname):
    # Define the port for SSL/TLS connection
    port = 443
    
    # Create a socket connection
    with socket.create_connection((hostname, port)) as sock:
        # Wrap the socket with SSL
        with ssl.create_default_context().wrap_socket(sock, server_hostname=hostname) as ssock:
            # Get the certificate in PEM format
            cert = ssock.getpeercert()
            
            # Extract certificate information
            cert_info = {
                "subject": dict(x[0] for x in cert["subject"]),
                "issuer": dict(x[0] for x in cert["issuer"]),
                "serialNumber": cert["serialNumber"],
                "cert valid until": datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z"),
                "OCSP_URL": cert["OCSP"]
            }
            global ocsp, serial 
            ocsp = cert["OCSP"]
            serial=cert["serialNumber"]
            
            return cert_info


def main():
    # Get SSL certificate information
    hostname = "google.com"
    cert_info = get_ssl_certificate_info(hostname)

    # Print certificate information
    for key, value in cert_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()