[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFailureDefinition Method

---



|  |
| --- |
| [FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates an instance of a FailureDefinition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FailureDefinition CreateFailureDefinition( 	FailureDefinitionId id, 	FailureSeverity severity, 	string messageString ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFailureDefinition ( _ 	id As FailureDefinitionId, _ 	severity As FailureSeverity, _ 	messageString As String _ ) As FailureDefinition ``` |

 

| Visual C++ |
| --- |
| ``` public: static FailureDefinition^ CreateFailureDefinition( 	FailureDefinitionId^ id,  	FailureSeverity severity,  	String^ messageString ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB FailureDefinitionId](b6ada360-a6fe-ebb6-b095-d74b37ade9bf.htm)    
     Unique identifier of the failure.

severity
:   Type:  [Autodesk.Revit.DB FailureSeverity](d0cdffe3-22c5-b764-8090-5104f044b000.htm)    
     The severity of the failure. Cannot be FailureSeverity::None.

messageString
:   Type:  System String    
     A user-visible string describing the failure.

#### Return Value

The created FailureDefinition instance.

# Remarks

The newly created FailureDefinition will be added to the FailureDefinitionRegistry. Because FailureDefinition could only be registered when Revit starting up, this function cannot be used after Revit has already started. Throws InvalidOperationException if invoked after Revit start-up is completed.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// define a new failure id for a warning about walls
FailureDefinitionId warnId = 
    new FailureDefinitionId(new Guid("FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"));

// register the new warning using FailureDefinition
FailureDefinition failDef = FailureDefinition.CreateFailureDefinition(warnId, 
    FailureSeverity.Warning, 
    "Wall is too big (>100'). Performance problems may result.");
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' define a new failure id for a warning about walls
Dim warnId As New FailureDefinitionId(New Guid("FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"))

' register the new warning using FailureDefinition
Dim failDef As FailureDefinition = FailureDefinition.CreateFailureDefinition(warnId, FailureSeverity.Warning, "Wall is too big (>100'). Performance problems may result.")
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The id of failure definition is not valid. -or- The id of failure definition is already used to register another FailureDefinition. -or- The severity of failures cannot be FailureSeverity::None. -or- Message string is empty or contains invalid characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)