[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDefaultRebarBarType Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Creates a new RebarBarType object with a default name.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static ElementId CreateDefaultRebarBarType( 	Document ADoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDefaultRebarBarType ( _ 	ADoc As Document _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ CreateDefaultRebarBarType( 	Document^ ADoc ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The newly created type id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)