import sys
import chilkat
import string
# This example requires the Chilkat API to have been previously unlocked.
# See Global Unlock Sample for sample code.

# The mailman object is used for sending and receiving email.
mailman = chilkat.CkMailMan()

# To use a SOCKS4 or SOCKS5 proxy, simply set the following
# properties prior to making any calls that communicate with
# an SMTP server:
# The SOCKS hostname may be a domain name or
# IP address:
# mailman.put_HttpProxyAuthMethod('LOGIN')
mailman.put_HttpProxyHostname("proxy.packetstream.io")
mailman.put_HttpProxyPort(31112)
mailman.put_HttpProxyUsername("kuchbhientertainment")
mailman.put_HttpProxyPassword("bhkXQOTQgJmyygXW")
# # # Set the SOCKS version to 4 or 5 based on the version
# # # of the SOCKS proxy server:
# mailman.put_SocksVersion(5)
# Note: SOCKS4 servers only support usernames without passwords.
# SOCKS5 servers support full login/password authentication.

# Set the SMTP server.
mailman.put_SmtpHost("smtp.gmail.com")
# mailman.get_StartTLS()
# Set the SMTP login/password (if required)
mailman.put_SmtpUsername("souravberaofficial@gmail.com")
mailman.put_SmtpPassword("htcljornffzfdabd")
# mailman.put_SmtpSsl(True)
mailman.put_SmtpPort(465)
# Create a new email object
email = chilkat.CkEmail()
# email.put_FromAddress("test@gmail.com")
# email.put_From("Me <SoundControlsEverything@outlook.com>")

email.put_Subject("This is a test")
email.SetHtmlBody("<html><h1>This is a test</h1></html>")
# email.put_Body("<h1>This is a test</h1>")
# email.put_FromName("Shikha")
email.put_From(
    f"test <souravberaofficial@gmail.com>")
success = email.AddTo("Admin", "souravberaofficial@gmail.com")

# contentType = email.addFileAttachment("qa_data/jpg/starfish.jpg")
# if (email.get_LastMethodSuccess() != True):
#     print(email.lastErrorText())
#     sys.exit()


# Call SendEmail to connect to the SMTP server and send.
# The connection (i.e. session) to the SMTP server remains
# open so that subsequent SendEmail calls may use the
# same connection.

success = mailman.SendEmail(email)
if (success != True):
    print(mailman.lastErrorText())
    sys.exit()

# Some SMTP servers do not actually send the email until
# the connection is closed.  In these cases, it is necessary to
# call CloseSmtpConnection for the mail to be  sent.
# Most SMTP servers send the email immediately, and it is
# not required to close the connection.  We'll close it here
# for the example:
success = mailman.CloseSmtpConnection()
if (success != True):
    print("Connection to SMTP server not closed cleanly.")

print("Mail Sent!")
