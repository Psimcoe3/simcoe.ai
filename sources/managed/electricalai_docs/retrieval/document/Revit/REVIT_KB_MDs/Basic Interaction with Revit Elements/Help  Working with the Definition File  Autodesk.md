---
created: 2026-01-28T20:49:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_Working_with_the_Definition_File_html
author: 
---

# Help | Working with the Definition File | Autodesk

> ## Excerpt
> The definition file provides access to shared parameters.

---
The definition file provides access to shared parameters.

## Accessing parameters in the definition file

Use the following steps to gain access to the definition file and its parameters:

1.  Specify the Application.SharedParametersFilename property with an existing text file or a new one.
2.  Open the shared parameters file, using the Application.OpenSharedParameterFile() method.
3.  Open an existing group or create a new group using the DefinitionFile.Groups property.
4.  Open an existing external parameter definition or create a new definition using the DefinitionGroup.Definitions property.

The following classes and methods in the Autodesk.Revit.DB namespace provide access to shared parameters using the Revit API.

-   DefinitionFile Class
    -   Retrieved using the Application.OpenSharedParameterFile() method. Revit uses one shared parameter file at a time.
    -   Represents one shared parameter file.
    -   Contains a number of Group objects.
    -   Shared parameters are grouped for easy management and contain shared parameter definitions.
    -   New definitions can be added as needed.
-   ExternalDefinition Class
    -   The ExternalDefinition object is created by a DefinitionGroup object from a shared parameter file.
    -   External parameter definitions must belong to a Group which is a collection of shared parameter definitions.
-   Application.SharedParametersFilename Property
    -   Get and set the shared parameter file path using this property.
    -   By default, Revit does not have a shared parameter file.
    -   Initialize this property before using. If it is not initialized, an exception is thrown.
        
        ### Create a Shared Parameter File
        

Because the definition file is a text file, it can be created manually or using code.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_0D36FD6D39C342238FAF2997C6DF7514"><tbody><tr><td><b>Code Region 22-3: Creating a shared parameter file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateExternalSharedParamFile</span><span>(</span><span>string</span><span> sharedParameterFile</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>System</span><span>.</span><span>IO</span><span>.</span><span>FileStream</span><span> fileStream </span><span>=</span><span> </span><span>System</span><span>.</span><span>IO</span><span>.</span><span>File</span><span>.</span><span>Create</span><span>(</span><span>sharedParameterFile</span><span>);</span><span>
        fileStream</span><span>.</span><span>Close</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Access an Existing Shared Parameter File

Since Revit can have many shared parameter files, it is necessary to specifically identify the file and external parameters you want to access. The following two procedures illustrate how to access an existing shared parameter file.

#### Get DefinitionFile from an External Parameter File

Set the shared parameter file path as the following code illustrates, then invoke the Application.OpenSharedParameterFile() method.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_B6089AE38BBA40969BC78F2E23CD9C45"><tbody><tr><td><b>Code Region 22-4: Getting the definition file from an external parameter file</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>DefinitionFile</span><span> </span><span>SetAndOpenExternalSharedParamFile</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>string</span><span> sharedParameterFile</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// set the path of shared parameter file to current Revit</span><span>
    application</span><span>.</span><span>SharedParametersFilename</span><span> </span><span>=</span><span> sharedParameterFile</span><span>;</span><span>
    </span><span>// open the file</span><span>
    </span><span>return</span><span> application</span><span>.</span><span>OpenSharedParameterFile</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: Consider the following points when you set the shared parameter path:

-   During each installation, Revit cannot detect whether the shared parameter file was set in other versions. You must bind the shared parameter file for the new Revit installation again.
-   If Application.SharedParametersFilename is set to an invalid path, an exception is thrown only when OpenSharedParameterFile() is called.
-   Revit can work with multiple shared parameter files. Even though only one parameter file is used when loading a parameter, the current file can be changed freely.
    
    #### Traverse All Parameter Entries
    

The following sample illustrates how to traverse the parameter entries and display the results in a message box.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_674A9F985BA149489A6F2961C045BDA2"><tbody><tr><td><b>Code Region 22-5: Traversing parameter entries</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ShowDefinitionFileInfo</span><span>(</span><span>DefinitionFile</span><span> myDefinitionFile</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StringBuilder</span><span> fileInformation </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>(</span><span>500</span><span>);</span><span>

    </span><span>// get the file name </span><span>
    fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"File Name: "</span><span> </span><span>+</span><span> myDefinitionFile</span><span>.</span><span>Filename</span><span>);</span><span>

    </span><span>// iterate the Definition groups of this file</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>DefinitionGroup</span><span> myGroup </span><span>in</span><span> myDefinitionFile</span><span>.</span><span>Groups</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get the group name</span><span>
        fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"Group Name: "</span><span> </span><span>+</span><span> myGroup</span><span>.</span><span>Name</span><span>);</span><span>

        </span><span>// iterate the difinitions</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Definition</span><span> definition </span><span>in</span><span> myGroup</span><span>.</span><span>Definitions</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// get definition name</span><span>
            fileInformation</span><span>.</span><span>AppendLine</span><span>(</span><span>"Definition Name: "</span><span> </span><span>+</span><span> definition</span><span>.</span><span>Name</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>fileInformation</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Change the Parameter Definition Owner Group

The following sample shows how to change the parameter definition group owner.

<table summary="" id="GUID-C6FAC918-DC11-41B6-94FD-F745C3C00D98__TABLE_74AFDA7C512E4465857DFBEC26F63D3D"><tbody><tr><td><b>Code Region 22-6: Changing parameter definition group owner</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ReadEditExternalParam</span><span>(</span><span>DefinitionFile</span><span> file</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get ExternalDefinition from shared parameter file</span><span>
    </span><span>DefinitionGroups</span><span> myGroups </span><span>=</span><span> file</span><span>.</span><span>Groups</span><span>;</span><span>
    </span><span>DefinitionGroup</span><span> myGroup </span><span>=</span><span> myGroups</span><span>.</span><span>get_Item</span><span>(</span><span>"MyGroup"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>myGroup </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ExternalDefinition</span><span> myExtDef </span><span>=</span><span> myGroup</span><span>.</span><span>Definitions</span><span>.</span><span>get_Item</span><span>(</span><span>"MyParam"</span><span>)</span><span> </span><span>as</span><span> </span><span>ExternalDefinition</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>myExtDef </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>DefinitionGroup</span><span> newGroup </span><span>=</span><span> myGroups</span><span>.</span><span>get_Item</span><span>(</span><span>"AnotherGroup"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>newGroup </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// change the OwnerGroup of the ExternalDefinition</span><span>
                myExtDef</span><span>.</span><span>OwnerGroup</span><span> </span><span>=</span><span> newGroup</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
