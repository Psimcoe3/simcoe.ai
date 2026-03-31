[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanAddBarGeometry Method

---



|  |
| --- |
| [RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)   [See Also](#seeAlsoToggle) |

If the layout rule is Singe or FixedNumber or NumberWithSpacing this function will return true if getNumberOfBarGeometry() is less getBarsNumber(), false otherwise.

If the layout rule is MaximumSpacing or MinimumClearSpacing this function will return always true.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool CanAddBarGeometry() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanAddBarGeometry As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanAddBarGeometry() ``` |

#### Return Value

Returns true if we can add more bar geometry for the current layout, false otherwise.

# See Also

[RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)