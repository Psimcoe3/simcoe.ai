[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Unit Property

---



|  |
| --- |
| [BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.htm)   [See Also](#seeAlsoToggle) |

The unit of measure for imported geometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ImportUnit Unit { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Unit As ImportUnit 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ImportUnit Unit { 	ImportUnit get (); 	void set (ImportUnit value); } ``` |

# Remarks

Units are used to calculate the import scale unless scale is defined explicitly using CustomScale, in which case Units will be ignored. Feet, inches, meters, centimeters, decimeters, millimeters are all supported. If Default unit is set, Revit will read and use the units from the file. If units are not available or accessible there, Revit will default to %overrideUnit%.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)