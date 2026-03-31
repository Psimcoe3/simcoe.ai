[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### YoungModulus Property

---



|  |
| --- |
| [StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)   [See Also](#seeAlsoToggle) |

The Young's modulus of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public XYZ YoungModulus { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property YoungModulus As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ YoungModulus { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

This property cannot be used to set the Young's modulus for wood-based and isotropic materials. For such assets, use setYoungModulus instead. The value is in Newtons per foot meter (N/(ft Â· m)).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | When setting this property: the material type is wood. -or- When setting this property: the behavior is isotropic. |

# See Also

[StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)