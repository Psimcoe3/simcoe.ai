[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalResourceLoadData Class

---



|  |
| --- |
| [Members](579ff09c-481b-872a-0414-b8b7cb10b2c3.htm)   [See Also](#seeAlsoToggle) |

This class contains the input and output data resulting from invoking an IExternalResourceServer's LoadResource method.

After the call to LoadResource, the resulting ExternalResourceLoadData will be passed into IExternalResourceServer.HandleLoadResourceResults() so that appropriate UI can be displayed.

Server providers can inspect the ExternalResourceLoadData to get an ExternalResourceLoadContent object of the subclass appropriate to the external resource. The class also contains a copy of the ExternalResourceReference, and information about the context of the load operation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class ExternalResourceLoadData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExternalResourceLoadData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalResourceLoadData : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExternalResourceLoadData

# See Also

[ExternalResourceLoadData Members](579ff09c-481b-872a-0414-b8b7cb10b2c3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)