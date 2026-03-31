[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDBServerId Method

---



|  |
| --- |
| [IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.htm)   [See Also](#seeAlsoToggle) |

Implement this method to return the id of the server which is associated with this UI server.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` Guid GetDBServerId() ``` |

 

| Visual Basic |
| --- |
| ``` Function GetDBServerId As Guid ``` |

 

| Visual C++ |
| --- |
| ``` Guid GetDBServerId() ``` |

#### Return Value

The id of the associated DB server.

# Remarks

If there's no DB server associated with this UI server, an empty GUID value will be returned.

# See Also

[IExternalResourceUIServer Interface](aee37f3f-98e9-79c6-e02d-1b07e3ffd89c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)