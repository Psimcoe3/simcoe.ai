[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemovePaint Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Remove the material painted on the element's face. If the face is currently not painted,it will do nothing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void RemovePaint( 	ElementId elementId, 	Face face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemovePaint ( _ 	elementId As ElementId, _ 	face As Face _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemovePaint( 	ElementId^ elementId,  	Face^ face ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element that the painted face belongs to.

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The painted element's face.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elementId does not exist in the document -or- The face doesn't belong to the element |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)