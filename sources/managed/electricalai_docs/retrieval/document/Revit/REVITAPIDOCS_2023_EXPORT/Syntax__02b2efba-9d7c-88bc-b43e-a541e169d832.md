[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, ViewSet, FBXExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports the document in 3D-Studio Max (FBX) format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Export( 	string folder, 	string name, 	ViewSet views, 	FBXExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Export ( _ 	folder As String, _ 	name As String, _ 	views As ViewSet, _ 	options As FBXExportOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Export( 	String^ folder,  	String^ name,  	ViewSet^ views,  	FBXExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     Output folder, into which file(s) will be exported. The folder must exist.

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     Either the name of a single file or a prefix for a set of files. If    a null reference (  Nothing  in Visual Basic)  or empty, automatic naming will be used.

views
:   Type:  [Autodesk.Revit.DB ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.htm)    
     Selection of views to be exported.Only 3D views are allowed.

options
:   Type:  [Autodesk.Revit.DB FBXExportOptions](faede206-7c81-c13d-b584-a49b56329941.htm)    
     Options applicable to the FBX format.

#### Return Value

Function returns true only if all specified views are exported successfully. The function returns False if exporting of any view fails, even if some views might have been exported successfully.

# Remarks

Though the 'options' argument is not currently used, an object still must be provided (may be    a null reference (  Nothing  in Visual Basic)  ).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input views is    a null reference (  Nothing  in Visual Basic) |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input views is an empty ViewSet. Thrown if any view in the views is not a 3D view. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)