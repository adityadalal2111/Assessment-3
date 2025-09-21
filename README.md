IT 5016 Assessment 3
Name – Aditya Dalal
Student_ID = 20250218
 
GitHub Link –
https://github.com/adityadalal2111/Assessment-3.git




SUMMARY
This task is divided into four consecutive activities where a simple requisition system is expected to be developed using Python.  Every assignment used the concepts of KISS, DRY, and SoC so that it would be efficient and clear and focus on some particular programming concepts.
The staff information task was created in Task 1 to accept the information about the staff and apply a counter in order to create a separate requisition ID.  This was a demonstration of the use of input techniques and creation of IDs and follows the KISS principle due to its simple design.
Task 2 used the DRY principle where the requisitions_total function used the staff-info to prevent duplication.  It was used to show how mathematical calculations and call of functions can be used by summing up the total value of the request items.
The function requisition approval in Task 3 exhibited SoC by partitioning the responsibilities and determining whether requisitions were approved or not.
Finally, Task 4 made use of prior functions to make it efficient by using display requirements to present all the results.
PRINCIPLE WHICH I HAVE USED 
1. KISS (Keep It Simple, Stupid)
Meaning: Code must not be overly complex and must be as straightforward and simple as possible.
 Where your code uses it:
 Your functions (Staff_Info, Requisitions_Total, Requisition_Approval and Display_Requisitions) have very few stages (input -process-output), and they are not very long, and easy to comprehend.
 E.g. everything you need to do in Staff_Info is collect inputs, automatic generation of requisition ID, and print.  Very KISS: no fixed conditions and other logic.________________________________________
2. SoC (Separation of Concerns)
Meaning: Each part of the code is supposed to deal with some duty.
 Where your code uses it:
 • Staff -Info() only handles the requisition ID and staff information.
 • Requisitions_Total() -> only finds out the overall value of the request.
 • Requisition_Approval() only deals with the number of reference and decision of approval.
 • Display_Requisitions only formats and prints the final result,  This separation of these functions into separate functions avoided mixing logic together that would have made it difficult to maintain and expand programs.________________________________________
 3. DRY (Don’t Repeat Yourself)
Meaning: Reuse aims at avoiding duplication of codes.
 Where used in your code: • You use Staff_Info() more than once in Requisitions_Total() instead of creating staff input code more than once.
 Requisitions total is subsequently reused within Requisition approval.
 • Requisition_Approval() is used again in Display_Requisitions() as the last.
   With this chain of reuse, one will be able to avoid writing the same logic or input many times.  That's DRY at work.
Limitation
The system however does have a number of disadvantages.  It can cause conflict in larger systems or in multi-user system since it relies on a global variable (Requisition_ID_counter) to generate the ID.  Since the software does not require any input checks, it may crash or cause errors in case the prices or quantities of items are entered incorrectly.  In addition, the approval logic is limited in the sense that it fails to support multi-level, or more complex, real-world approval processes and only considers totals less than $500.  These restrictions would be countered; otherwise, reliability and scalability would be enhanced.
Conclusion
The Python reservation system is a first attempt project that features class methods, object-oriented programming, and software principles such as KISS and DRY.  Despite its simplicity and possible enhancement by including error management and long-term storage, it shows the booking, approval, and data management steps in a clear way, which can serve as a strong foundation in the future of its further development and education.
