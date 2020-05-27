# minimal-webrtc

Try it out at https://apps.aweirdimagination.net/camera/

Create a WebRTC audio/video connection between two devices with minimal
setup: basic usage is to open the page on one device and send the
generated link to (or scan the QR code on) the other device and a
peer-to-peer connection will be established. Communication through the
server is only used for the signalling to set up the connection.

Configuration options on the first device allow selection of what, if
any, video and audio streams should be sent in each direction over the
connection.

Note this intentionally does not use STUN for NAT traversal, as I wrote
it for connections on a local network. If you wish to use this for
connections over the internet, you may need to modify the
`new RTCPeerConnection()` call to include
[`iceServers`](https://developer.mozilla.org/en-US/docs/Web/API/RTCIceServer).
