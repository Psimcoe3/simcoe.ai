[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathName Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

The fully qualified path of the document's disk file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string PathName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PathName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ PathName { 	String^ get (); } ``` |

# Remarks

This string is empty if the project has not been saved or does not have a disk file associated with it yet. Note that the pathname will be empty if a document is detached. See  [IsDetached](0792283e-f112-0a57-d0d9-e79e6b9ea5b9.htm)  .

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
string docPathName = document.PathName;
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim docPathName As String = document.PathName
```

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)