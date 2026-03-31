[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new instance of a AnalyticalLink element between two Hubs.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static AnalyticalLink Create( 	Document doc, 	ElementId type, 	ElementId startHubId, 	ElementId endHubId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	type As ElementId, _ 	startHubId As ElementId, _ 	endHubId As ElementId _ ) As AnalyticalLink ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalyticalLink^ Create( 	Document^ doc,  	ElementId^ type,  	ElementId^ startHubId,  	ElementId^ endHubId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document to which new AnalyticalLink should be added.

type
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     AnalyticalLinkType for the new AnalyticalLink.

startHubId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Hub at start of AnalyticalLink.

endHubId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Hub at end of AnalyticalLink.

#### Return Value

The newly created AnalyticalLink instance.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void CreateLink(Document doc, AnalyticalElement fi1, AnalyticalElement fi2)
{
    FilteredElementCollector hubCollector = new FilteredElementCollector(doc);
    hubCollector.OfClass(typeof(Hub));  //Get all hubs
    ICollection<Element> allHubs = hubCollector.ToElements();
    FilteredElementCollector linktypeCollector = new FilteredElementCollector(doc);
    linktypeCollector.OfClass(typeof(AnalyticalLinkType));
    ElementId firstLinkType = linktypeCollector.ToElementIds().First();  //Get the first analytical link type.  
    // Get hub Ids from two selected family instance items
    ElementId startHubId = GetHub(fi1.Id, allHubs); 
    ElementId endHubId = GetHub(fi2.Id, allHubs);
    Transaction tran = new Transaction(doc, "Create Link");
    tran.Start();
    //Create a link between these two hubs.
    AnalyticalLink createdLink = AnalyticalLink.Create(doc, firstLinkType, startHubId, endHubId);  
    tran.Commit();
}

//Get the first Hub on a given AnalyticalModel element
private ElementId GetHub(ElementId hostId, ICollection<Element> allHubs)
{
    foreach (Element ehub in allHubs)
    {
        Hub hub = ehub as Hub;
        ConnectorManager manager = hub.GetHubConnectorManager();
        ConnectorSet connectors = manager.Connectors;
        foreach (Connector connector in connectors)
        {
            ConnectorSet refConnectors = connector.AllRefs;
            foreach (Connector refConnector in refConnectors)
            {
                if (refConnector.Owner.Id == hostId)
                {
                    return hub.Id;
                }
            }
        }
    }
    return ElementId.InvalidElementId;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub CreateLink(doc As Document, fi1 As AnalyticalElement, fi2 As AnalyticalElement)
    Dim hubCollector As New FilteredElementCollector(doc)
    hubCollector.OfClass(GetType(Hub))
    'Get all hubs
    Dim allHubs As ICollection(Of Element) = hubCollector.ToElements()
    Dim linktypeCollector As New FilteredElementCollector(doc)
    linktypeCollector.OfClass(GetType(AnalyticalLinkType))
    Dim firstLinkType As ElementId = linktypeCollector.ToElementIds().First()
    'Get the first analytical link type.  
    ' Get hub Ids from two selected family instance items
    Dim startHubId As ElementId = GetHub(fi1.Id, allHubs)
    Dim endHubId As ElementId = GetHub(fi2.Id, allHubs)
    Dim tran As New Transaction(doc, "Create Link")
    tran.Start()
    'Create a link between these two hubs.
    Dim createdLink As AnalyticalLink = AnalyticalLink.Create(doc, firstLinkType, startHubId, endHubId)
    tran.Commit()
End Sub

'Get the first Hub on a given AnalyticalModel element
Private Function GetHub(hostId As ElementId, allHubs As ICollection(Of Element)) As ElementId
    For Each ehub As Element In allHubs
        Dim hub As Hub = TryCast(ehub, Hub)
        Dim manager As ConnectorManager = hub.GetHubConnectorManager()
        Dim connectors As ConnectorSet = manager.Connectors
        For Each connector As Connector In connectors
            Dim refConnectors As ConnectorSet = connector.AllRefs
            For Each refConnector As Connector In refConnectors
                If refConnector.Owner.Id = hostId Then
                    Return hub.Id
                End If
            Next
        Next
    Next
    Return ElementId.InvalidElementId
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | startHubId is not a valid Hub ID for an AnalyticalLink element. -or- endHubId is not a valid Hub ID for an AnalyticalLink element. -or- Thrown if startHubId or endHubId do not represent ids of Hubs. -or- Thrown if startHubId == endHubId. -or- Thrown if type does not represent an id of an AnalyticalLinkType. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)