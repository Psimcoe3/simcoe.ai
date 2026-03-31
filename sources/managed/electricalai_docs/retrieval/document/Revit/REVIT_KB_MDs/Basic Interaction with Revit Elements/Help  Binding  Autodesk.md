---
created: 2026-01-28T20:49:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Binding_html
author: 
---

# Help | Binding | Autodesk

> ## Excerpt
> Binding is what ties shared parameters to elements in certain categories in the model.

---
Binding is what ties shared parameters to elements in certain categories in the model.

There are two types of binding available, Instance binding and Type binding. The key difference between the two is that the instance bound parameters appear on all instances of the elements in those categories. Changing the parameter on one does not affect the other instances of the parameter. The Type bound parameters appear only on the type object and is shared by all the instances that use that type. Changing the type bound parameter affects all instances of the elements that use that type. Note, a definition can only be bound to an instance or a type and not both.

To bind a parameter:

1.  Use an InstanceBinding or a TypeBinding object to create a new Binding object that includes the categories to which the parameter is bound.
2.  Add the binding and definition to the document using the BindingMap object available from the Document.ParameterBindings property.

The following class and method in the Autodesk.Revit.DB namespace provide more information on binding parameters to elements.

-   BindingMap Class
    -   Retrieved from the Document.ParameterBindings property.
    -   Parameter binding connects a parameter definition to elements within one or more categories.
    -   The map is used to interrogate existing bindings as well as generate new parameter bindings using the Insert method.
-   BindingMap.Insert() Method
    -   The binding object type dictates whether the parameter is bound to all instances or just types.
    -   A parameter definition cannot be bound to both instances and types.
    -   If the parameter binding exists, the method returns false.

### Type Binding

The TypeBinding objects are used to bind a property to a Revit type, such as a wall type. It differs from Instance bindings in that the property is shared by all instances identified in type binding. Changing the parameter for one type affects all instances of the same type.

The following code sample demonstrates how to add parameter definitions using a shared parameter file. The following code performs the same actions as using the dialog box in the Revit UI. Parameter definitions are created in the following order:

1.  A shared parameter file is created.
2.  A definition group and a parameter definition are created for the Walls type.
3.  The definition is bound to the wall type parameter in the current document based on the wall category.

#### Code Region 22-7: Adding type parameter definitions using a shared parameter file

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

### Instance Binding

The InstanceBinding object indicates binding between a parameter definition and a parameter in certain category instances.

Once bound, the parameter appears in all property dialog boxes for the instance (if the visible property is set to true). Changing the parameter in any one instance does not change the value in any other instance.

The following code sample demonstrates how to add parameter definitions using a shared parameter file. Parameter definitions are added in the following order:

1.  A shared parameter file is created
2.  A definition group and a definition for all Walls instances is created
3.  Definitions are bound to each wall instance parameter in the current document based on the wall category.

#### Code Region 22-8: Adding instance parameter definitions using a shared parameter file

```
public bool SetNewParameterToInstanceWall(UIApplication app, DefinitionFile myDefinitionFile)
    {
        // create a new group in the shared parameters file
        DefinitionGroups myGroups = myDefinitionFile.Groups;
        DefinitionGroup myGroup = myGroups.Create("MyParameters1");

        // create an instance definition in definition group MyParameters
        ExternalDefinitionCreationOptions option = new ExternalDefinitionCreationOptions("Instance_ProductDate", SpecTypeId.String.Text);
        // Don't let the user modify the value, only the API
        option.UserModifiable = false;
        // Set tooltip
        option.Description = "Wall product date";
        Definition myDefinition_ProductDate = myGroup.Definitions.Create(option);

        // create a category set and insert category of wall to it
        CategorySet myCategories = app.Application.Create.NewCategorySet();
        // use BuiltInCategory to get category of wall
        Category myCategory = Category.GetCategory(app.ActiveUIDocument.Document, BuiltInCategory.OST_Walls);

        myCategories.Insert(myCategory);

        //Create an instance of InstanceBinding
        InstanceBinding instanceBinding = app.Application.Create.NewInstanceBinding(myCategories);

        // Get the BingdingMap of current document.
        BindingMap bindingMap = app.ActiveUIDocument.Document.ParameterBindings;

        // Bind the definitions to the document
        bool instanceBindOK = bindingMap.Insert(myDefinition_ProductDate,
                                        instanceBinding, BuiltInParameterGroup.PG_TEXT);
        return instanceBindOK;
    }
```
