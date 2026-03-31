[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Autodesk.Revit.Exceptions Namespace

---



|  |
| --- |
|  |

# Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm) | The exception that is thrown when a non-fatal application error occurs. |
| Public class | [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The exception that is thrown when one of the arguments provided to a method is not valid. |
| Public class | [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | The exception that is thrown when    a null reference (  Nothing  in Visual Basic)  is passed to a method that does not accept it as a valid argument. |
| Public class | [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method. |
| Public class | [ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The exception that is thrown when each individual argument is OK, but a joint constraint is violated. |
| Public class | [AutoJoinFailedException](666f8a45-18c9-0a1f-1a3f-eaa0ac96f23f.htm) | The exception that is thrown when an autojoin operation failed. |
| Public class | [BackgroundTaskCancelledException](656ff28c-486a-49ea-69e7-53ce76f75567.htm) | The exception thrown when Revit cancels a background operation. Third-party developers are not expected to catch and handle this exception. Instead, if allowed to propagate back to Revit code, it will be handled by Revit. |
| Public class | [CannotOpenBothCentralAndLocalException](13aac793-10be-9bed-90d8-5474a05f0fea.htm) | The exception thrown when both a central model and also a local file for the same central model are opened in the same session. |
| Public class | [CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.htm) | The exception thrown when there is a network communication error involving a file-based central model. |
| Public class | [CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.htm) | The exceptions thrown when a central model can be reached but access is denied due to a lack of access privileges. |
| Public class | [CentralModelAlreadyExistsException](2ffb2cbc-6ab4-c486-b683-96483f33df78.htm) | Exception is thrown when the central model already exists at the specified location. |
| Public class | [CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.htm) | The exception thrown when a central model is busy (locked) and the operation is canceled. |
| Public class | [CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | The base class for exceptions that are common to both file-based and server-based central models or specific to just file-based central models. |
| Public class | [CentralModelVersionArchivedException](9b54c5a2-22f3-ac30-3efd-7ef80adff6ea.htm) | Exception is thrown when last central version merged into the local model has been archived in the central model. Reload Latest or Synchronized with Central needs to be conducted before the current failed operation is retried. |
| Public class | [CheckoutElementsRequestTooLargeException](61162ab4-01c4-cf01-d307-fc45c19ad63d.htm) | Exception is thrown when too many elements are requested for checkout |
| Public class | [CorruptModelException](b1a877a7-6c68-c0e4-25c9-005ee153bc60.htm) | The exception that is thrown when the model is or seems corrupt. |
| Public class | [DirectoryNotFoundException](e6614e11-0fd4-df20-0d2d-02722b779128.htm) | The exception that is thrown when the specified directory could not be found. |
| Public class | [DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | The exception that is thrown when the function cannot execute because a discipline is disabled. The exception specifies which discipline(s) would let the operation succeed. |
| Public class | [ExternalApplicationException](06e9a9a5-c212-2708-3151-301c1f33a96a.htm) | The exception that is thrown when an issue in the Add-Ins resulted in an unexpected error. |
| Public class | [FamilyContextException](b9aae3f6-b261-5328-d685-63d4ad046506.htm) | The exception that is thrown when an operation is invalid in the current family document, because of the type of family. |
| Public class | [FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | The exception that is thrown when the specified file could not be accessed, e.g. read-only, locked by the OS etc. |
| Public class | [FileArgumentAlreadyExistsException](bffdd5da-7a0a-2450-efa8-84a1deeebae3.htm) | The exception that is thrown when the specified file exists. |
| Public class | [FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The exception that is thrown when a method received a filename as an argument and requires it to exist as a precondition. |
| Public class | [FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.htm) | The exception that is thrown when the specified file could not be found. |
| Public class | [ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | The exception that is thrown when making or attempting to make changes that are forbidden during dynamic updates to the model. |
| Public class | [FunctionId](f510babd-969e-98fd-530e-c58fe4c9e5ca.htm) | The information of a function throwing an exception. |
| Public class | [InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | The exception that is thrown when attempting to access a piece of data that is structurally not part of an object at the moment. |
| Public class | [InsufficientResourcesException](658e57bc-6929-4883-d245-dcd832fed696.htm) | The exception that is thrown when the OS runs out of resources, e.g. memory, disk space, or USER or GDI objects. |
| Public class | [InternalException](c52bc6d3-6cd9-26f5-4b27-1646c0711a34.htm) | The exception that is thrown when an issue in the Revit code resulted in an unexpected error. |
| Public class | [InvalidDataStreamException](5501eca1-70f1-3204-fda2-d6abc4e33e03.htm) | The exception that is thrown when the reading or saving operation failed due to parsing error. |
| Public class | [InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | The exception that is thrown when referencing an object that is no longer valid. |
| Public class | [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The exception that is thrown when a method call is invalid for the object's current state. |
| Public class | [InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The exception that is thrown when a method received a pathname as an argument, but the pathname is illegal: too long, invalid characters, etc. |
| Public class | [IOException](30d0cc9b-741e-7695-4f52-d9d747791ec3.htm) | The exception that is thrown when an I/O error occurs. |
| Public class | [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The exception that is thrown by the undo transaction framework when a modification operation is not allowed. |
| Public class | [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The exception that is thrown by the undo transaction framework when the modification operation to the model is outside of a transaction. |
| Public class | [NotTransmittedModelException](6b7f7376-d5bf-e5bd-2c77-446f7c72a047.htm) | The exception thrown when OpenOptions were provided to deal with a transmitted model, but the model is not transmitted. |
| Public class | [ObjectAccessException](7d69a00b-f531-c575-0e55-ea2f3858560d.htm) | The exception that is thrown when an operation is denied, e.g. an attempt was made to set a read-only property. |
| Public class | [OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | The exception that is thrown when an operation is unexpectedly cancelled. |
| Public class | [OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The exception that is thrown when the optional functionality is not available in the installed Revit |
| Public class | [OutdatedDirectlyOpenedCentralException](d38fd86b-6281-788d-bf20-6b896da2fbbb.htm) | The exception thrown when a central model is opened directly and its copy in the session is outdated. If the operation is supported for local files, first resave as local, and try again. |
| Public class | [RegenerationFailedException](787bb389-74c2-5ce7-cdd6-32211209ded2.htm) | The exception that is thrown when a regeneration operation failed. |
| Public class | [RevitServerCollaborationNotAvailableException](220ad785-883e-1b26-8eb0-99ffb55605fb.htm) | The exception that is thrown when Collaboration fails because of an external resource (e.g., Amazon S3) failure. |
| Public class | [RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The exception that is thrown when there is any network communication error happening. |
| Public class | [RevitServerException](cb9f496c-f65b-7d27-0fe4-e42f80261b38.htm) | The exception that is base class for all exceptions originating from the Revit server. |
| Public class | [RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | The exception that is thrown when there is any server internal error happening. |
| Public class | [RevitServerModelAlreadyExistsException](a3ed0157-0a46-0b62-62db-08112e1645bd.htm) | The exception that is thrown when there is a model with the same name already exist. |
| Public class | [RevitServerModelNameBreaksConventionException](ec0e702a-f076-1b44-4277-feefd39045d4.htm) | The exception that is thrown when the model is breaking the project naming convention. |
| Public class | [RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.htm) | The exception that is thrown when an unauthenticated user attempts to initiate a call to RevitServer. |
| Public class | [RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.htm) | The exception that is thrown when a call to the server is unauthorized. |
| Public class | [TransientElementCreationException](5d572105-6feb-10ad-db16-4d09de36de2e.htm) | The exception that is thrown when TransientElementCreationScope is used incorrectly. |
| Public class | [TransmittedModelException](5fb430a2-bbcc-34d2-6524-f38972b585ac.htm) | The exception thrown when model was transmitted (sent by eTransmit) and insufficient OpenOptions were provided to handle its transmitted flag. |
| Public class | [WrongUserException](e445bf18-84d1-83f2-6b24-45a6a6fe2bd9.htm) | The exception thrown when a local model is manipulated under a different username than it was created with. |