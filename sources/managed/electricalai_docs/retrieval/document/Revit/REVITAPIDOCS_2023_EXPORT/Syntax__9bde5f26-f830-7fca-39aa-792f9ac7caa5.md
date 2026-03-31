[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRegions Method

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Gets the face regions (created, for example, by the Split Face command) of the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public IList<Face> GetRegions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRegions As IList(Of Face) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Face^>^ GetRegions() ``` |

#### Return Value

A list of faces, one for the main face of the object hosting the Split Face (such as wall or floor) and one face for each Split Face regions.

# Remarks

Use the FaceSplitter class to filter and find elements which may generate face regions.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)