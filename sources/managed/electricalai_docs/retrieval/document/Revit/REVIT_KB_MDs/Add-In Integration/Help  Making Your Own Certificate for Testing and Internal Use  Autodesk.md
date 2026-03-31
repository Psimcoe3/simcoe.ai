---
created: 2026-01-28T20:37:52 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Making Your Own Certificate for Testing and Internal Use | Autodesk

> ## Excerpt
> You can make your own digital certificate for testing or using within your company.

---
You can make your own digital certificate for testing or using within your company.

To create your own digital certificate

1.  Create a digital certificate using the [MakeCert.exe](https://msdn.microsoft.com/EN-US/LIBRARY/WINDOWS/DESKTOP/AA386968(V=VS.85).ASPX) tool.
2.  Create a Personal Information Exchange (pfx) file using the Pvk2Pfx.exe tool.
3.  [Digitally Signing Your App](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Digitally_Signing_Your_Revit_Add_in_Digitally_Signing_Your_App_html).
4.  Import a Digital Certificate to Windows Certificate Store. ([CertMgr.msc or CertUtil.exe](https://msdn.microsoft.com/en-us/library/E78BYTA0(V=VS.110).aspx))

## Create a Digital Certificate

You can use [MakeCert.exe](https://msdn.microsoft.com/EN-US/LIBRARY/WINDOWS/DESKTOP/AA386968(V=VS.85).ASPX) tool to make your own digital certificate for testing and internal use. The following is the command format:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_CB2735141C884AA185BF09B93CDCA5F4"><tbody><tr><td>Command Region: Make a certificate command format</td></tr><tr><td><pre><code><span>MakeCert</span><span>.</span><span>exe </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>&lt;</span><span>name</span><span>-</span><span>of</span><span>-</span><span>private</span><span>-</span><span>key</span><span>-</span><span>file</span><span>&gt;.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=&lt;developer-name&gt;"</span><span> </span><span>&lt;</span><span>name</span><span>-</span><span>of</span><span>-</span><span>certificate</span><span>-</span><span>file</span><span>&gt;.</span><span>cer </span><span>-</span><span>b </span><span>&lt;</span><span>start</span><span>-</span><span>data</span><span>&gt;</span><span> </span><span>-</span><span>e </span><span>&lt;</span><span>end</span><span>-</span><span>date</span><span>&gt;</span></code></pre></td></tr></tbody></table>

Where `<name-of-private-key-file>` is the name of the file where the private key is stored, `<developer- name>` is the name of the developer, `<name-of-certificate-file>` is the name of the certificate file, `<start-date>` is the date when the certificate became valid (format is mm/dd/yyyy), and `<end-date>` is the date when the validity of the certificate ends.

For example:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_5282B69274E4442A800F24DECE780E25"><tbody><tr><td>Command Region: MakeCert.exe example</td></tr><tr><td><pre><code><span>"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\MakeCert.exe"</span><span> </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=DevABC"</span><span> </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>b </span><span>01</span><span>/</span><span>01</span><span>/</span><span>2016</span><span> </span><span>-</span><span>e </span><span>12</span><span>/</span><span>31</span><span>/</span><span>2016</span></code></pre></td></tr></tbody></table>

Or:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_B60C5B26166F4ED39ABE4C01B9DBEA6C"><tbody><tr><td>Command Region: MakeCert.exe example</td></tr><tr><td><pre><code><span>"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\makecert.exe"</span><span> </span><span>-</span><span>r </span><span>-</span><span>sv </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>n </span><span>"CN=DevABC"</span><span> </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>b </span><span>01</span><span>/</span><span>01</span><span>/</span><span>2016</span><span> </span><span>-</span><span>e </span><span>12</span><span>/</span><span>31</span><span>/</span><span>2016</span></code></pre></td></tr></tbody></table>

This command will bring up "Create Private Key Password" dialog. Enter the private key password in the dialog. If it asks for password, enter again. When everything is done, you will see a message "Succeeded" in the command window and .cer and .pvk files are created.

## Convert to PFX

The next step is to convert a digital certificate to a Personal Information Exchange (pfx) file using the pvk2pfx.exe tool. In this step, you need the .pvk file, .cer file, and password you created in the above step. The command format looks like this:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_D142C4EBFF7C4DB280ABEF022A5D8986"><tbody><tr><td>Command Region: Convert to PFX command format</td></tr><tr><td><pre><code><span>pvk2pfx</span><span>.</span><span>exe</span><span>" -pvk &lt;name-of-private-key-file&gt;.pvk -pi &lt;password-for-pvk&gt; -spc &lt;name-of-certification-file-name&gt;.cer 
-pfx &lt;name-of-pfx-file&gt; -po &lt;password-for-pfx&gt;</span></code></pre></td></tr></tbody></table>

Where `<name-of-private-key-file>` is the name of pvk file you created, `<password-for-pvk>` is the password you assigned to the pvk file. `<name-of-certification-file-name>` is the name of the certification file or .cer file. `<name-of-pfx-file>` is the name of the .pfx. `<password-for-pfx>` is a password to be assigned to the .pfx file.

For example:

<table summary="" id="GUID-B9A067F4-234F-47F8-A5EE-0D84A93FA98E__TABLE_27049496D3F04BC2A51BB0056D3E7727"><tbody><tr><td>Command Region: Convert to PFX example</td></tr><tr><td><pre><code><span>"C:\Program Files (x86)\Windows Kits\8.1\bin\x64\pvk2pfx.exe"</span><span> </span><span>-</span><span>pvk </span><span>MyCert</span><span>.</span><span>pvk </span><span>-</span><span>pi password123 </span><span>-</span><span>spc </span><span>MyCert</span><span>.</span><span>cer </span><span>-</span><span>pfx </span><span>MyCert</span><span>.</span><span>pfx </span><span>-</span><span>po password234</span></code></pre></td></tr></tbody></table>

When the operation succeeds, the command ends without error message and a .pfx file will be created.

Once you have a pfx file, you can [Digitally Signing Your App](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Digitally_Signing_Your_Revit_Add_in_Digitally_Signing_Your_App_html).

## Import the Digital Certificate to Windows Certificate Store

One more step you need when you are making your own digital certificate is to import it to your computer. You can do this in Certificate Manager ([CertMgr.msc](https://msdn.microsoft.com/EN-US/LIBRARY/E78BYTA0(V=VS.110).ASPX)) or CertUtils.exe tool. Here we use the UI tool. Please refer [here for alternatives](http://help.autodesk.com/view/ACD/2018/ENU/?guid=GUID-19D6716A-0AD1-4A7A-82BA-A067E6D65F66).

1.  From Start >> Run >> CertMgr.msc. (Or on Windows 8.1/10, right click on Start >> Run >> CertMgr.msc) CertMgr opens.
2.  On CertMgr dialog, right click on **Trusted Publishers** >> All Tasks >> Import …
3.  Follow the instructions on Certificate Import Wizard. Click Next.
4.  On a dialog which asks "Files to Import", choose the pfx file you want to import.
5.  On the "Password" dialog, enter the password. Keep "Include all extended properties" checked.
6.  Choose "Place all certificates in the following store" then Click Next.
7.  Confirm and Finish.
8.  If you see "Import a new Private signature key" dialog, click OK. (This part may differ depending on your environment.) ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/certmgr.png)
9.  Repeat the same step with **Trusted Root Certification Authorities**. This step is to validate digitally signed binary files.
