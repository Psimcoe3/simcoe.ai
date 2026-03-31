[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Activate Method

---



|  |
| --- |
| [FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)   [See Also](#seeAlsoToggle) |

Activates the symbol to ensure that its geometry is accessible.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Activate() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Activate ``` |

 

| Visual C++ |
| --- |
| ``` public: void Activate() ``` |

# Remarks

Symbols that are not used in the document may be deactivated to conserve memory and regeneration time. When the symbol is inactive, its geometry is empty and should not be accessed. In order to access geometry of a symbol that is not active in the document, first check its  [IsActive](69706e35-87cc-a6d9-68fe-90a41c1c48db.htm)  property. Note that until the document is regenerated, the newly activated symbol's geometry will still be empty.

# See Also

[FamilySymbol Class](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)