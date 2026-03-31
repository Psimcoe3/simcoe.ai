[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPath Method (String)

---



|  |
| --- |
| [ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)   [See Also](#seeAlsoToggle) |

Update the path of the file that specifies the image to be used.

The provided string path must specify a local file. The path can be absolute or relative to the project's location. ImageType will respectively use an absolute or relative path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetPath( 	string path ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPath ( _ 	path As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPath( 	String^ path ) ``` |

#### Parameters

path
:   Type:  System String    
     The file path that specifies the image to be used.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImageTypeOptions Class](981135c3-777b-df9b-747f-60a35b74e00e.htm)

[SetPath Overload](64f4404e-a352-6fc6-72e2-821855ae1c50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)