[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrimExtendCurves Method

---



|  |
| --- |
| [IRebarUpdateServer Interface](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm)   [See Also](#seeAlsoToggle) |

This function is supposed to trim or extend curves that were obtained from calling GenerateCurves(). Also in this function can be set new constraints for start and end handles.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` bool TrimExtendCurves( 	RebarTrimExtendData trimExtendData ) ``` |

 

| Visual Basic |
| --- |
| ``` Function TrimExtendCurves ( _ 	trimExtendData As RebarTrimExtendData _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool TrimExtendCurves( 	RebarTrimExtendData^ trimExtendData ) ``` |

#### Parameters

trimExtendData
:   Type:  [Autodesk.Revit.DB.Structure RebarTrimExtendData](980b816d-dc7e-7550-3e37-61482516b5ab.htm)    
     Use the members of this class to access the inputs and define any trim/extend actions to be taken for bars in the free form rebar.

#### Return Value

Returns true if the trim/extend was successful, false otherwise.

# Remarks

This function is called in the regeneration context when at least one data in trimExtendData parameter was changed. It is called immediately after GenerateCurves() and only if GenerateCurves() returns true.

If new constraints were created for start or end handle, a new regeneration will take place and the new constraints will become the rebar's actual constraints.

If new curves will be added by calling TrimExtendData.AddBarGeometry(), the existing curves in Rebar element will be replaced with these curves. It will not add curves to the existing ones.

# See Also

[IRebarUpdateServer Interface](3e845cad-eca0-ccb3-785b-48a32a9f2677.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)