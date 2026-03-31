[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValidFamilySymbolId Method

---



|  |
| --- |
| [StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)   [See Also](#seeAlsoToggle) |

Checks whether the family symbol id is allowed for StructuralConnectionTypes with the given value for the applyTo property.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool ValidFamilySymbolId( 	Document doc, 	StructuralConnectionApplyTo applyTo, 	ElementId familySymbolId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ValidFamilySymbolId ( _ 	doc As Document, _ 	applyTo As StructuralConnectionApplyTo, _ 	familySymbolId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ValidFamilySymbolId( 	Document^ doc,  	StructuralConnectionApplyTo applyTo,  	ElementId^ familySymbolId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

applyTo
:   Type:  [Autodesk.Revit.DB.Structure StructuralConnectionApplyTo](2d0e55f6-fbb5-a5c6-2423-6bb4e759d56e.htm)

familySymbolId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

#### Return Value

True if %familySymbolId% is invalidElementId; or if it is the id of a FamilySymbol of category "Connection Symbols" (OST\_StructConnectionSymbols) with its "Apply To" parameter set to match the applyTo property. Returns false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)