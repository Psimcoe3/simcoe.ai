[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GlobalParametersManager Class

---



|  |
| --- |
| [Members](9940520e-4932-0326-40e5-9b47b2a6b812.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A class to access and query information about global parameters in Revit models.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class GlobalParametersManager : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class GlobalParametersManager _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class GlobalParametersManager : IDisposable ``` |

# Remarks

This class provides access to general information and data of Global Parameter elements in a particular model. First of all, it is important to know that global parameters can be had in main project document; there are not supported in family documents. Availability of global parameters in a document can be tested by calling  [AreGlobalParametersAllowed(Document)](0191434b-d8c8-ed25-c81b-2679e8201460.htm)  method.

Global Parameter in a document can be obtained by calling either  [GetAllGlobalParameters(Document)](62b46073-1a11-0cc8-1798-8d6d87719888.htm)  or  [FindByName(Document, String)](7c7a7bd3-18e8-d9be-d9a7-66cd9ecdccc7.htm)  . The former returns a set of all global parameters in the document, while the latter returns just the requested one, providing it exists.

Each global parameters must be created with a valid name that is unique in the scope of the document. To test whether a particular name is unique, programmer can use the  [IsUniqueName(Document, String)](30f6c20b-2ddd-b584-8770-d7968bf70c29.htm)  method.

More details about creating and manipulating global parameters can be found in the description of the  [GlobalParameter](b0e53a4a-84ad-abb4-358d-9797870f101b.htm)  class.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
/// <summary>
/// Counts all global parameter elements defined in the given document. 
/// </summary>
/// <param name="document">Revit project document.</param>
/// <returns>Total number of all global parameter elements in the document</returns>
public int CountAllGlobalParameters(Document document)
{
    // Global parameters are not available in all documents.
    // They are available in projects, but not in families.
    if (GlobalParametersManager.AreGlobalParametersAllowed(document))
    {
        return GlobalParametersManager.GetAllGlobalParameters(document).Count;
    }

    return 0;   // no global parameters in this document
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' <summary>
' Counts all global parameter elements defined in the given document. 
' </summary>
' <param name="document">Revit project document.</param>
' <returns>Total number of all global parameter elements in the document</returns>
Public Function CountAllGlobalParameters(document As Document) As Integer
    ' Global parameters are not available in all documents.
    ' They are available in projects, but not in families.
    If GlobalParametersManager.AreGlobalParametersAllowed(document) Then
        Return GlobalParametersManager.GetAllGlobalParameters(document).Count
    End If

    Return 0
    ' no global parameters in this document
End Function
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB GlobalParametersManager

# See Also

[GlobalParametersManager Members](9940520e-4932-0326-40e5-9b47b2a6b812.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)