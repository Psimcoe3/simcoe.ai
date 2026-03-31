[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

This method creates a constraint for a given Rebar Constrained Handle Tag. Will throw exception if used for Shape Driven Rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static RebarConstraint Create( 	RebarConstrainedHandle handle, 	IList<Reference> targetReferences, 	bool isConstraintToCover, 	double offsetValue ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	handle As RebarConstrainedHandle, _ 	targetReferences As IList(Of Reference), _ 	isConstraintToCover As Boolean, _ 	offsetValue As Double _ ) As RebarConstraint ``` |

 

| Visual C++ |
| --- |
| ``` public: static RebarConstraint^ Create( 	RebarConstrainedHandle^ handle,  	IList<Reference^>^ targetReferences,  	bool isConstraintToCover,  	double offsetValue ) ``` |

#### Parameters

handle
:   Type:  [Autodesk.Revit.DB.Structure RebarConstrainedHandle](08b4c4a3-3bb9-0801-9cc8-cd5420a306d9.htm)    
     The handle of the rebar that will be constrained.

targetReferences
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The references to which the rebar handle will be constrained. This collection must contain one or more references to faces of elements that can host rebar.

isConstraintToCover
:   Type:  System Boolean    
     If true the RebarConstraintType will be set to ToCover, otherwise RebarConstraintType will be set to FixedDistanceToHostFace.

offsetValue
:   Type:  System Double    
     The distance from references to the rebar handle.

#### Return Value

Returns the newly created RebarConstraint.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Constrained rebar is a shape driven rebar element. -or- handle is no longer valid. -or- targetReferences is empty. -or- targetReferences do not represent faces from structurals that can host rebar. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)