---
created: 2026-01-28T20:40:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Revit Exceptions | Autodesk

> ## Excerpt
> When API methods encounter a non-fatal error, they throw an exception. Exceptions should be caught by Revit add-ins. The Revit API help file specifies exceptions that are typically encountered for specific methods. All Revit API methods throw a subclass of Autodesk.Revit.Exceptions.ApplicationException. These exceptions closely mirror standard .NET exceptions such as:

---
When API methods encounter a non-fatal error, they throw an exception. Exceptions should be caught by Revit add-ins. The Revit API help file specifies exceptions that are typically encountered for specific methods. All Revit API methods throw a subclass of Autodesk.Revit.Exceptions.ApplicationException. These exceptions closely mirror standard .NET exceptions such as:

-   ArgumentException
-   InvalidOperationException
-   FileNotFoundException

However, some of these subclasses are unique to Revit:

-   AutoJoinFailedException
-   RegenerationFailedException
-   ModificationOutsideTransactionException

In addition, there is a special exception type called InternalException, which represents a failure path which was not anticipated. Exceptions of this type carry extra diagnostic information which can be passed back to Autodesk for diagnosis.
