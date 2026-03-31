[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectDuctPlaceholdersAtElbow Method (Document, Connector, Connector)

---



|  |
| --- |
| [MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Connects a pair of placeholders that can intersect in an Elbow connection.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool ConnectDuctPlaceholdersAtElbow( 	Document document, 	Connector connector1, 	Connector connector2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConnectDuctPlaceholdersAtElbow ( _ 	document As Document, _ 	connector1 As Connector, _ 	connector2 As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ConnectDuctPlaceholdersAtElbow( 	Document^ document,  	Connector^ connector1,  	Connector^ connector2 ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

connector1
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the first placeholder.

connector2
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the second placeholder.

#### Return Value

True if connection succeeds, false otherwise.

# Remarks

The placeholders may have a physical intersection but this is not required. If they are not intersecting the connectors must be coplanar and able to be moved to intersect each other. If connection fails, the placeholders cannot be physically connected.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
//Create a point to be the connection point of two ductPlaceholders
XYZ connectionPoint = new XYZ(150, 0, 0);

//Create two new ductPlaceholders, duct1 and duct2, each ductPlaceholder has connectionPoint as its parameter
Duct duct1 = Duct.CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, new XYZ(100, 0, 0), connectionPoint);
Duct duct2 = Duct.CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, connectionPoint, new XYZ(150, 50, 0));

//Get Connectors of duct1 and duct2's ConnectorManager and change their type to IEnumerable<Connector>
//Get the first connector from the IEnumerable where the origin of the connector is almost equal to connectionPoint
Connector connector1 = duct1.ConnectorManager.Connectors.Cast<Connector>().Where(c => c.Origin.IsAlmostEqualTo(connectionPoint)).First();
Connector connector2 = duct2.ConnectorManager.Connectors.Cast<Connector>().Where(c => c.Origin.IsAlmostEqualTo(connectionPoint)).First();

//Connect duct1 and duct2 with elbow fitting by their intersecting connectors(whose origin is almost equal to connectionPoint)
bool connectResult = MechanicalUtils.ConnectDuctPlaceholdersAtElbow(document, connector1, connector2);

//Convert duct1 and duct2 to real ducts
ICollection<ElementId> convertedElementsId = MechanicalUtils.ConvertDuctPlaceholders(document, new ElementId[] { duct1.Id, duct2.Id });
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
'Create a point to be the connection point of two ductPlaceholders
Dim connectionPoint As New XYZ(150, 0, 0)

'Create two new ductPlaceholders, duct1 and duct2, each ductPlaceholder has connectionPoint as its parameter
Dim duct1 As Duct = Duct.CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, New XYZ(100, 0, 0), connectionPoint)
Dim duct2 As Duct = Duct.CreatePlaceholder(document, systemTypeId, ductTypeId, levelId, connectionPoint, New XYZ(150, 50, 0))

'Get Connectors of duct1 and duct2's ConnectorManager and change their type to IEnumerable<Connector>
'Get the first connector from the IEnumerable where the origin of the connector is almost equal to connectionPoint
Dim connector1 As Connector = duct1.ConnectorManager.Connectors.Cast(Of Connector)().Where(Function(c) c.Origin.IsAlmostEqualTo(connectionPoint)).First()
Dim connector2 As Connector = duct2.ConnectorManager.Connectors.Cast(Of Connector)().Where(Function(c) c.Origin.IsAlmostEqualTo(connectionPoint)).First()

'Connect duct1 and duct2 with elbow fitting by their intersecting connectors(whose origin is almost equal to connectionPoint)
Dim connectResult As Boolean = MechanicalUtils.ConnectDuctPlaceholdersAtElbow(document, connector1, connector2)

'Convert duct1 and duct2 to real ducts
Dim convertedElementsId As ICollection(Of ElementId) = MechanicalUtils.ConvertDuctPlaceholders(document, New ElementId() {duct1.Id, duct2.Id})
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The owner of connector is not duct placeholder. -or- The owners of connectors belong to different types of system. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)

[ConnectDuctPlaceholdersAtElbow Overload](7b82eb6f-4daf-cc0b-0ae6-9468c95a7245.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)