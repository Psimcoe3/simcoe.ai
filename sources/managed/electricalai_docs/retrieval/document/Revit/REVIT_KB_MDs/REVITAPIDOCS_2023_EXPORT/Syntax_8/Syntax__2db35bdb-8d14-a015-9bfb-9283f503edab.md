[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnInstanceBegin Method

---



|  |
| --- |
| [IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This method marks the start of processing of an instance node (e.g. a family instance).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` RenderNodeAction OnInstanceBegin( 	InstanceNode node ) ``` |

 

| Visual Basic |
| --- |
| ``` Function OnInstanceBegin ( _ 	node As InstanceNode _ ) As RenderNodeAction ``` |

 

| Visual C++ |
| --- |
| ``` RenderNodeAction OnInstanceBegin( 	InstanceNode^ node ) ``` |

#### Parameters

node
:   Type:  [Autodesk.Revit.DB InstanceNode](4f7fbd19-9a61-c173-2b4f-9c0be9e550bb.htm)

#### Return Value

Return RenderNodeAction.Skip if you wish to skip processing this family instance, or return RenderNodeAction.Proceed otherwise.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
/// <summary>
/// This method marks the start of processing of an Instance node (e.g. a family instance).
/// </summary>
public RenderNodeAction OnInstanceBegin(InstanceNode node)
{
   // We can get particular information about the family instance and its type if we need to
   ElementId symbolId = node.GetSymbolGeometryId().SymbolId;
   FamilySymbol famSymbol = m_document.GetElement(symbolId) as FamilySymbol;

   // Typically, an export context has to manage a stack of transformation
   // for all nested objects, such as instances, lights, links, etc.
   // A combined transformation needs to be applied to the incoming geometry
   // (providing all geometry is to be flattened in the resultant format.)
   m_TransformationStack.Push(m_TransformationStack.Peek().Multiply(node.GetTransform()));

   // We can either skip this instance or proceed with rendering it.
   return RenderNodeAction.Proceed;
}

/// <summary>
/// This method marks the end of processing of an Instance Node (e.g. a family instance).
/// </summary>
public void OnInstanceEnd(InstanceNode node)
{
   // Note: This method is invoked even for instances that were skipped.

   // If we maintain a transformation stack, we need to remove the latest one from it.
   m_TransformationStack.Pop();
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' <summary>
' This method marks the end of processing of an Instance Node (e.g. a family instance).
' </summary>
Public Function OnInstanceBegin(node As InstanceNode) As RenderNodeAction Implements IExportContext.OnInstanceBegin
    ' We can get particular information about the family instance and its type if we need to
    Dim symbolId As ElementId = node.GetSymbolGeometryId().SymbolId
    Dim famSymbol As FamilySymbol = TryCast(m_document.GetElement(symbolId), FamilySymbol)

    ' Typically, an export context has to manage a stack of transformation
    ' for all nested objects, such as instances, lights, links, etc.
    ' A combined transformation needs to be applied to the incoming geometry
    ' (providing all geometry is to be flattened in the resultant format.)
    m_TransformationStack.Push(m_TransformationStack.Peek().Multiply(node.GetTransform()))

    ' We can either skip this instance or proceed with rendering it.
    Return RenderNodeAction.Proceed
End Function

' <summary>
' This method marks the end of processing a family instance
' </summary>
Public Sub OnInstanceEnd(node As InstanceNode) Implements IExportContext.OnInstanceEnd
    ' Note: This method is invoked even for instances that were skipped.


    ' If we maintain a transformation stack, we need to remove the latest one from it.
    m_TransformationStack.Pop()
End Sub
```

# See Also

[IExportContext Interface](7d0dc6df-db0e-6a07-3b42-8dde1bedb3c1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)