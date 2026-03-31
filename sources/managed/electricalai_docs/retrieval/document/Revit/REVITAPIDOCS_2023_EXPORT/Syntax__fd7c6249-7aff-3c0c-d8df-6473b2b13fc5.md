[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBuildingConstruction Method

---



|  |
| --- |
| [MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)   [See Also](#seeAlsoToggle) |

Sets the Building Construction of the Project Information.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetBuildingConstruction( 	ConstructionType constructionType, 	Construction buildingConstruction ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBuildingConstruction ( _ 	constructionType As ConstructionType, _ 	buildingConstruction As Construction _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBuildingConstruction( 	ConstructionType constructionType,  	Construction^ buildingConstruction ) ``` |

#### Parameters

constructionType
:   Type:  [Autodesk.Revit.DB.Analysis ConstructionType](5f6be035-3a2d-77ad-8402-4d6b87dec818.htm)    
     The Construction Type of Building Construction.

buildingConstruction
:   Type:  [Autodesk.Revit.DB Construction](b43d097e-b798-2aea-1008-ac79f71d3fc4.htm)    
     The Building Construction to be set.

# Remarks

This function is used to set the Building Construction of the Project Information.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | buildingConstruction is NULL. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Sets construction type to an invalid value. - or - Can not set construction type. |

# See Also

[MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)