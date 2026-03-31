[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewMechanicalSystem Method

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new MEP mechanical system element.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public MechanicalSystem NewMechanicalSystem( 	Connector baseEquipmentConnector, 	ConnectorSet connectors, 	DuctSystemType ductSystemType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewMechanicalSystem ( _ 	baseEquipmentConnector As Connector, _ 	connectors As ConnectorSet, _ 	ductSystemType As DuctSystemType _ ) As MechanicalSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: MechanicalSystem^ NewMechanicalSystem( 	Connector^ baseEquipmentConnector,  	ConnectorSet^ connectors,  	DuctSystemType ductSystemType ) ``` |

#### Parameters

baseEquipmentConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     One connector within base equipment which is used to connect with the system. The base equipment is optional for the system, so this argument may be    a null reference (  Nothing  in Visual Basic)  . The baseEquipmentConnector should not be included in the connectors.

connectors
:   Type:  [Autodesk.Revit.DB ConnectorSet](a9821fc1-54cf-5f69-13a9-25d506ecb048.htm)    
     Connectors that will connect to the system. The owner elements of these connectors will be added into system as its elements.

ductSystemType
:   Type:  [Autodesk.Revit.DB.Mechanical DuctSystemType](108631a7-6d3a-a5f6-cc0c-0579ca8cf999.htm)    
     The system type.

#### Return Value

If creation was successful then an instance of mechanical system is returned, otherwise an exception with information will be thrown.

# Remarks

This method will regenerate the document even in manual regeneration mode.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// create a connector set for new mechanical system
ConnectorSet connectorSet = new ConnectorSet();
// Base equipment connector
Connector baseConnector = null;

// Select a Parallel Fan Powered VAV and some Supply Diffusers
// prior to running this example
ConnectorSetIterator csi = null;
ICollection<ElementId> selectedIds = uiDocument.Selection.GetElementIds();
Document document = uiDocument.Document;
foreach (ElementId id in selectedIds)
{
    Element e = document.GetElement(id);
    if (e is FamilyInstance)
    {
        FamilyInstance fi = e as FamilyInstance;
        Family family = fi.Symbol.Family;
        // Assume the selected Mechanical Equipment is the base equipment for new system
        if (family.FamilyCategory.Name == "Mechanical Equipment")
        {
            //Find the "Out" and "SupplyAir" connector on the base equipment
            if (null != fi.MEPModel)
            {
                csi = fi.MEPModel.ConnectorManager.Connectors.ForwardIterator();
                while (csi.MoveNext())
                {
                    Connector conn = csi.Current as Connector;
                    if (conn.Direction == FlowDirectionType.Out && conn.DuctSystemType == DuctSystemType.SupplyAir)
                    {
                        baseConnector = conn;
                        break;
                    }
                }
            }
        }
        else if (family.FamilyCategory.Name == "Air Terminals")
        {
            // add selected Air Terminals to connector set for new mechanical system
            csi = fi.MEPModel.ConnectorManager.Connectors.ForwardIterator();
            csi.MoveNext();
            connectorSet.Insert(csi.Current as Connector);
        }
    }
}

MechanicalSystem mechanicalSys = null;
if (null != baseConnector && connectorSet.Size > 0)
{
    // create a new SupplyAir mechanical system
    mechanicalSys = uiDocument.Document.Create.NewMechanicalSystem(baseConnector, connectorSet, DuctSystemType.SupplyAir);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' create a connector set for new mechanical system
Dim connectorSet As New ConnectorSet()
' Base equipment connector
Dim baseConnector As Connector = Nothing

' Select a Parallel Fan Powered VAV and some Supply Diffusers
' prior to running this example
Dim csi As ConnectorSetIterator = Nothing
Dim selectedIds As ICollection(Of ElementId) = uiDocument.Selection.GetElementIds()
Dim document As Document = uiDocument.Document
For Each id As ElementId In selectedIds
    Dim e As Element = document.GetElement(id)
    If TypeOf e Is FamilyInstance Then
        Dim fi As FamilyInstance = TryCast(e, FamilyInstance)
        Dim family As Family = fi.Symbol.Family
        ' Assume the selected Mechanical Equipment is the base equipment for new system
        If family.FamilyCategory.Name = "Mechanical Equipment" Then
            'Find the "Out" and "SupplyAir" connector on the base equipment
            If fi.MEPModel IsNot Nothing Then
                csi = fi.MEPModel.ConnectorManager.Connectors.ForwardIterator()
                While csi.MoveNext()
                    Dim conn As Connector = TryCast(csi.Current, Connector)
                    If conn.Direction = FlowDirectionType.Out AndAlso conn.DuctSystemType = DuctSystemType.SupplyAir Then
                        baseConnector = conn
                        Exit While
                    End If
                End While
            End If
        ElseIf family.FamilyCategory.Name = "Air Terminals" Then
            ' add selected Air Terminals to connector set for new mechanical system
            csi = fi.MEPModel.ConnectorManager.Connectors.ForwardIterator()
            csi.MoveNext()
            connectorSet.Insert(TryCast(csi.Current, Connector))
        End If
    End If
Next

Dim mechanicalSys As MechanicalSystem = Nothing
If baseConnector IsNot Nothing AndAlso connectorSet.Size > 0 Then
    ' create a new SupplyAir mechanical system
    mechanicalSys = uiDocument.Document.Create.NewMechanicalSystem(baseConnector, connectorSet, DuctSystemType.SupplyAir)
End If
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when calling this function outside of the Autodesk Revit MEP product. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input connectors parameter value is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the ductSystemType parameter is out of permitted scope. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when some connectors can't be used to create the mechanical system. All the input connectors and base equipment connector should match system type and domain with the system, and they should not have been used in another system. The owner of BaseConnector should be a mechanical equipment, and the owner of other connectors should be a mechanical equipment or air terminal. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the mechanical system creation failed. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)