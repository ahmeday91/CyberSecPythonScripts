software_versions = ["Python 2.7",
                     "Python 3.8",
                     "OpenSSL 1.0.1",
                     "OpenSSL 1.1.1"]
vulnerable_versions = ["Python 2.7",
                       "OpenSSL 1.0.1"]

#Your code goes here

for version in software_versions:
    if version in vulnerable_versions:
            print("Warning - ", version, "is there in our software version")
        