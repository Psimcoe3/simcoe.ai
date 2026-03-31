[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChangeHostReference Method (Reference)

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Changes the connector host reference to a new planar face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void ChangeHostReference( 	Reference planarFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ChangeHostReference ( _ 	planarFace As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ChangeHostReference( 	Reference^ planarFace ) ``` |

#### Parameters

planarFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The planar face to place the connector on.

# Remarks

The connector referenced by a planar face alone is placed at the plane origin, and may be moved later along the planar face.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The face is not a planar face. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[ChangeHostReference Overload](c5862502-8bcb-ff4d-5f78-7ee301282dc5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)