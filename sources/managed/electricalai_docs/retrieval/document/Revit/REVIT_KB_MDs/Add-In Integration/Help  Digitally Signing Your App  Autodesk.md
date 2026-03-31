---
created: 2026-01-28T20:37:43 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Digitally Signing Your App | Autodesk

> ## Excerpt
> If you are publisher of a Revit add-in, you will have to sign your add-in with your own certificate.

---
If you are publisher of a Revit add-in, you will have to sign your add-in with your own certificate.

To sign your add-in with your own certificate, you first need to purchase a digital signature from a digital certificate vendor. Once you obtain a certificate (cer) or Personal Information Exchange (pfx) file, you can sign your DLL(s) using **signtool**.

Alternatively, you can also use an online Authenticode signing service, such as Symantec's Secure App Service - [https://www.symantec.com/code-signing/secure-app-service/](https://www.symantec.com/CODE-SIGNING/SECURE-APP-SERVICE/).

## Digital Certificate Venders

The following is a non-exhaustive list of vendors that provide digital certificates:

-   Symantec - [www.symantec.com](https://www.symantec.com/)
-   DigiCert - [www.digicert.com](https://www.digicert.com/)
-   VERISIGN - [www.verisign.com](https://www.verisign.com/)
-   Thawte - [www.thawte.com](https://www.thawte.com/)

You can use [signtool.exe](https://msdn.microsoft.com/EN-US/LIBRARY/8S9B9YAZ(V=VS.110).ASPX) tool to sign your .NET dll. The tool is automatically installed with Visual Studio. To run the tool, use the Developer Command Prompt. The following is the format of the command line parameters:

### Command Region: Using signtool

```
signtool.exe sign /fd SHA256 /f <.pfx-file-name> /p  <password> <file-to-sign>.dll
```

Where /fd is a flag for the file digest algorithm to use. Here we use SHA256. (SHA stands for Secure Hash Algorithm. The signtool default is SHA1. We recommend SHA256, which is a newer, more secure version.) <.pfx-file-name> is the name of .pfx (Personal Information Exchange) file you obtain from the vendor. `<password>` is the password that you specify when obtaining the pfx file. `<file-to-sign>.dll` is the name of the DLL that you want to sign.

For example, if you run the command in an arbitrary folder, the above command may look like this:

#### Command Region: signtool example

```
"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\signtool" sign /fd SHA256 /f "C:/Dev/MyCert.pfx" /p "password123" “C:/Dev/HelloRevit.dll”
```

Note: The exact location of signtool may differ in your environment.

Once the DLL is signed with an authorized certification, Revit will no longer pop up a security warning dialog upon loading your add-in.

You can also include the command in the Post-Built Event section of Visual Studio for your application project properties.

#### Command Region: Post-Build Event signing

```
"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\signtool.exe" /fd SHA256 sign /f
"C:\Autodesk\MyCert.pfx" /p MyPassword "$(TargetDir)$(TargetFileName)"
```

It is also worth adding a time stamp while signing (/td and /tr switches in signtool.exe); otherwise the app becomes untrusted when the certificate expires. Adding the time stamp ensures the app is trusted forever as long as it was signed prior to expiration (unless the certificate gets revoked):

#### Command Region: Adding a time stamp

```
signtool.exe timestamp /td sha256 /tr <URL-of-time-stamp-server> <file-to-sign>.dll
```

For example, the following uses the verisign timestamp server:

#### Command Region: Time stamp example

```
signtool.exe timestamp /td sha256 /tr "http://sha256timestamp.ws.symantec.com/sha256/" HelloRevit.dll
```

Note: The /td sha256 and /tr switches used in the example above are used to sign with sha256 timestamp. Beginning January 1, 2017 Microsoft will treat SHA1 timestamps as unsigned. Please refer to [this article](http://support.ksoftware.net/support/solutions/articles/215805-the-truth-about-sha1-sha-256-and-code-signing-certificates-) for more details.
