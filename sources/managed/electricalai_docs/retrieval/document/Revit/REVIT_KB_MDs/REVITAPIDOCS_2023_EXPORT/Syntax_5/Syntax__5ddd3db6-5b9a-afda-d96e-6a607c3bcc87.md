[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceNormal Property

---



|  |
| --- |
| [PlanarFace Class](e5f08848-bd35-4b17-ac7b-ae39fd817d6d.htm)   [See Also](#seeAlsoToggle) |

Normal of the planar face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ FaceNormal { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FaceNormal As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ FaceNormal { 	XYZ^ get (); } ``` |

# Remarks

This property is the "face normal" vector, and thus should return a vector consistently pointing out of the solid that this face is a boundary for (if it is a part of a solid).

# See Also

[PlanarFace Class](e5f08848-bd35-4b17-ac7b-ae39fd817d6d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)