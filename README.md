## Flipkart Grocery Cart Automation <img src="https://github.com/rehanmondal/Flipkart-Grocery-Cart-Automation/assets/125151906/e5b3a590-558c-4df8-b423-1711cb999903" width="42px;" height="32px;">
<p>
<img src="https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54" width="90px;" height="28px;">
<img src="https://github.com/rehanmondal/rehanmondal/assets/125151906/43d5ce7b-c8b3-4707-8af0-e28b2281dd57" width="90px;" height="28px;">
</p>  

## Tables Contains:
- [Overview](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Working Preview](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Working Steps](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Log Report](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)

## Overview
Automation is the use of technology to perform tasks with where human input is minimized. This includes enterprize applications such as business process automation, IT automation, network automation,automating integration between systems & industrial automation such as robotics and more. In this Flipkart Grocery Automation I have tried to minimize the effort of manual entry of products for search, quantity match and add to cart that element.In one word it is basically controlling the Event Driven Programming with the help of selenium without human interactions.

<p><img src="https://github.com/rehanmondal/Flipkart-Grocery-Cart-Automation/assets/125151906/01c977d5-5b87-48f7-b817-86f32e6e87fc" width="420" height="220"></p>

## Working Preview : 
<img src="https://github.com/rehanmondal/Flipkart-Grocery-Cart-Automation/assets/125151906/c92fcbf4-6d6f-421f-8e32-ddc82cc94038" width="600px;" height="300px;">

## Working Steps
    Human Steps :
    step 1 : Buyer needs to make a manual list of items (such as items.txt file)
    step 2 : Put that file in to the desired folder location and start the python main file.
 Other tasks are automatically done without any human interactions.
 
    Automation Steps :
    step 1: It will add the saved pincode of delivery in the location box (In order to change it is also possible).
    step 2: Next it will read one by one element form the provided item list and search for it.
    step 3: It then matches customer required quiantity with website's available quantity.
    step 4: If quantity or same product found then add to cart else skip that product and search for next.
    step 5: Visit view cart and print the total amount.
    step 6: Finally click On Place order button where confidential Login Password will put through send_keys function(as similar as pincode input). 


## Log Report
        DevTools listening on ws://127.0.0.1:58022/devtools/browser/0eebbf8b-4b0d-4fa7-8e6c-353d0ff9f6ce
    
        ============================ FLIPKART   GROCERY   AUTOMATION ===============================
        ============================ Automation Started Successfully ===============================
    
        Items read successfully from text file
        Home page loaded Succesfully
        Pincode put Succesfully
        Search box found and clear succesfully
        Total number of products available in the list is 5
        
        1 no. product searched Succesfully
        Customer requrements :  500
        Website Availabe     :  500
        1 no. product added to Cart Succesfully
    
        2 no. product searched Succesfully
        Customer requrements :  4
        Website Availabe     :  4
        2 no. product added to Cart Succesfully

        3 no. product searched Succesfully
        Customer requrements :  1
        Website Availabe     :  1
        3 no. product added to Cart Succesfully
                
        4 no. product searched Succesfully
        Customer requrements :  2
        Website Availabe     :  5
        Quantity Not Available  

        5 no. product searched Succesfully
        Customer requrements :  1
        Website Availabe     :  500
        Quantity Not Available
        View Cart Clicked Successfully
        
        Total Amount for the cart elements are : ₹1,257
        Place Order Clicked Successfully

        ============================ Automation Completed Successfully ===============================

Total Time Taken to complete the order process :  1.51 minutes

<img src="https://github.com/rehanmondal/Flipkart-Grocery-Cart-Automation/assets/125151906/1a3cf59d-d3f1-479d-a8c0-9efeaffd9671" width="420" height="220">



