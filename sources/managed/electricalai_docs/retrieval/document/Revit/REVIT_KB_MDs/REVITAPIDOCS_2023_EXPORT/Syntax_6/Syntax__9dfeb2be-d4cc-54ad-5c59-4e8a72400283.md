[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceBasedPlacementType Property

---



|  |
| --- |
| [PromptForFamilyInstancePlacementOptions Class](d321705f-3f3a-bdcd-759a-882f9f62964a.htm)   [See Also](#seeAlsoToggle) |

The placement type to be used if prompting to place an instance of a face-based family. This option is ignored if placing a non-face-based family. If placing a face-based family, Default is an acceptable value, but will correspond to the first available selection in the user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public FaceBasedPlacementType FaceBasedPlacementType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FaceBasedPlacementType As FaceBasedPlacementType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FaceBasedPlacementType FaceBasedPlacementType { 	FaceBasedPlacementType get (); 	void set (FaceBasedPlacementType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PromptForFamilyInstancePlacementOptions Class](d321705f-3f3a-bdcd-759a-882f9f62964a.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)