[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoordinate Method

---



|  |
| --- |
| [PolyLine Class](f3de399b-5522-f96e-2589-70bfecc557a8.htm)   [See Also](#seeAlsoToggle) |

Gets the coordinate point of the specified index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ GetCoordinate( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCoordinate ( _ 	index As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetCoordinate( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the coordinates.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the index value is out of range. |

# See Also

[PolyLine Class](f3de399b-5522-f96e-2589-70bfecc557a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)