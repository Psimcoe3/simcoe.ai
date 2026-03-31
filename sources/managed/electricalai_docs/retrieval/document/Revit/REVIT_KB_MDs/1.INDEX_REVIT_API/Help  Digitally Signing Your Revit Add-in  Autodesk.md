---
created: 2026-01-28T21:34:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Digitally_Signing_Your_Revit_Add_in_html
author: 
---

# Help | Digitally Signing Your Revit Add-in | Autodesk

> ## Excerpt
> Revit checks security credentials of add-ins.

---
Revit checks security credentials of add-ins.

If an add-in is not digitally signed with a certificate issued by a trusted certificate authority, Revit pops up a dialog when opening asking the user to confirm if he/she wants to load the application. The figure below shows an example of the security warning dialog when an unsigned add-in is detected. The user is presented with choices of: 1) allowing the same add-in to always load from now on, 2) load only this time and ask again next time, and 3) do not allow to load the add-in.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/UnsignedAddIn.png)

If you are professional developer and your application is already digitally signed by a trusted certificate authority, your add-in is already compatible with the digital signature checking in Revit. The following sections are intended for developers who author add-ins, but who are not familiar with digital signing in Revit.
