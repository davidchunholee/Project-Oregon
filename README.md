# Project-Oregon

**Overview:**
Project Oregon aims to simulate a terminal at a transportation hub in Portland. This is a fictional,
futuristic transportation system that involves self-flying pods that can get a customer from one 
specified location in Oregon to another.

**Database Implementation/Purpose:**
The goal of this assignment was to successfully implement a working interface that communicates with
a database. The database holds 5 separate tables (`Customers,` `Engineer_Pods,` `Locations,` `Service_Engineers,`
and `Transport_Pods.` All of these tables are represented in some form in the website and allow for CRUD operations
(Create, Read, Update, Delete).

**How Does It Work?**
The user is introduced with the homepage that shows all current locations that Project Oregon operates in. This
is information taken directly from the `Locations` table in the database. The user proceeds by selecting the 'Book
Ticket' tab on the homepage where he/she can enter personal information along with the number of people and the destination.
Upon clicking the 'Book Ticket' button, the database references the `Transport_Pods` table and its attributes to see if there
is an available pod ie: `operableStatus` = true, `availableSeat` - number of Party <= `seatCapacity`, `inTransition` = false,
currentLocation = Portland. If there is an available pod, it reserves the podID number and relays it to the user to get to that
pod. It then sets the `inTransition` attribute to true, updates the `availableSeat` attribute, and sets the destination appropriately.
Upon arrival, the user is prompted with a review which he/she can select their pod number and let the administration know if there
were any technical issues. Upon submission, the database updates the pod to set `inTransition` back to false. If there was a technical
issue, `operableStatus` becomes false.

**Where can I access the website?**
http://project-oregon.herokuapp.com/
