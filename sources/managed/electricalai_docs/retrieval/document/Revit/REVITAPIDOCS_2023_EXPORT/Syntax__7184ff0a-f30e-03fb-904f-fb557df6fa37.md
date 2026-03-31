[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PostFailure Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Posts a failure to be displayed to the user at the end of transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureMessageKey PostFailure( 	FailureMessage failure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PostFailure ( _ 	failure As FailureMessage _ ) As FailureMessageKey ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureMessageKey^ PostFailure( 	FailureMessage^ failure ) ``` |

#### Parameters

failure
:   Type:  [Autodesk.Revit.DB FailureMessage](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)    
     The failure to be posted.

#### Return Value

A unique key that identifies posted failure message in a document. If exactly the same error is posted more than once, and not removed between the postings, returned key will be the same every time.

# Remarks

If code inside transaction detects a problem that needs to be communicated to the user, it should report these conditions via this method. Failures will be validated and possibly resolved at the end of transaction. Warnings posted via this method will not be stored in the document after they are resolved. A unique key returned by postFailure can be stored for the lifetime of transaction and used to remove failure message if it is no longer relevant.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Execute function for an Updater triggered when new FamilyInstances are added
public void Execute(UpdaterData data)
{
   Document doc = data.GetDocument();
   Autodesk.Revit.ApplicationServices.Application app = doc.Application;
   foreach (ElementId id in data.GetModifiedElementIds())
   {
      AnalyticalMember fi = doc.GetElement(id) as AnalyticalMember;
      if (fi.StructuralRole == AnalyticalStructuralRole.StructuralRoleBeam)
      {
         if (fi.IsSingleCurve() == true)
         {
            Curve beamCurve = fi.GetCurve();
            // enforce beam length minimum of 12 inches
            if (beamCurve.Length < 12.0)
            {
               FailureMessage failMessage =
                     new FailureMessage(BuiltInFailures.CurveFailures.TooShort);
               failMessage.SetFailingElement(id);
               doc.PostFailure(failMessage);
            }
         }
      }
   }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Execute function for an Updater triggered when new FamilyInstances are added
Public Sub Execute(data As UpdaterData) Implements IUpdater.Execute
   Dim doc As Document = data.GetDocument()
   Dim app As Autodesk.Revit.ApplicationServices.Application = doc.Application
   For Each id As ElementId In data.GetModifiedElementIds()
      Dim fi As FamilyInstance = TryCast(doc.GetElement(id), FamilyInstance)
      If fi.StructuralType = StructuralType.Beam Then
         Dim analyticalModel As Autodesk.Revit.DB.Structure.AnalyticalElement = Nothing
         Dim relManager As Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager = Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(doc)

         If (relManager Is Nothing) Then
            Exit Sub
         End If

         Dim counterpartId As ElementId = relManager.GetAssociatedElementId(fi.Id)
         If (counterpartId Is Nothing) Then
            Exit Sub
         End If

         analyticalModel = doc.GetElement(counterpartId)
         If analyticalModel.IsSingleCurve() = True Then
            Dim beamCurve As Curve = analyticalModel.GetCurve()
            ' enforce beam length minimum of 12 inches
            If beamCurve.Length < 12.0 Then
               Dim failMessage As New FailureMessage(BuiltInFailures.CurveFailures.TooShort)
               failMessage.SetFailingElement(id)
               doc.PostFailure(failMessage)
            End If
         End If
      End If
   Next
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Document must be in state of accepting posted failures and the failures must be appropriate for that current state. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)