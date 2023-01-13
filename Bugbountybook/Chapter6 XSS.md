Types of XSS
**Stored XSS**
**Reflected XSS**
**DOM Based XSS**


**XSS polyglot**
https://brutelogic.com.br/blog/building-xss-polyglots/


**Finding Your First XSS!**
Jump right into hunting for your first XSS! Choose a target and follow the
steps we covered in this chapter:
1. Look for user input opportunities on the application. When user input
is stored and used to construct a web page later, test the input field for
stored XSS. If user input in a URL gets reflected back on the resulting
web page, test for reflected and DOM XSS.
2. Insert XSS payloads into the user input fields you’ve found. Insert pay-
loads from lists online, a polyglot payload, or a generic test string.
3. Confirm the impact of the payload by checking whether your browser
runs your JavaScript code. Or in the case of a blind XSS, see if you can
make the victim browser generate a request to your server.
4. If you can’t get any payloads to execute, try bypassing XSS protections.
5. Automate the XSS hunting process with techniques introduced in
Chapter 25.
6. Consider the impact of the XSS you’ve found: who does it target? How
many users can it affect? And what can you achieve with it? Can you
escalate the attack by using what you’ve found?
7. Send your first XSS report to a bug bounty program!