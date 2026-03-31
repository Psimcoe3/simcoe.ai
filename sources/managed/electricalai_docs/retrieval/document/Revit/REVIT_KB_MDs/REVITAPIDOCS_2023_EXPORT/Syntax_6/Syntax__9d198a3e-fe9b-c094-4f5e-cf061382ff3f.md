[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)   [See Also](#seeAlsoToggle) |

Create a new StructuralConnectionType, allowing the specified annotation FamilySymbol to be applied to structural members.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static StructuralConnectionType Create( 	Document doc, 	StructuralConnectionApplyTo applyTo, 	string name, 	ElementId familySymbolId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	applyTo As StructuralConnectionApplyTo, _ 	name As String, _ 	familySymbolId As ElementId _ ) As StructuralConnectionType ``` |

 

| Visual C++ |
| --- |
| ``` public: static StructuralConnectionType^ Create( 	Document^ doc,  	StructuralConnectionApplyTo applyTo,  	String^ name,  	ElementId^ familySymbolId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

applyTo
:   Type:  [Autodesk.Revit.DB.Structure StructuralConnectionApplyTo](2d0e55f6-fbb5-a5c6-2423-6bb4e759d56e.htm)    
     Specify which type of member this connection type can be applied to.

name
:   Type:  System String    
     A name for the connection type. It must be unique within the document.

familySymbolId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of an annotation FamilySymbol. InvalidElementId is allowed. Otherwise, the FamilySymbol must be in the category "Connection Symbols" (OST\_StructConnectionSymbols) and have its "Apply To" parameter set to match the applyTo argument.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | familySymbolId is the id of some element that is not a FamilySymbol, is not of the category "Connection Symbols" (OST\_StructConnectionSymbols), or has its "Apply To" parameter not equal to applyTo. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)