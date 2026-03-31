[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceReference Class

---



|  |
| --- |
| [Members](dbd1a1bb-2419-96be-f4e0-bea9c627cd9a.htm)   [See Also](#seeAlsoToggle) |

This class identifies an external resource provided by an IExternalResourceServer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class ExternalResourceReference : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExternalResourceReference _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalResourceReference : IDisposable ``` |

# Remarks

The class contains:

* The id of the IExternalResourceServer from which the resource was obtained.
* A (String, String) map containing information that is meaningful to the server for accessing the desired data. This could be something as simple as "4" to indicate that Revit wants option 4 from a range of several choices, or something more detailed, such as a filename or directory path.
* A String indicating the version of the resource that was most recently loaded in Revit.
* A (String, String) map containing "in session" information that is meaningful to the server, but which does not need to be saved permanently in the document on disk.

When calling an IExternalResourceServer, Revit will provide an ExternalResourceReference to identify the specific resource that Revit is using from that server. The server can then use the relevant information in the (String, String) maps to retrieve the data from the correct source.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExternalResourceReference

# See Also

[ExternalResourceReference Members](dbd1a1bb-2419-96be-f4e0-bea9c627cd9a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)