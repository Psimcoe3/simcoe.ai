[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddFace Method

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

Adds a face to the currently open connected face set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AddFace( 	TessellatedFace face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddFace ( _ 	face As TessellatedFace _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddFace( 	TessellatedFace^ face ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB TessellatedFace](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)    
     Face to add. The 'face' parameter can be added only once, as its boundary loops will be cleared while adding and 'face' will become unusable.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The 'face' does not have enough loops and/or vertices to be valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A face set is closed and faces cannot be added to it. |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)