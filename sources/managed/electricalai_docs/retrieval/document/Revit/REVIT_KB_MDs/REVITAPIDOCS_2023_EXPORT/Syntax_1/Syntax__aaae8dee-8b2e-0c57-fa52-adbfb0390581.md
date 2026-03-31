[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBendProfileWithFillets Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Returns the profile with generated fillets that defines the shape of the Fabric Sheet bending.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public CurveLoop GetBendProfileWithFillets() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBendProfileWithFillets As CurveLoop ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveLoop^ GetBendProfileWithFillets() ``` |

#### Return Value

The bend profile with generated fillets that defines the shape of the fabric sheet bending for bent fabric sheet, for flat fabric sheet    a null reference (  Nothing  in Visual Basic)  will be returned.

# Remarks

Returned curve loop is created automatically as a result of adding fillets to bend profile. The returned profile defines the center-curve of a wire. Note that bent Fabric Sheets can have planar geometry, but flat Fabric Sheets are always planar.

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)