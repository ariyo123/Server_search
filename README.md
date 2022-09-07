# Server_search

The app crawls through n- numbers of server to search for specific information in a log path on the server to help with investigations and troubleshootings and then copy the files to your defined workstation.

A specific use case is when you have serveral servers behind a load Balancer and you need to investigate a transaction but not sure of which server processed the transaction. with this application, it will fetch the log and reduce stress of going through several servers remotely to check.

Requirement:
1. pip install shutil
