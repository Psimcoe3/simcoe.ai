[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TypeBinding Class

---



|  |
| --- |
| [Members](b72804b4-596f-75db-37ab-ea78a51da3bc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

TypeBinding objects are used to bind a property to a Revit type, such as a wall type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class TypeBinding : ElementBinding ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TypeBinding _ 	Inherits ElementBinding ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TypeBinding : public ElementBinding ``` |

# Remarks

This differs from Instance bindings in that the property is then shared by all instances that use that type. Changing the parameter for one type affects all other instances that use that type.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public bool SetNewParameterToTypeWall(UIApplication app, DefinitionFile myDefinitionFile)
{
    // Create a new group in the shared parameters file
    DefinitionGroups myGroups = myDefinitionFile.Groups;
    DefinitionGroup myGroup = myGroups.Create("MyParameters");

    // Create a type definition
    ExternalDefinitionCreationOptions option = new ExternalDefinitionCreationOptions("CompanyName", SpecTypeId.String.Text);
    Definition myDefinition_CompanyName = myGroup.Definitions.Create(option);

    // Create a category set and insert category of wall to it
    CategorySet myCategories = app.Application.Create.NewCategorySet();
    // Use BuiltInCategory to get category of wall
    Category myCategory = Category.GetCategory(app.ActiveUIDocument.Document, BuiltInCategory.OST_Walls);

    myCategories.Insert(myCategory);

    //Create an object of TypeBinding according to the Categories
    TypeBinding typeBinding = app.Application.Create.NewTypeBinding(myCategories);

    // Get the BingdingMap of current document.
    BindingMap bindingMap = app.ActiveUIDocument.Document.ParameterBindings;

    // Bind the definitions to the document
    bool typeBindOK = bindingMap.Insert(myDefinition_CompanyName, typeBinding,
      BuiltInParameterGroup.PG_TEXT);
    return typeBindOK;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function SetNewParameterToTypeWall(app As UIApplication, myDefinitionFile As DefinitionFile) As Boolean
   ' Create a new group in the shared parameters file
   Dim myGroups As DefinitionGroups = myDefinitionFile.Groups
   Dim myGroup As DefinitionGroup = myGroups.Create("MyParameters")

   ' Create a type definition
   Dim [option] As New ExternalDefinitionCreationOptions("CompanyName", SpecTypeId.String.Text)
   Dim myDefinition_CompanyName As Definition = myGroup.Definitions.Create([option])

   ' Create a category set and insert category of wall to it
   Dim myCategories As CategorySet = app.Application.Create.NewCategorySet()
   ' Use BuiltInCategory to get category of wall
   Dim myCategory As Category = Category.GetCategory(app.ActiveUIDocument.Document, BuiltInCategory.OST_Walls)

   myCategories.Insert(myCategory)

   'Create an object of TypeBinding according to the Categories
   Dim typeBinding As TypeBinding = app.Application.Create.NewTypeBinding(myCategories)

   ' Get the BingdingMap of current document.
   Dim bindingMap As BindingMap = app.ActiveUIDocument.Document.ParameterBindings

   ' Bind the definitions to the document
   Dim typeBindOK As Boolean = bindingMap.Insert(myDefinition_CompanyName, typeBinding, BuiltInParameterGroup.PG_TEXT)
   Return typeBindOK
End Function
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB Binding](47f6ad6f-8d00-af57-995e-dc6db1255f58.htm)    
  [Autodesk.Revit.DB ElementBinding](15ebf308-364c-2bef-e91c-dd6552e5ccbe.htm)    
  Autodesk.Revit.DB TypeBinding

# See Also

[TypeBinding Members](b72804b4-596f-75db-37ab-ea78a51da3bc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)