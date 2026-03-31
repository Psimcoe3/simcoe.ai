[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyInstance Method (XYZ, FamilySymbol, View)

---



|  |
| --- |
| [ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)   [See Also](#seeAlsoToggle) |

Add a new family instance into the Autodesk Revit document, using an origin and a view where the instance should be placed.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstance NewFamilyInstance( 	XYZ origin, 	FamilySymbol symbol, 	View specView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFamilyInstance ( _ 	origin As XYZ, _ 	symbol As FamilySymbol, _ 	specView As View _ ) As FamilyInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyInstance^ NewFamilyInstance( 	XYZ^ origin,  	FamilySymbol^ symbol,  	View^ specView ) ``` |

#### Parameters

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The origin of family instance. If created on a  [ViewPlan](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)  , the origin will be projected onto the  [ViewPlan](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)  .

symbol
:   Type:  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
     A family symbol object that represents the type of the instance that is to be inserted.

specView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The 2D view in which to place the family instance.

#### Return Value

If creation was successful then an instance to the new object is returned.

# Remarks

This overload applies only to 2D family symbols (detail components, annotation symbols, titleblocks, etc.). The type/symbol that is used must be loaded into the document before this method is called. Families and their symbols can be loaded using the Document.LoadFamily or Document.LoadFamilySymbol methods.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | One or more required arguments was    a null reference (  Nothing  in Visual Basic) |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input family PlacementType was not ViewBased, the input view was not 2D, Thrown if The symbol is not active. or instances of the input FamilySymbol are not permitted on a view of this type. |

# See Also

[ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)

[NewFamilyInstance Overload](451ee414-cea0-e9bd-227b-c73bc93507dd.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)