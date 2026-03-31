[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Double, Double, ElementId, Double)

---



|  |
| --- |
| [FabricWireItem Class](ec68f4e9-ba5a-6036-7d5a-2718689ef95f.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of a single Fabric wire.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static FabricWireItem Create( 	double distance, 	double wireLength, 	ElementId wireType, 	double wireOffset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	distance As Double, _ 	wireLength As Double, _ 	wireType As ElementId, _ 	wireOffset As Double _ ) As FabricWireItem ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricWireItem^ Create( 	double distance,  	double wireLength,  	ElementId^ wireType,  	double wireOffset ) ``` |

#### Parameters

distance
:   Type:  System Double    
     The distance between this wire and the next wire in the Custom Fabric Sheet

wireLength
:   Type:  System Double    
     Length of this wire

wireType
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The wire type of this wire

wireOffset
:   Type:  System Double    
     The offset between two wires in the same line

#### Return Value

The newly created Fabric wire instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for distance is not a number -or- The given value for wireLength is not a number -or- wireType is not a valid Element identifier. -or- The given value for wireOffset is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for distance must be between 0 and 30000 feet. -or- The given value for wireLength must be greater than 0 and no more than 30000 feet. -or- The given value for wireOffset must be between 0 and 30000 feet. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[FabricWireItem Class](ec68f4e9-ba5a-6036-7d5a-2718689ef95f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)