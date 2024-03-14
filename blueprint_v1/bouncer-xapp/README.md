# Bouncer Python Xapp 

This xApp replicates the Bouncer-RC C++ xApp by using the OSC Python xApp framework.

Installing the xApp (by the dms_cli install command) initiates its startup routine:
- Registrating the xApp on the Application Manager (AppMgr)
- Registering a signal handler for SIGTERM, SIGQUIT, and SIGINT signals, which stop the xApp execution
- Starting a REST server on 8080 port for logging received GET and POST messages
- Consulting the Shared Data Layer (SDL) for which E2 nodes are available
- Sending a subscription request for each E2 node via a REST POST message to the Subscription Manager (SubMgr)

The xApp loop consists of:
- Receiving an INSERT message from the E2 nodes via RIC Message Router (RMR)
- TODO: Decoding the ASN.1 received message
- TODO: Encoding a ASN.1 message with a CONTROL response
- Replying the CONTROL message to the sender

When the xApp is uninstalled (by the dms_cli uninstall command), the xApp receives a SIGTERM signal, which triggers:
- Sending a subscription deletion request to the SubMgr for each active subscription
- Unregistering the xApp from AppMgr
- Shutting down the REST server

## Troubleshoot
Sometimes the E2SIMs may start before the E2 Term is ready, which may cause the E2 nodes to not be registered in the SDL. If the xApp logs `Number of gNBs: 0`, then restart the E2SIMs with this script:
```bash
restart_E2SIMs_script
```