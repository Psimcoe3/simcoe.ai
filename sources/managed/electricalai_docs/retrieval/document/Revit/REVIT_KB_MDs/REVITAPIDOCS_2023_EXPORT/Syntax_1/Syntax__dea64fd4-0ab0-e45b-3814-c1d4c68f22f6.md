[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UniqueID Property

---



|  |
| --- |
| [SteelElementProperties Class](911b649a-d108-14a2-dc09-8e97d489c17d.htm)   [See Also](#seeAlsoToggle) |

This method will return the fabrication id. This represents the link between the Revit and the Steel Core element.

**Namespace:**   [Autodesk.Revit.DB.Steel](9b98b590-ace1-9487-a688-8942d90305f1.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public Guid UniqueID { get; internal set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UniqueID As Guid 	Get 	Friend Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Guid UniqueID { 	Guid get (); 	internal: void set (Guid value); } ``` |

# Remarks

This id should not be confused with the guid returned by ExportUtils.GetExportId().

# See Also

[SteelElementProperties Class](911b649a-d108-14a2-dc09-8e97d489c17d.htm)

[Autodesk.Revit.DB.Steel Namespace](9b98b590-ace1-9487-a688-8942d90305f1.htm)