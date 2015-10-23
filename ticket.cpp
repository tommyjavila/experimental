
// Application to keep track of customers of the latest concerts
// 
//  We want to track which :
//  1. Which seats have not been purchased
//  2. The name of the person who purcased a particular seat


#include <iostream>
#include <string>
#include <cstring>


using namespace std;

const int TICKETS_PER_ROW = 20;

string gold_tix[TICKETS_PER_ROW]; 
string silver_tix[TICKETS_PER_ROW]; 
string bronze_tix[TICKETS_PER_ROW]; 
int available_seat[TICKETS_PER_ROW]; 


string empty_string = "NULL";
int section=0;


void init_rows()
{
   int i;

   for (i=0; i < TICKETS_PER_ROW; i++)
   {
      gold_tix[i] = empty_string;
      silver_tix[i] = empty_string;
      bronze_tix[i] = empty_string;
      available_seat[i] = 0;
   }
}

void print_rows(string row[])
{
   int i;
   for (i=0; i<TICKETS_PER_ROW; i++)
   {
      cout << row[i] << endl;
   }
}


int check_availability(int section, int num_tickets)
{

string tix_section[TICKETS_PER_ROW];

   int number_of_seats = 0;

   switch (section)
   {
      case 1 :   
                   for (int i=0; i<TICKETS_PER_ROW; i++)
                      tix_section[i] = gold_tix[i];
                   break;
      case 2 :   for (int i=0; i<TICKETS_PER_ROW; i++)
                      tix_section[i] = silver_tix[i];
                   break;
      case 3 :   for (int i=0; i<TICKETS_PER_ROW; i++)
                      tix_section[i] = bronze_tix[i];
                   break;
   }

   for(int i=0; i<TICKETS_PER_ROW - num_tickets; i++)
   {
      for (int j=0; j<num_tickets; j++)
      {
            if (tix_section[i+j] !=  empty_string)
            {
               continue;
            }                     
            if (j == num_tickets -1)
            {
               available_seat[number_of_seats++] = i;               
            }
      }
   }
   return (number_of_seats);
}

void save_purchase_info(int section, int seats_to_purchase, int num_tickets)
{

   string customer;
   cout << endl;
   cout << "Enter the name of the customer: " << endl;
   cin >> customer;
   switch (section)
   {
      case 1 :   
                for (int i=seats_to_purchase; i< seats_to_purchase +  num_tickets; i++)
                   gold_tix[i-1] = customer; 
                   break;
      case 2 :   
                for (int i=seats_to_purchase; i< seats_to_purchase +  num_tickets; i++)
                   silver_tix[i-1] = customer; 
                   break;
      case 3 :   
                for (int i=seats_to_purchase; i< seats_to_purchase +  num_tickets; i++)
                   bronze_tix[i-1] = customer;
                   break;
      default  :   cout << " Incorrect section specified. "  << endl;
   }
}


void purchase_tickets()
{
    
   int section = 0;
   int num_tickets = 0;
   int num_of_seats = 0;
   int seats_to_purchase = 0;

   cout << "In Purchase Tickets" << endl;

   cout << endl;
   cout << "Choose which section: " << endl;
   cout << endl;
   cout << "1. Gold" << endl;
   cout << "2. Silver" << endl;
   cout << "3. Bronze" << endl;
   cout << endl;
   cout << endl;
   cin >> section;
   cout << endl;
   
   cout << "How many tickets would you like to purchase? " << endl;
   cin >> num_tickets;   
   cout << endl;
   
   num_of_seats = check_availability(section, num_tickets);   

   cout << "The available seats are: " << endl;
   cout << endl;
   for (int i=0; i<num_of_seats; i++)
   {
     cout << available_seat[i] << endl;
   }
   cout << endl;

   cout << "Which group of tickets would you like to purchase? " << endl;
   cin >> seats_to_purchase;
   cout << endl;
   save_purchase_info(section, seats_to_purchase, num_tickets);

}

bool print_menu()
{
   int choice=0;
    
   cout << endl;
   cout << "Choose one of the following: " << endl;
   cout << endl;
   cout << "1. Show current GOLD seating map" << endl;
   cout << "2. Show current SILVER seating map" << endl;
   cout << "3. Show current BRONZE seating map" << endl;
   cout << "4. Purchase Tickets" << endl;
   cout << "5. Exit" << endl;
   cout << endl;

   cin >> choice;
   cout << endl;
   switch (choice)
   {
      case 1 :   print_rows(gold_tix);
                   break;
      case 2 :   print_rows(silver_tix);
                   break;
      case 3 :   print_rows(bronze_tix);
                   break;
      case 4 :   purchase_tickets();   
                   break;
      case 5 :  return(1);   
      default  :   cout << "Enter a number 1 through 5" << endl;
   }
}


main()
{

  bool bExit = 0;

  init_rows(); 
  init_rows(); 
  init_rows(); 

  cout << "----------------------GOLD------------------------";
  cout << "\n";
  // print_rows(gold_tix);
  cout << "----------------------SILVER------------------------";
  cout << "\n";
  // print_rows(silver_tix);
  cout << "----------------------BRONZE------------------------";
  cout << endl;
  // print_rows(bronze_tix);
  cout << endl;
  while (bExit == 0)
  {
     bExit = print_menu();
  }
   
}

